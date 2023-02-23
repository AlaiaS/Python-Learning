print('I\'m learning \nPython.')
print(r'\\\t\\')
print('\\\n\\')
print('''line1
line2
line3''')

age = int(input('Please enter your age:'))
if age >= 18: 
    print('adult')
else: 
    print('teenager')

a = "ABC"
b = a
a = "XYZ"
print(b)

print(10 // 3)
print(10 % 3)

print(ord('A'))

name = input('Please enter your name:')
print('Hello, %s' % name)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Growth rate: %d %%' % 7)

r = 2.5
s = 3.14 * r * r
print(f'The area of a circle with radius {r} is {s:.2f}.')
print(f'The area of a circle with radius {r} is {s:2d}.')

past_grade = int(input('Please enter your past grade:'))
present_grade = int(input('Please enter your present grade:'))
change_percentage = (present_grade - past_grade) / past_grade * 100
print(f'Your grade has changed by {change_percentage:.1f}%.')

#使用list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
len(classmates)

classmates = 'Michael', 'Bob', 'Tracy'
print(classmates)
len(classmates)

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates.insert(1, 'Adam')
classmates[1] = 'Sarah'
print(classmates)

#Practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0]) #取出Apple
print(L[1][1]) #打印Pyhon
print(L[2][2]) #打印Lisa

height = int(input('Please enter your height:'))
weight = int(input('Please enter your weight:'))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')