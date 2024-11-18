#1
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#2
def number_to_string(num):
    return str(num)
#3 
def get_count(sentence):
    vowel = {'a','e','i','o','u'}
    count = sum(1 for char in sentence.lower() if char in vowel)