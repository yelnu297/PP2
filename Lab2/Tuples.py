thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry') 

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 