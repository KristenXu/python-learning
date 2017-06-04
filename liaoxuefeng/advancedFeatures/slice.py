# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3] #['Michael', 'Sarah', 'Tracy']
L[:3] #['Mi#chael', 'Sarah', 'Tracy']
L[1:3] #['Sarah', 'Tracy']
L[-2:] #['Bob', 'Jack']



L1 = range(10)
#拷贝
M = L1[:]
print L1
L1[0] = 1
print M #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ,做了一次深拷贝

L2 = range(100)
#前10个数，每两个取一个：
L2[:10:2] #[0, 2, 4, 6, 8]
#所有数，每5个取一个：
L[::5] #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

(0, 1, 2, 3, 4, 5)[:3] #(0, 1, 2)

'ABCDEFG'[:3] #'ABC'