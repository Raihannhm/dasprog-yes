a = input("masukkan karakter : ")

def konversi(a):
    hasil = 1
    for huruf in a.lower():
        if huruf.isalpha():
            asc = ord(huruf) - ord("a") + 1
            hasil *= asc
        elif huruf.isdigit():
            hasil *= int(huruf)
        elif huruf==" ":
            continue
    return hasil

print(konversi(a))
