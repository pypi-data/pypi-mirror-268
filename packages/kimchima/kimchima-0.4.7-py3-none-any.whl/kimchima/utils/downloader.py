
# coding=utf-8
# Copyright [2024] [SkywardAI]
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from kimchima.pkg import logging
from transformers import (
    pipeline, 
    AutoModel,
    AutoTokenizer,
    AutoModelForCausalLM,
    )

logger=logging.get_logger(__name__)



class Downloader:

    def __init__(self):
        raise EnvironmentError(
            "Embeddings is designed to be instantiated "
            "using the `Embeddings.from_pretrained(pretrained_model_name_or_path)` method."
        )
    
    @classmethod
    def model_downloader(cls, *args, **kwargs):
        r"""
        Here we will use pipeline from Huggingface to download the model.
        And save the model to the specified folder.
        """
        model_name=kwargs.pop("model_name", None)
        if model_name is None:
            raise ValueError("model_name is required")

        folder_name=kwargs.pop("folder_name", None)
        pipe=pipeline(model=model_name)
        pipe.save_pretrained(folder_name if folder_name is not None else model_name)
        logger.info(f"Model {model_name} has been downloaded successfully")

    
    @classmethod
    def auto_downloader(cls, *args, **kwargs):
        r"""
        Here we will use AutoModel from Huggingface to download the model.
        It support a wider range of models beyond causal language models,
        like BERT, RoBERTa, BART, T5 and more.

        It returns the base model without a specific head, it does not directly
        perform tasks like text generation or translation.
        """

        model_name=kwargs.pop("model_name", None)
        if model_name is None:
            raise ValueError("model_name is required")
        folder_name=kwargs.pop("folder_name", None)

        model=AutoModel.from_pretrained(model_name)
        model.save_pretrained(folder_name if folder_name is not None else model_name)
        logger.info(f"Model {model_name} has been downloaded successfully")

    
    @classmethod
    def casual_downloader(cls, *args, **kwargs):
        r"""
        Here we will use AutoModelForCausalLM from Huggingface to download the model
        Like GPT-2 XLNet etc. 
        It return a language modeling head which can be used to generate text,
        translate text, write content, answer questions in a informative way.
        """
        model_name=kwargs.pop("model_name", None)
        if model_name is None:
            raise ValueError("model_name is required")

        folder_name=kwargs.pop("folder_name", None)
        # https://github.com/huggingface/transformers/issues/25296
        # https://github.com/huggingface/accelerate/issues/661
        model=AutoModelForCausalLM.from_pretrained(model_name)
        model.save_pretrained(folder_name if folder_name is not None else model_name)
        logger.info(f"Model {model_name} has been downloaded successfully")

    @classmethod
    def auto_token_downloader(cls, *args, **kwargs):
        r"""
        Here we will use AutoTokenizer from Huggingface to download the tokenizer congifuration.
        """
        model_name=kwargs.pop("model_name", None)
        if model_name is None:
            raise ValueError("model_name is required")

        folder_name=kwargs.pop("folder_name", None)
        
        tokenizer=AutoTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(folder_name if folder_name is not None else model_name)
        logger.info(f"Tokenizer {model_name} has been downloaded successfully")