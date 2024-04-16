# Description: Provides model inferencing capability to the cli

import os
import warnings
import detoxio.config as config

from abc import ABC, abstractmethod
from .utils import get_torch_device, print_verbose

from transformers import logging

def hide_transformers_warnings():
    if not config.debug():
        logging.set_verbosity_error()
        warnings.filterwarnings("ignore")
        os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

# Define a contract for implementing model inference adapters for LLMs
class LLMInferenceAdapter(ABC):
    @abstractmethod
    def inference(self, prompt: str) -> str:
        pass

class TransformersAdapter(LLMInferenceAdapter):
    def __init__(self, model_name: str, max_length=1000, num_return_sequences=1,
                 skip_special_tokens=True,
                 skip_prompt_tokens=True,
                 top_k=10, top_p=1, temperature=1,
                 repetition_penalty=1.5,
                 apply_chat_template=True,
                 pad_token_id=0,
                 do_sample=True):
        self.model_name = model_name
        self.max_length = max_length
        self.top_k = top_k
        self.top_p = top_p
        self.temperature = temperature
        self.do_sample = do_sample
        self.num_return_sequences = num_return_sequences
        self.repetition_penalty = repetition_penalty
        self.skip_special_tokens = skip_special_tokens
        self.skip_prompt_tokens = skip_prompt_tokens
        self.apply_chat_template = apply_chat_template
        self.pad_token_id = pad_token_id

    def inference(self, prompt: str) -> str:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        hide_transformers_warnings()

        device = get_torch_device()
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForCausalLM.from_pretrained(self.model_name).to(device)

        input_ids = None
        if self.apply_chat_template:
            input_ids = tokenizer.apply_chat_template([
                { "role": "system", "content": "You are a chatbot who is helpful and friendly." },
                { "role": "user", "content": prompt }], return_tensors="pt",
                tokenize=True, add_generation_prompt=True).to(device)
        else:
            input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

        print_verbose(f"Prompt input to model: {tokenizer.decode(input_ids[0], skip_special_tokens=True)}")

        output = model.generate(input_ids=input_ids,
                                max_length=self.max_length,
                                num_return_sequences=self.num_return_sequences,
                                top_k=self.top_k, top_p=self.top_p, temperature=self.temperature,
                                pad_token_id=self.pad_token_id, do_sample=self.do_sample)

        output_tokens = output[0]
        if self.skip_prompt_tokens:
            output_tokens = output_tokens[input_ids.shape[-1]:]

        decoded_output = tokenizer.decode(output_tokens, skip_special_tokens=self.skip_special_tokens)
        print_verbose(f"Model output: {decoded_output}")

        return decoded_output

