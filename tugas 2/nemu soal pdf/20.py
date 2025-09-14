a = list(map(int,input().split()))
x, y = map(int,input().split())

q = a[x]
w = a[y]

q+=w
print(q)