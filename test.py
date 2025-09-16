import math 
a=int(input('Write a ='))
b=int(input('Write b ='))
c=int(input('Write c ='))

d = b ** 2 - 4 * a * c

if d > 0: 
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
elif d==0:
    x3 = (-b) / 2*a
else: 
    print('ERROR')
print('hi')   