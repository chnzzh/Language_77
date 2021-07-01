# -*- coding: utf-8 -*-
"""
@author: @chnzzh
@file: switch_77.py
@time: 2021/07/01
@description: main func
"""

from switch_77 import Switcher_77

encode_type = 'gbk'
words = ['我', '爱', '七七', 'qi', '77']

if __name__ == '__main__':
    A = Switcher_77(words=words, encode=encode_type)
    mode = 'e'
    print('Choose mode: /mode\nExit: /e\n')
    while 1:
        str_in = input(f'[{mode}]input:')
        if str_in == '/mode':
            mode = input('encode(e)/decode(d)):\n')
            continue
        if str_in == '/e':
            break
        if mode in ['e', 'encode']:
            A.encode(str_in)
        else:
            A.decode(str_in)
