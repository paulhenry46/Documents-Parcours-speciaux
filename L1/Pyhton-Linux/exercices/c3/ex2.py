n = int(input("Donnez une température "))
if n < 0:
    s = "SOLIDE"
elif (n <= 100) & (n >= 0):
    s = "LIQUIDE"
elif n > 100:
    s = "GAZEUX"
print(s)