#Searching rong string word in the string

s1 = 'core java is base to all java and JEE in a java echo system'

search_word = input("Enter a word you want to search in string :")#searching word in the string

if search_word in s1:#condition : if it is available
    print(f'The word {search_word} is found')#so this
else:
    print(f'The word {search_word} is not found')