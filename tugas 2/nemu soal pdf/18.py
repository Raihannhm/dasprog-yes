ang = int(input("masukkan angka : "))
if ang < 10:
    print("satuan")
elif ang <100:
    print("puluhan")
elif ang < 1000:
    print("ratusan")
else:
    print("lebih dari ratusan")