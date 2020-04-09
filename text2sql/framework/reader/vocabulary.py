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
:py:class:`Vocabulary`
"""
import collections
from text2sql.framework.utils.util_helper import convert_to_unicode


class Vocabulary(object):
    """Vocabulary"""
    def __init__(self, vocab_path, unk_token):
        """
        :param vocab_path: 词表地址，必填
        :param unk_token: unk默认的token，必填
        """
        if not vocab_path:
            raise ValueError("vocab_path can't be None")

        self.vocab_path = vocab_path
        self.unk_token = unk_token
        self.vocab_dict, self.id_dict = self.load_vocab()
        self.vocab_size = len(self.id_dict)

    def load_vocab(self):
        """
        :return:
        """
        vocab_dict = collections.OrderedDict()
        id_dict = collections.OrderedDict()
        file_vocab = open(self.vocab_path)
        for num, line in enumerate(file_vocab):
            items = convert_to_unicode(line.strip()).split("\t")
            if len(items) > 2:
                break
            token = items[0]
            if len(items) == 2:
                index = items[1]
            else:
                index = num
            token = token.strip()

            vocab_dict[token] = int(index)
            id_dict[index] = token

        return vocab_dict, id_dict

    def add_reserve_id(self):
        """添加预留的一些id
        :return:
        """
        pass

    def convert_tokens_to_ids(self, tokens):
        """
        :param tokens:
        :return:
        """
        output = []
        UNK = self.vocab_dict[self.unk_token]
        for item in tokens:
            output.append(self.vocab_dict.get(item, UNK))
        return output

    def convert_ids_to_tokens(self, ids):
        """
        :param ids:
        :return:
        """
        output = []
        for item in ids:
            output.append(self.id_dict.get(item, self.unk_token))
        return output

    def get_vocab_size(self):
        """获取词表大小
        :return:
        """
        return len(self.id_dict)

    def covert_id_to_token(self, id):
        """
        :param id:
        :return: token
        """
        return self.id_dict.get(id, self.unk_token)

    def covert_token_to_id(self, token):
        """
        :param token:
        :return: id
        """
        UNK = self.vocab_dict[self.unk_token]
        return self.vocab_dict.get(token, UNK)



