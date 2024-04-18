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

from transformers import AutoModel, AutoModelForCausalLM
from kimchima.pkg import logging

logger = logging.get_logger(__name__)


class ModelFactory:
    r"""
    ModelFactory class to get the model from the specified model.

    Args:
        pretrained_model_name_or_path: pretrained model name or path
    """
    def __init__(self):
        raise EnvironmentError(
            "ModelFactory is designed to be instantiated "
            "using the `ModelFactory.from_pretrained(pretrained_model_name_or_path)` method."
        )

    @classmethod                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    def auto_model(cls, *args, **kwargs)-> AutoModel:
        r"""
        Here we will use AutoModel from Huggingface to load the model form local.
        It support a wider range of models beyond causal language models,
        like BERT, RoBERTa, BART, T5 and more.

        It returns the base model without a specific head, it does not directly
        perform tasks like text generation or translation.

        """
        pretrained_model_name_or_path=kwargs.pop("pretrained_model_name_or_path", None)
        if pretrained_model_name_or_path is None:
            raise ValueError("pretrained_model_name_or_path cannot be None")

        model = AutoModel.from_pretrained(
            pretrained_model_name_or_path,
            **kwargs
        )
        logger.debug(f"Loaded model: {pretrained_model_name_or_path}")
        return model
    
    @classmethod
    def auto_model_for_causal_lm(cls, *args, **kwargs)-> AutoModelForCausalLM:
        r"""
        Here we will use AutoModelForCausalLM to load the model from local,
        Like GPT-2 XLNet etc. 
        It return a language modeling head which can be used to generate text,
        translate text, write content, answer questions in a informative way.
        """
        pretrained_model_name_or_path=kwargs.pop("pretrained_model_name_or_path", None)
        if pretrained_model_name_or_path is None:
            raise ValueError("pretrained_model_name_or_path cannot be None")

        model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path,
            **kwargs
        )
        logger.debug(f"Loaded model: {pretrained_model_name_or_path}")
        return model

