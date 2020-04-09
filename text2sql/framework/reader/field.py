# -*- coding: utf-8 -*-
#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
:py:class:`Reader` is an abstract class representing
"""
from text2sql.framework.rule import MaxTruncation, DataShape


class Field(object):
    """Filed"""
    def __init__(self):
        self.name = None
        self.data_type = DataShape.STRING
        self.reader_info = None  # 需要什么reader
        self.tokenizer_info = None
        self.need_convert = True  # 是否需要进行文本转id的操作，比如已经数值化了的文本就不需要再转了
        self.vocab_path = None
        self.max_seq_len = 128
        self.embedding_info = None
        self.truncation_type = MaxTruncation.KEEP_HEAD
        self.padding_id = 0
        self.field_reader = None
        self.label_start_id = 4
        self.label_end_id = 5

    def build(self, params_dict):
        """
        :param params_dict:
        :return:
        """
        self.name = params_dict["name"]
        self.data_type = params_dict["data_type"]
        self.reader_info = params_dict["reader"]

        self.need_convert = params_dict["need_convert"]
        self.vocab_path = params_dict["vocab_path"]
        self.max_seq_len = params_dict["max_seq_len"]

        self.truncation_type = params_dict["truncation_type"]
        self.padding_id = params_dict["padding_id"]
        # self.label_start_id = params_dict["label_start_id"]
        # self.label_end_id = params_dict["label_end_id"]

        if params_dict.__contains__("embedding"):
            self.embedding_info = params_dict["embedding"]
        if params_dict.__contains__("tokenizer"):
            self.tokenizer_info = params_dict["tokenizer"]






