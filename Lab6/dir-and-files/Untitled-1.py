n = 50
def a(n):
    while n>0:
        if n%2==0 and n%3==0:
            yield
        n-=1

for b in a(50):
    print(b)
