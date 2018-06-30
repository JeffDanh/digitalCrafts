# 1
phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '968-345-2345'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

# Exercise 2: Nested Dictionaries
print()
ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}
print(ramit.get('email'))
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

# Letter Summary
from collections import Counter
letters = []
def letter_histogram(word):
    # for key in word:
    #     if key not in letters.items():
    #         letters[key] = word.count(key)
    for letter in word:
        letters.append(letter)
    print(letters)
    print(Counter(letters))
print(letter_histogram('banana'))  

# Word Summary
words = []
def word_histogram(para):
    p = para.split()
    p_counter = Counter(p)
    return p_counter
print(word_histogram('to be or not to be'))



