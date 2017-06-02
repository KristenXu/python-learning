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
print calc(1, 2)
nums = [1, 2, 3]
print calc(*nums)

#关键字参数：自动组装为一个dict