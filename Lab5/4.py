import re

pattern = r"[A-Z][a-z]+"

test_strings = [
    "Hello",      
    "World",      
    "HELLO",      
    "hello",      
    "Python",     
    "P",          
    "Aaaa",       
    "AaAaAa",     
]
for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")