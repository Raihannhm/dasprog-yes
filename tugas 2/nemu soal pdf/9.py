a, b = list(map(int,input().split()))
c, d = list(map(int,input().split()))

a += c
b += d
a, b = b, a
print(a, b)