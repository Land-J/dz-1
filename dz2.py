s = int(input())
a = s //6
b = (a + a) * 2

if (a + a + b) == s:
    print(a, b, a)
else:
    print('некоректно')
