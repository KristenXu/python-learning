# -*- coding: utf-8 -*-
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5, 3)
print power(5)

#要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]):
#     L.append('END')
#     return L
# print add_end()
# print add_end()


#可变参数：自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2) #5
calc() #0

nums = [1, 2, 3]
calc(*nums) #14

#关键字参数：自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30) #name: Michael age: 30 other: {}
person('Adam', 45, gender='M', job='Engineer') #name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw) #name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}