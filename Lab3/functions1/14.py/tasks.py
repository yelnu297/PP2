# tasks.py

def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0
    for num in nums:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False

def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

def histogram(lst):
    for num in lst:
        print('*' * num)

def grams_to_ounces(grams):
    return 28.3495231 * grams
