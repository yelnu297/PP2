import re

pattern = r"[a-z]+_[a-z]+"

test_strings = [
    "abc_def", 
    "ABC_DEF",     
    "123_abc",    
    "hello_world", 
    "no_underscore", 
    "abc-",      
]

for string in test_strings:
    if re.fullmatch(pattern, string): 
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")