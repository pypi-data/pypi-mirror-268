
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

logger=logging.get_logger(__name__)


def chat_summary(*args,**kwargs)-> str:
        r"""
        """
        pipe_con=kwargs.pop("pipe_con", None)
        if pipe_con is None:
            raise ValueError("conversation pipeline is required")
        
        pipe_sum=kwargs.pop("pipe_sum", None)
        if pipe_sum is None:
            raise ValueError("summarization pipeline is required")
        
        messages=kwargs.pop("messages", None)
        if messages is None:
            raise ValueError("messages is required")

        prompt=kwargs.pop("prompt", None)
        max_length=kwargs.pop("max_length", None)
        
        response = pipe_con(messages)

        logger.info("Finish conversation pipeline")
        
        if prompt is None:
            return response[0].get('generated_text')
        
        raw_response = prompt + response[0].get('generated_text')
        
        if max_length is None:
            max_length = len(raw_response)

        response = pipe_sum(raw_response, min_length=5, max_length=max_length)

        logger.info("Finish summarization pipeline")

        return response[0].get('summary_text')
