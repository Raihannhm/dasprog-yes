N = int(input("baris : "))
M = int(input("kolom : "))

a = "#"
b = "*"

for i in range(N):
    if i%2!=0:
        c = a + b
        ulg1 = (M//len(c)) + 1
        hasil = (c*ulg1)[:M]
    else:
        c = b + a
        ulg2 = (M//len(c)) + 1
        hasil = (c*ulg2)[:M]
    print(hasil)