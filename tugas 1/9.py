n = int(input("masukkan angka : "))

a = "#"
b = "*"

if n%2!=0:
    c = a + b
    ulg = (n//len(c)) + 1
    hasil = (c*ulg)[:n]
else:
    c = b + a
    ulg = (n//len(c)) + 1
    hasil = (c*ulg)[:n]
print(hasil)