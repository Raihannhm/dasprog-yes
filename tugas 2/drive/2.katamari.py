import math
n = int(input())
k = int(math.log(n+1, 2))

if n == 0:
    print("Maybe it's better to add 1 fences, just to be perfect")
else:
    if n==(2**k)-1:
        print("It's the perfect amount, nice!")
    elif (2**k)-1 < n < (2**(k+1))-1:
        slshatas = ((2**(k+1))-1) - n
        slshbwh = n - ((2**k)-1)
        if slshatas < slshbwh:
            print(f"Maybe it's better to add {slshatas} fences, just to be perfect")
        else :
            print(f"Maybe it's better to remove {slshbwh} fences, just to be perfect")
