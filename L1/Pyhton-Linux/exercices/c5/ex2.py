def frac(x: float, y:float):
    if y != 0:
        return x/y
    else:
        return 'nan'

print(frac(float(input('x')),float(input('y'))))