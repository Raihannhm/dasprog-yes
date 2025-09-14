x, y, z = map(int,input("masukkan 3 angka : ").split())
x+=z
if x % y==0:
    print("BISA")
else:
    print("MAAF")