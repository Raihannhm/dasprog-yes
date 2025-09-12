N = int(input("baris : "))
M = int(input("kolom : "))

a = "#"
b = "*"
c = a*2 + b*2 # ##**
d = b*2 + a*2 # **##

for i in range(N):
    if i % 2==0:
        baris1 = (M//len(d)) + 1
        hasil = (d*baris1)[:M]
    else:
        baris2 = (M//len(c)) + 1
        hasil = (c*baris2)[:M]
    print(hasil)