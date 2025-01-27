fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #apple, banana, mango

newlist = [x for x in fruits if x != "apple"]   #apple is not in the list

newlist = [x if x != "banana" else "orange" for x in fruits] #banana is replaced with orange

