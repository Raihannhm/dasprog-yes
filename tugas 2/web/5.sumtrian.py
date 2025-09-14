t = int(input())
o = []
for _ in range(t):
    n = int(input())
    segitiga = []

    for _ in range(n):
        baris = list(map(int, input().split()))
        segitiga.append(baris)

    for j in range(n-2, -1, -1):
        for k in range(len(segitiga[j])):
            segitiga[j][k] += max(segitiga[j+1][k], segitiga[j+1][k+1])

    o.append(segitiga[0][0])
for g in o:
    print(g)