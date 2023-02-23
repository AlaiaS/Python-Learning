#!/usr/bin/env python3

name = input("Please enter your name:")
print ('Hello,', name)

print('I\'m \"ok\"!')

print('I\'m learning')

# Redirect to a file
print('I\'m learning', file=open('test.txt', 'w'))