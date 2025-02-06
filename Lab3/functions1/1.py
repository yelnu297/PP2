def grams_to_ounces(g):
    o = 28.3495231 * g
    return o

g = float(input())
o = grams_to_ounces(g)
print(f"{o} ounces")
