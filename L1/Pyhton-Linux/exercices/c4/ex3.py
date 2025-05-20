sup = 2
inf = 1
m = (sup+inf)/2
sqrt2 = 2**0.5
precision = int(input('precision'))
n=1
while n < precision:
    if(m > sqrt2):
        sup = m
    else:
        inf=m
    n=n+1
    m = (sup+inf)/2
m = (sup+inf)/2

print(m)

sup = 2
inf = 1
m = (sup+inf)/2
sqrt2 = 2**0.5
it = int(input('precision'))
n=1
for i in range(it-1):
    if(m > sqrt2):
        sup = m
    else:
        inf=m
    it=it+1
    m = (sup+inf)/2
m = (sup+inf)/2
print(sup,inf)
print(m)