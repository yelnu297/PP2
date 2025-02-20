import re

pattern = r"ab{2,3}"

test_strings = ["ab", "abb", "abbb", "a", "abbbb", "ac"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")