a = str(input())
b = str(input())

b2 = b[::-1]

hasil = ""

for huruf, hrf in zip(a,b2):
    if huruf.isalpha() and hrf.isalpha():
        n = (ord(hrf.lower()) - ord(huruf.lower())) % 26
        if huruf.islower():
            asc = (ord(huruf) - ord('a') + n) % 26 + ord('a')
            hasil += chr(asc)
        else:
            asc = (ord(huruf) - ord('A') + n) % 26 + ord('A')
            hasil += chr(asc)
            
        
if b2==hasil:
    print(f"Silahkan berjalan sejauh {n} Meter")
else:
    print("mending pulang aja")