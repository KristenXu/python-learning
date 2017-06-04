L = [x * x for x in range(10)]
print L #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print g #<generator object <genexpr> at 0x104feab40>
# print g.next() #0
for n in g:
    print n

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib(6):
    print n

def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o = odd()
o.next() #step 1
o.next() #step 2
o.next() #step 3