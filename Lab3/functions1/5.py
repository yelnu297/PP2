import itertools

def p():
    a = input("Enter a string: ")
    p = itertools.permutations(a)
    for perm in p:
        print(''.join(perm))

p()
