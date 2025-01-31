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


