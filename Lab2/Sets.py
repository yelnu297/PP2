thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) #False Это значит что banana есть в множестве 

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) #{'apple', 'a', 'c', 'bananas', 'John', 'Elena', 'b', 1, 2, 3, 'cherry'} 