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
