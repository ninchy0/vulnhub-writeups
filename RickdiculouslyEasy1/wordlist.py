import string

strings = list()
numbers = list()

for i in string.ascii_uppercase:
    strings.append(i)

for i in string.digits:
    numbers.append(i)
words = ['The', 'Flesh', 'Curtains']


with open('wordlist.txt','w') as f:
    for i in strings:
        for j in numbers:
            for k in words:
                wordlist = i + j + k
                f.write(f'{wordlist}\n')