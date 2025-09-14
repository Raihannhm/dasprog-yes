a, b = list(map(int,input().split()))
c, d = list(map(int,input().split()))

a += c
b += d
a, b = b, a
b -= a
a/=c
b*=a
a = int(a)
b = int(b)
print(a, b)