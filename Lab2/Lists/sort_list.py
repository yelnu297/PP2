thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #pineapple, orange, mango, kiwi, banana

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #50, 65, 23, 82, 100

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #cherry, Kiwi, Orange, banana