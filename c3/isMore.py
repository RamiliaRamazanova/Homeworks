from PI import *

r = int(input('radus:'))
a = int(input('a:'))
b = int(input('b:'))

if roundSquare(r) > square(a,b):
    print('Circle is more')
elif roundSquare(r) < square(a, b):
    print('Circle is less')
else:
    print('eqvivalent')

