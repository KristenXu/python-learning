# -*- coding: utf-8 -*-
print [x*x for x in range(1, 11)] #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print [x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]
print [m + n for m in 'ABC' for n in 'XYZ'] #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os # 导入os模块
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L] #['hello', 'world', 'ibm', 'apple']