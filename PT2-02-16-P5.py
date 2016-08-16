
import inflect
def number(x):
    p = inflect.engine()
    print(p.number_to_words(x))
number(987)


from num2words import num2words
def number2(y):
    print(num2words(y, lang='de'))
number2(789)



def spam(numb):
    print('egg' * numb)
    
spam(1)
spam(3)
spam(12)

def SUM (*args):
    print(sum(args))

SUM(1,2,3,4,78)
