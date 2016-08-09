L = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

my_second_string = ' alexander.gorelik@gmail.com'
print('')
print(L + my_second_string)
print('')
print('Explicit is better than implicit.' + my_second_string)
print('')
print('length of text=', len(L))
print('')

vowels = 0
for i in L:
    letter = i.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        vowels += 1
print(vowels)
print('')

n=1
while n < 49:
    index_number = 17 * n
    print('%d%s') % (index_number, L[index_number])
    n = n + 1

def to_weird(my_string):
    str1 = my_string.lower()
    str2 = ''
    for num, c in enumerate(str1):
        if num % 2 == 0:
            str2 += c.upper()
        else:
            str2 += c
    print(str2)


to_weird('DON\'T PANIC!')