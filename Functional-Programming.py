# Higher order function

# %%
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
# %%
# map/reduce
def normalize(name):
    return name[0].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
# %%

from functools import reduce
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
# %%
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    n = 0
    while s[n] != '.': 
        s1 = s[0:n]
        n = n+1
        return s1
    m = -1
    while s[m] !='.': 
        s2 = s[m:]
        m = m-1
        return s2
    def char2num(s):
        return DIGITS[s1].append(DIGITS[s2])
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, s)) / 10 ** len(s2) 

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
# %%

# filter

def is_palindrome(n):
    while str(n) == str(n)[::-1]:
        return n
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# %%
# sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return sorted(t[0])

L2 = sorted(L, key=by_name)
print(L2)
# %%
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2
# %%

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
# %%
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)    
# %%

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
# %%
