print('введите шестизначное число:')
a = int(input())
a1 = a // 1000
a2 = a % 1000

b = a1 % 10
c = a1 // 10
d = c % 10
f = c //10
j = b + d + f

b2 = a2 % 10
c2 = a2 //10
d2 = c2 % 10
f2 = c2 //10
j2 = b2 + d2 + f2

if j == j2:
    print('yes')
else:
    print('no')
