'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 200
b = 33
if b > a: 
  print("b is greater than a")
else:
  print("b is not greater than a") 

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 

a = 33
b = 200

if b > a:
  pass # pass это пустой оператор, который не делает ничего. Он используется когда синтаксически требуется оператор, но никаких действий не требуется.