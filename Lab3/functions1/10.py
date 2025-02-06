def unique_elements(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
print(unique_elements([1, 1, 1, 1, 1]))  
print(unique_elements([5, 6, 7, 8, 9, 6, 7]))  