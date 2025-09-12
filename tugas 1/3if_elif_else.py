S1, S2, S3 = map(str,input("masukkan 3 kata : ").split())

if len(S1)<len(S2)>len(S3) or len(S1)>len(S2)<len(S3):
    print("Yeehaaw")
elif len(S1)<len(S2)<len(S3) or len(S1)>len(S2)>len(S3):
    print("Woohoohoo")
else:
    print("Hebwueh")