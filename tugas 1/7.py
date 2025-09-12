n = int(input("masukkan angka : "))

a = "#"
b = "*"

c = a*2 + b*2 # c = ##**
ulg = (n//len(c)) + 1
hasil = (c*ulg)[:n]
print(hasil)
