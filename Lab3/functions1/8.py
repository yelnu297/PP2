def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0
    
    for num in nums:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7])) 
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 
