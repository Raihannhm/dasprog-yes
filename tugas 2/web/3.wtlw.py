n = int(input())
hasil = []

for i in range(n):
    a = str(input())
    if len(a)>4:
        hasil.append(f"{a[0]}{len((a)[1:-1])}{a[-1]}")
    else:
        hasil.append(a)

for h in hasil:
    print(h)