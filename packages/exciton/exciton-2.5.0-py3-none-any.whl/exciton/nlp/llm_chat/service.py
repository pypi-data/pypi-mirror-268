import os
from typing import Any, Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class Llm_Chat_Model(object):
    """AI is creating summary for __init__

    Args:
        path_to_model (str, optional): path to the model. Defaults to None.
    """

    def __init__(self, path_to_model: str = None) -> None:
        self.path_to_model = path_to_model
        self.train_modules = {}
        self.base_modules = {}
        self.batch_data = {}

        if self.path_to_model is None:
            HOME = os.path.expanduser("~")
            MODEL_DIR = "exciton/models/nlp/llm_chat"
            model = "Llama-2-7B-Chat-GPTQ"
            path_to_model = f"{HOME}/{MODEL_DIR}/{model}"
            self.path_to_model = path_to_model
        self.tokenizer = AutoTokenizer.from_pretrained(f"{path_to_model}/tokenizer")
        self.model = AutoModelForCausalLM.from_pretrained(
            f"{path_to_model}/models",
            device_map="auto",
        )

    def predict(
        self,
        prompt: str,
        max_new_tokens: int = 1028,
        do_sample: bool = False,
        temperature: float = 0.7,
        top_p: float = 0.95,
        top_k: int = 40,
        repetition_penalty: float = 1.1,
        device: str = "cuda",
    ) -> Dict[str, Any]:
        """predict result.

        Args:
            prompt (str): prompt
            max_new_tokens (int, optional): max number of new tokens. Defaults to 1028.
            do_sample (bool, optional): do sampling. Defaults to False.
            temperature (float, optional): temperature. Defaults to 0.7.
            top_p (float, optional): top_p. Defaults to 0.95.
            top_k (int, optional): top_k. Defaults to 40.
            repetition_penalty (float, optional): repetition_penalty. Defaults to 1.1.
            device (str, optional): [description]. Defaults to "cuda".

        Returns:
            Dict[str, Any]: result of llm_chat.
        """
        tokenized_text = self.tokenizer(
            [prompt], padding=False, return_tensors="pt"
        ).to(device)
        sequences = self.model.generate(
            tokenized_text["input_ids"],
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            eos_token_id=self.tokenizer.eos_token_id,
            num_return_sequences=1,
        )
        result = self.tokenizer.decode(sequences[0][1:-1])
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        result = result[len(prompt) :].strip()
        output = {"prompt": prompt, "result": result}
        return output
