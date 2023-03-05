#do slice
# %%
L = list(range(100))
n = L[0:10]
print(n)
# %%
n = L[:10:2]
print(n)
# %%
n = L[::5]
print(n)
# %%
def trim(s):
    if s == '':
        return s
    while s[0] == ' ':
        s = s[1:]
        if s == '':
            return s
    while s[-1] == ' ':
        s = s[:-1]
    return s

# 测试:  
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
# %%

#Iteration
def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = max = L[0]
    for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
    return (min, max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
# %%
print(list(range(20)))
# %%
[x * x for x in range(1, 11)]
# %%
[x * x for x in range(1, 11) if x % 2 == 0]
# %%
[m + n for m in 'ABC' for n in 'XYZ']
# %%
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
# %%
g = (x * x for x in range(10))
# %%
def triangles(max):
    results = [1]
    yield results
    while True:
        results = [v+w for v, w in zip([0]+results, results+[0])]
        yield results
    
for i, row in enumerate(triangles(max)):
    if i > 9:
        break
    print(i, row)

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

if row == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
# %%


def f2(a, b, c=0, **kw):
    x = f3(a)
    print('a =', a, 'x =', x)
    return x
# %%
def f3(test):
    best = test + 2
    return best
f2(3, 1)
# %%
