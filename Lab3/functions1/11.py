a = input()
b = ''.join(reversed(str(a)))
if a == b:
    print("Yes")
else:
    print("No")