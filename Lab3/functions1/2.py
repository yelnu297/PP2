def Fahrenheit_to_centigrade(F):
    C = 5/9 * (F - 32)
    return C

F=float(input())
C=Fahrenheit_to_centigrade(F)
print(f"{C} centigrade")