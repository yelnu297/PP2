thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #apple, orange, banana, cherry

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #apple, banana, cherry, orange

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #apple, banana, cherry, kiwi, orange
