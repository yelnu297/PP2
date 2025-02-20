import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

snake_str = "this_is_snake_case"
camel_str = snake_to_camel(snake_str)
print(camel_str)