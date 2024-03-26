import re
from phone import Phone

pattern = '[0-9][a-z][0-9]'
text = "123 1a2 1cc aa1"
response = re.search(pattern, text)
print(response.group())

pattern = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
text = "aaabbbcc rodrigo123@gmail.com.br fdasffdsafdsa"
response = re.search(pattern, text)
print(response.group())

pattern_phone = "\d{2}\d{4,5}\d{4}"
text = "I like the number 2126451234 and the number 2156356294"
response = re.findall(pattern, text)
print(response)

phone = '2126481234'
phone = Phone(phone)
print(phone)