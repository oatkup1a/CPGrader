a=float(input())
L=0
U=a
while True:
    x=(L+U)/2
    if abs(a-(10**x)) <= 10**(-10)*max(a,10**x):
        print(round(x,6))
        break
    if 10**x > a:
        U = x
    else:
      10**x < a
      L = x