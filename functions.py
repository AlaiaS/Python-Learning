# %%
a = abs(-1000)
print(a)
# %%
m = max(1, 2, 3, 4, 5)
print(m)
# %%  
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


# %%
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# %%
isinstance('a', str)
# %%
import math
def mul(*x):
    n = 1
    if x == ():
        return "At least one parameter is required"
    else:
        for i in x:
            n = n * i
        return n   
print('mul(5) =', mul(5))
# %%
print('mul(5, 6) =', mul(5, 6))
# %%
print('mul(5, 6, 7) =', mul(5, 6, 7))
# %%
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# %%
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
# %%
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))
# %%