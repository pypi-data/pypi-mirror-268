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

import unittest

from kimchima.chat_template import ChatTemplateFactory
from kimchima.pkg import (
    TokenizerFactory
)

class TestChatTemplateFactory(unittest.TestCase):
    
        model_name = 'gpt2'
        add_generation_prompt=False
        messages =[{"role": "user", "content": "Hello, how are you?"},
                   {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
                   {"role": "user", "content": "I'd like to show off how chat templating works!"}]

        @classmethod
        def setUpClass(cls):
            cls.tokenizer = TokenizerFactory.auto_tokenizer(pretrained_model_name_or_path=cls.model_name)

        @classmethod
        def tearDownClass(cls):
            pass

    
        def test_prompt_generation(self):
            """
            Test tokenlized prompt_generation method
            """
    
            self.assertIsNotNone(self.model_name)
    
            tokenized_chat = ChatTemplateFactory.prompt_generation(
                model=self.model_name,
                messages=self.messages,
                tokenize=True,
                add_generation_prompt=self.add_generation_prompt
                )
            non_tokenized_chat = ChatTemplateFactory.prompt_generation(
                model=self.model_name,
                messages=self.messages,
                tokenize=False,
                add_generation_prompt=self.add_generation_prompt
                )
            self.assertIsNotNone(tokenized_chat)
            self.assertEqual(self.tokenizer.decode(tokenized_chat[0]), "Hello")
            self.assertIsNotNone(non_tokenized_chat)
            self.assertEqual(len(non_tokenized_chat),147)