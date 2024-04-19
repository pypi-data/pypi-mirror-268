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

from kimchima.pipelines import PipelinesFactory
from kimchima.utils.chat import chat_summary

class TestChatSummary(unittest.TestCase):
        
        # prepare test data
        def setUp(self):
            self.conversation_model="gpt2"
            self.summarization_model="sshleifer/distilbart-cnn-12-6"
            self.msg = "why Melbourne is a good place to travel?"
            self.max_length = 10
            self.prompt = "Melbourne is often considered one of the most livable cities globally, offering a high quality of life."

            # Load conversation model by using pipeline
            self.pipe_con=PipelinesFactory.customized_pipe(model=self.conversation_model, device_map='auto')

            self.pipe_sum=PipelinesFactory.customized_pipe(model=self.summarization_model, device_map='auto')
        
        @unittest.skip("skip test_chat_summary")
        def test_chat_summary(self):
            """
            Test chat_summary method
            """

            res = chat_summary(
                pipe_con=self.pipe_con,
                pipe_sum=self.pipe_sum,
                messages=self.msg,
                prompt=self.prompt,
                max_length=self.max_length
                )

            # res is str and should not be None
            self.assertIsNotNone(res)
            self.assertIsInstance(res, str)