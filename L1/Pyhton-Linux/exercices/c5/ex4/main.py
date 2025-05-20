from utils.fact import fact

def sqrt():
    r = float(1.0)
    i = 0
    print(r)
    while abs(1.5*r-(2**0.5)) > 10**(-3):
        print(1.5*r)
        print(abs(1.5*r-(2**0.5)))
        r = r + (1/2 - (1*i))*((-1/9)**(i+1)/(fact(i+1)))
        i=i+1
    return 1.5*r,i+1

print(sqrt())