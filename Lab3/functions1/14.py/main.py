# main.py

from tasks import spy_game, unique_elements, histogram, grams_to_ounces

print("Test spy_game:")
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

print("\nTest unique_elements:")
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
print(unique_elements([1, 1, 1, 1, 1]))
print(unique_elements([5, 6, 7, 8, 9, 6, 7]))

print("\nTest histogram:")
histogram([4, 9, 7])

print("\nTest grams_to_ounces:")
print(grams_to_ounces(100))
