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