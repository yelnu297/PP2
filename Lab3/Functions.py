def my_function():
  print("Hello from a function") #def означает определение функции


def my_function(fname):
  print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus") #Emil Refsnes Tobias Refsnes Linus Refsnes


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") #The youngest child is Linus


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)


my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #The youngest child is Linus


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") # **kwargs означает передачу переменного числа аргументов ключевого слова


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") #I am from Sweden I am from India I am from Norway I am from Brazil 


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) #15 25 45


def my_function(x, /):
  print(x)

my_function(3) 
#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)


def my_function(a, b, /, *, c, d):
  print(a + b + c + d) #21

my_function(5, 6, c = 7, d = 8) 



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6) #Recursion Example Results: 1 3 6 10 15 21
