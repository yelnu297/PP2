thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #cherry, orange, kiwi

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #apple, blackcurrant, cherry 

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #apple, blackcurrant, watermelon, cherry

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #apple, banana, watermelon, cherry