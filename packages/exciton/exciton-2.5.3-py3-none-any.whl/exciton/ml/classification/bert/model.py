import json
import os
from typing import Any, List

import torch
from torch.autograd import Variable
from transformers import AutoModel, AutoTokenizer

from .utils import Attention_Classifier


class Classfication_Model(object):
    """Classification Model.

    Args:
        topic_name (str, optional): task name. Defaults to sentiment.
        path_to_model (str, optional): path to model. Defaults to None.
        drop_rate (float, optional): dropout rate. Defaults to 0.1.
        n_classes (int, optional): number of labels. Defaults to 2.
        device (str, optional): device. Defaults to "cpu".
    """

    def __init__(
        self,
        topic_name: str = None,
        path_to_model: str = None,
        drop_rate: float = 0.1,
        n_classes: int = 2,
        device: str = "cpu",
    ):
        if path_to_model is None:
            HOME = os.path.expanduser("~")
            MODEL_DIR = "exciton/models/nlp/pretrained"
            path_to_model = f"{HOME}/{MODEL_DIR}/xlm-roberta-large"
        self.path_to_model = path_to_model
        self.drop_rate = drop_rate
        self.n_classes = n_classes
        self.device = torch.device(device)
        self.topic_name = topic_name
        self.train_modules = {}
        self.base_modules = {}
        self.batch_data = {}
        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(f"{path_to_model}/tokenizer")

    def build_modules(self):
        """Declare all modules in your model."""
        self.base_modules["encoder"] = AutoModel.from_pretrained(
            f"{self.path_to_model}/models",
            output_hidden_states=True,
            output_attentions=True,
        ).to(self.device)
        self.TOK_START = 0
        self.TOK_END = 2
        self.TOK_PAD = 1
        with open(f"{self.path_to_model}/models/config.json", "r") as fp:
            params = json.load(fp)
        self.hidden_size = params["hidden_size"]

    def build_classifier(self):
        """Build classifier"""
        self.train_modules[f"cls_{self.topic_name}"] = Attention_Classifier(
            self.hidden_size, self.hidden_size, self.n_classes, self.drop_rate
        ).to(self.device)

    def _build_pipe(self, train_base_model: bool = False) -> torch.FloatTensor:
        """Build Encoder.

        Args:
            train_base_model (bool, optional): train base model. Defaults to False.

        Returns:
            torch.FloatTensor: encode vector.
        """
        if not train_base_model:
            with torch.no_grad():
                input_enc = self.base_modules["encoder"](
                    input_ids=self.batch_data["input_ids"],
                    attention_mask=self.batch_data["pad_mask"],
                )
                input_enc = input_enc[0]
        else:
            input_enc = self.base_modules["encoder"](
                input_ids=self.batch_data["input_ids"],
                attention_mask=self.batch_data["pad_mask"],
            )
            input_enc = input_enc[0]
        return input_enc

    def _build_pipe_classifier(self, input_enc: torch.FloatTensor) -> torch.FloatTensor:
        """Classifier.

        Args:
            input_enc (torch.FloatTensor): input vector.

        Returns:
            torch.FloatTensor: output.
        """
        logits = self.train_modules[f"cls_{self.topic_name}"](
            input_enc,
            self.batch_data["attn_mask"],
        )
        return logits

    def _build_batch(self, batch_raw: List[Any]):
        """Build Batch

        Args:
            batch_data (List[Any]): batch data.
        """
        tokens_arr = []
        input_data_raw = []
        max_length = 0
        for itm in batch_raw:
            out = self.tokenizer.encode(itm["text"])[1:-1]
            tokens_arr.append(out)
            if max_length < len(out):
                max_length = len(out)
            input_data_raw.append(itm)
        max_length = min(500, max_length)
        tokens_out = []
        for itm in tokens_arr:
            itm = itm[:max_length]
            itm += [self.TOK_PAD for _ in range(max_length - len(itm))]
            itm = [self.TOK_START] + itm + [self.TOK_END]
            tokens_out.append(itm)
        tokens_var = Variable(torch.LongTensor(tokens_out))
        # padding mask.
        pad_mask = Variable(torch.FloatTensor(tokens_out))
        pad_mask[pad_mask != float(self.TOK_PAD)] = -1.0
        pad_mask[pad_mask == float(self.TOK_PAD)] = 0.0
        pad_mask = -pad_mask
        # attention mask.
        attn_mask = Variable(torch.FloatTensor(tokens_out))
        attn_mask[attn_mask == float(self.TOK_START)] = -1.0
        attn_mask[attn_mask == float(self.TOK_END)] = -1.0
        attn_mask[attn_mask == float(self.TOK_PAD)] = -1.0
        attn_mask[attn_mask != -1.0] = 0.0
        attn_mask = attn_mask + 1.0
        # batch_data
        self.batch_data["max_length"] = max_length
        self.batch_data["input_ids"] = tokens_var.to(self.device)
        self.batch_data["pad_mask"] = pad_mask.to(self.device)
        self.batch_data["attn_mask"] = attn_mask.to(self.device)
        self.batch_data["input_data_raw"] = input_data_raw
