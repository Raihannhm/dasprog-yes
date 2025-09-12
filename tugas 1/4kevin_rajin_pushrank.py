n = int(input("masukkan skor : "))

if n<899:
    print("bronze")
elif 899<=n<=1097:
    print("warior")
elif 1098<=n<=3500:
    print("mythic")
elif 3501<=n<=4737:
    print("legend")
elif n>4737:
    print("epic")