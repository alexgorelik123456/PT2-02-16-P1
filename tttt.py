def whisper(x,num):
    def wrapped_function(word):

        x(word.lower() + '!' * num)

    return wrapped_function

@whisper(num=5)
def saysmth(word):
    print(word)


saysmth('Hey!')