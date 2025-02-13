N = int(input())

def even_generator(N):
    for i in range(N+1):
        if (i % 2 == 0):
            yield i

a = even_generator(N)

for even in a:
    print(even)
