import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

camel_str = "thisIsCamelCase"
snake_str = camel_to_snake(camel_str)
print(snake_str)