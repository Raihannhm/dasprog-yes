n = int(input())
hasil = 0

for i in range(n):
    a = list(map(int,input().split()))
    if a.count(1)>=2:
        hasil += 1

print(hasil)

