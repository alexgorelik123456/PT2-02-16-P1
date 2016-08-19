def my_generator():
    yield 'A'
    yield 'B'
    yield 10 / 0

gena = my_generator()

my_text = open('my_text', 'wb')
try:
    my_text.write(b'Hey')
except:
    pass
finally:
    pass

# while True:
#     try:
#         print(gena.next())
#     except StopIteration:
#         break
#     except ZeroDivisionError:
#         break
#     else:
#         print('Not excepted')
#     finally:
#         print('Done')
