def fact(n: int) -> int:
    nf=1
    for i in range(1,n+1,1):
        nf=nf*i
    return nf

def devLim(x: float):
    r = 1
    i=1
    while r < 2.718:
        r = r + (x**(i))/fact(i)
        i=i+1
        print(r)
    return r,i

print(devLim(1))