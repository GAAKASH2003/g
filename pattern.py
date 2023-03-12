import re

text="hello my name is aakash muy phone number is 6300696534"
phone=re.search('\d{2}',text)
print(phone.span())
fir=re.search(r'cat|dog','the dog or cat is here')
sir=re.findall(r'..at','the cat or rat is alive') 
print(fir)
print(sir)
phrase="36 big, lorries are coming in! 9 rows@"
pattern=r'[^!.,]'
my=re.findall(pattern,phrase)
print(my)
# text=re.serach()
# print(''.join(my))
