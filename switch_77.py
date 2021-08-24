# -*- coding: utf-8 -*-
"""
@author: @chnzzh
@file: switch_77.py
@time: 2021/07/01
@description: str and language_qi encode and decode
"""
import re


def qi_int_anybase(int_in, base, ans):
    if int_in == 0:
        return

    d = int_in // base
    qi_int_anybase(d, base, ans)

    rm = int_in % base
    ans.append(rm)
    return


def qi_anybase_int(anybase: list, base: int):
    anybase_r = anybase.copy()
    anybase_r.reverse()
    ans = 0
    b = 1
    for i in anybase_r:
        ans = ans + i*b
        b = b * base

    return ans


class Switcher_77:
    def __init__(self, words=None, encode='utf-8'):
        """

        :param words: list
        :param encode: https://docs.python.org/zh-cn/3.8/library/codecs.html#standard-encodings
        """
        if words is None:
            words = ['q', 'i']
        self.errcode = 0
        self.err = ['NoErr', 'Too little words']
        self.encode_type = encode
        self.words = words
        if words is None:
            words = ['q', 'i']

        self.__pre_treat()
        self.base = len(self.words)

        # Mapping relation
        self.map = [i for i in range(len(self.words))]

        if self.errcode:
            print('Err: ', self.err[self.errcode])

        else:
            print('Congratulations! Using ', self.words)

    def __pre_treat(self):
        """
        check conflicting words and remove
        """

        self.words.sort(key=lambda x: len(x))
        approval_words = []
        flag = True
        for i in self.words:
            for j in approval_words:
                if j in i:
                    flag = False
                    break
            if flag:
                approval_words.append(i)
                flag = True
        self.words = approval_words

        if len(self.words) < 2:
            self.errcode = 1

    def encode(self, str_in: str) -> str:
        str_ec = str_in.encode(self.encode_type)
        str_i = int.from_bytes(str_ec, byteorder='big')

        str_base = []
        qi_int_anybase(str_i, self.base, str_base)

        str_ans = ''.join(self.words[i] for i in str_base)

        return str_ans

    def decode(self, str_in: str) -> str:
        map_rvs = self.map.copy()
        map_rvs.reverse()
        for i in map_rvs:
            str_in = re.sub(r'(?<!\t)%s' % self.words[i], r'\t%s' % i, str_in)
        str_base = [int(i) for i in (re.split(r'\t', str_in)[1:])]
        str_i = qi_anybase_int(str_base, self.base)

        str_ec = int.to_bytes(str_i, length=len(str_base), byteorder='big').lstrip(b'\x00')
        str_ec = str_ec.decode(self.encode_type)

        return str_ec
