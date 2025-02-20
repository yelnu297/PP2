import re

pattern = r"ab*"

test_strings = ["a", "ab", "abb", "ac", "b", ""]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")