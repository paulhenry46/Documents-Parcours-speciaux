a = int(input('a'))
b = int(input('b'))
c = int(input('c'))

delta = b**2-4*a*c
s=1
if(delta > 0):
    x_1 = (-b-(delta)**0.5)/(2*a)
    x_2 = (-b+(delta)**0.5)/(2*a)
elif(delta == 0):
    x= -b/2*a
    s= 0
elif(delta < 0):
    x_1 = (-b-1j*(-delta)**0.5)/(2*a)
    x_2 = (-b+1j*(-delta)**0.5)/(2*a)

if (s==1):
    print('les solutiions sont', x_1,x_2)
elif(s==0):
    print('la solution est', x)