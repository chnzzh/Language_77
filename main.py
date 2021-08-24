# -*- coding: utf-8 -*-
"""
@author: @chnzzh
@file: switch_77.py
@time: 2021/07/01
@description: main func
"""

from switch_77 import Switcher_77

# 编码类型
encode_type = 'gbk'     # 使用gbk编码中文长度较短
# 编码字符列表
words = ['绝绝子', '好喝到', '跺', 'jio', '暴风吸入']

if __name__ == '__main__':
    # 实例化
    A = Switcher_77(words=words, encode=encode_type)

    mode = 'e'
    print('Choose mode: /mode\nExit: /e\n')
    while 1:
        str_in = input(f'[{mode}]input:')
        if str_in == '/mode':
            mode = input('encode(e)/decode(d):\n')
            continue
        if str_in == '/e':
            break
        if mode in ['e', 'encode']:
            # 编码，返回结果字符串
            print(A.encode(str_in))
        else:
            # 解码，返回结果字符串
            print(A.decode(str_in))
