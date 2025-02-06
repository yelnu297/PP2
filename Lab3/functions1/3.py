def solve(numheads, numlegs):
    x = (4 * numheads - numlegs) // 2
    y = numheads - x
    return x, y

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Куриц: {chickens}, кроликов: {rabbits}")
