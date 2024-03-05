#1
import re

n = input()
n = re.search("ab*", n)
if n:
    print("Match")
else:
    print("Doesn't match")

#2
n = input()
n = re.search("aabbb+", n)
if n:
    print("Match")
else:
    print("Doesn't match")
    
    
#3
n = input()
n = re.search(r"[a-z]+[_][a-z]+", n)
if n:
    print("Match")
else:
    print("Doesn't match")


#4
n = input()
n = re.search(r"[A-Z]+[a-z]+", n)
if n:
    print("Match")
else:
    print("Doesn't match")

#5
n = input()
n = re.search("a..b", n)
if n:
    print("Match")
else:
    print("Doesn't match")
    
    
#6
def replace_with_colon(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result
input_text = input()
output_text = replace_with_colon(input_text)
print(output_text)


#7
test_str = input()
temp = test_str.split('_')
res = temp[0] + ''.join(ele.title() for ele in temp[1:])
print(str(res))

#8
def split_at_uppercase(text):
    pattern = r'[A-Z]'
    indices = [match.start() for match in re.finditer(pattern, text)]
    parts = [text[i:j] for i, j in zip([0] + indices, indices + [None])]
    parts = [part for part in parts if part]
    return parts
input_text = input()
result = split_at_uppercase(input_text)
print(result)

#9
def insert_spaces(text):
    pattern = r'(?<!\b)(?=[A-Z])'
    result = re.sub(pattern, ' ', text)
    return result
input_text = input()
result = insert_spaces(input_text)
print(result)

#10
def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case
camel_case_string = input()
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
