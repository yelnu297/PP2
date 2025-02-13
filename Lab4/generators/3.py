N = int(input())

def kratnoe_generator(N):
    for i in range(N+1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

a = kratnoe_generator(N)

for krat in a:
    print(krat)
