m = int(input("Note de Maths "))
p = int(input("Note de PC "))
if (m >= 10) & (p >= 10):
    s = "Felicitation"
elif (m >= 10) & (p < 10) or (m < 10) & (p >= 10):
    s = "Cous de soutient"
elif (m < 10) & (p < 10):
    s = "Non"
print(s)