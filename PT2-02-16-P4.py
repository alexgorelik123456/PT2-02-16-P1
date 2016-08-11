
str_input = 'c*!@#$%^&*()a'
dictionary = ['car', 'carpet', 'rat', 'rabbit', 'carmageddon', 'caramba', 'lufthansa', 'carnival', 'Canada', 'absolut', 'carlsberg']

def autocomplete(str_input, dictionary):
    str1 = []
    for symbol in str_input:
        if symbol.isalpha():
            str1.append(symbol)
    str1 = ''.join(str1)
    print(str1)
    words_found = []
    for word in dictionary:
        if word.startswith(str1):
            words_found.append(word)
    print(words_found[:5])


autocomplete(str_input, dictionary)