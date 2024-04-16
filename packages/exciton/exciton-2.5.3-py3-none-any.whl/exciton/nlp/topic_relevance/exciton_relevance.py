import logging
from glob import glob
from typing import Any, Dict, List

import torch

from exciton.ml.classification.bert import Classfication_Model
from exciton.ml.classification.bert.utils import Attention_Classifier


class Exciton_Relevance(Classfication_Model):
    """Topic Relevance Model by Exciton Research.

    Args:
        path_to_model (str): path to model.
        device (str, optional): device. Defaults to "cpu".
    """

    def __init__(self, path_to_model: str, device: str = "cpu") -> None:
        super().__init__(path_to_model=path_to_model, n_classes=2, device=device)
        logging.disable(logging.INFO)
        logging.disable(logging.WARNING)
        self.path_to_model = path_to_model
        self.build_modules()
        self.build_classifier()
        self._init_model_parameters()

    def build_classifier(self):
        """Build classifier"""
        cls_models = glob(f"{self.path_to_model}/models/cls_*.model")
        for clsm in cls_models:
            clsm = clsm.split("/")[-1].split(".")[0]
            self.train_modules[clsm] = Attention_Classifier(
                self.hidden_size, self.hidden_size, self.n_classes, self.drop_rate
            ).to(self.device)

    def _init_model_parameters(self):
        """load model param"""
        for model_name in self.base_modules:
            self.base_modules[model_name].eval()
        for model_name in self.train_modules:
            self.train_modules[model_name].eval()
            model_file = f"{self.path_to_model}/models/{model_name}.model"
            self.train_modules[model_name].load_state_dict(
                torch.load(model_file, map_location=lambda storage, loc: storage)
            )

    def _build_pipe_classifier(
        self, topic: str, input_enc: torch.FloatTensor
    ) -> torch.FloatTensor:
        """Build pipe classifier.

        Args:
            topic (str): topic
            input_enc (torch.FloatTensor): input encoding vector.

        Returns:
            torch.FloatTensor: output.
        """
        logits = self.train_modules[topic](input_enc, self.batch_data["attn_mask"])
        return logits

    def _get_results(
        self, topic: str, batch: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Get results

        Args:
            topic (str): Topic.
            batch (List[Dict[str, Any]]): Batch data.

        Returns:
            List[Dict[str, Any]]: results
        """
        self._build_batch(batch_raw=batch)
        with torch.no_grad():
            input_enc = self._build_pipe()
            logits = self._build_pipe_classifier(topic, input_enc)
        probs = torch.softmax(logits, dim=1)
        probs = probs.squeeze(1).data.cpu().numpy().tolist()
        torch.cuda.empty_cache()
        output = []
        for sen in probs:
            score = sen[1]
            label = 0
            if score >= 0.5:
                label = 1
            output.append({"topic": topic[4:], "label": label, "score": score})
        return output

    def predict(self, topic: str, source: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict labels.

        Args:
            source (List[Dict[str, Any]]): Source data.
            topic (str): Topic.

        Returns:
            List[Dict[str, Any]]: Target labels.
        """
        topic = f"cls_{topic}"
        batch_size = min(20, len(source))
        k = 0
        output = []
        while k * batch_size < len(source):
            batch_text = source[k * batch_size : (k + 1) * batch_size]
            results = self._get_results(topic, batch_text)
            output.extend(results)
            k += 1
        return output
