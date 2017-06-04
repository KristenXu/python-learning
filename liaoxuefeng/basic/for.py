sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
sum2 = 0
for index,x  in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print index
    sum2 = sum2 + x
print sum2

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
for k, v in d.iteritems():
    print k, v