#Setting up all the words in a list 
with open('sowpods.txt', 'r') as scrabble_words:
    words = []
    for word in scrabble_words:
        words.append(word.strip())


#Question: 
#What are all of the words containing UU?
words_with_UU = []
for word in words:
    if 'UU' in word:
        words_with_UU.append(word)
#to display answer: 
#print(words_with_UU)


#Question: 
#What are all of the words containing an X and a Y and a Z
words_with_X_Y_Z = []
for word in words:
    if "X" in word and "Y" in word and "Z" in word:
       words_with_X_Y_Z.append(word) 
#to display answer: 
#print(words_with_X_Y_Z)

#Question: 
#What are all the words containing a Q but not a U
words_with_Q_not_U = []
for word in words:
    if "Q" in word and "U" not in word:
            words_with_Q_not_U.append(word)
#To Display Answer:
#print(words_with_Q_not_U)

#Question: 
#What are all of the words that contain the word CAT and are exactly 5 letters long?
words_with_CAT_5 = [] 
for word in words:
    if len(word) == 5 and "CAT" in word:
        words_with_CAT_5.append(word)
#To Display Answer:
#print(words_with_CAT_5)

#Question: 
#What are all of the words that have no E or A and are at least 15 letters long?
words_no_E_A_15plus =[] 
for word in words:
    if len(word) >= 15:
        if 'E' not in word and "A" not in word:
            words_no_E_A_15plus.append(word)
#To Display Answer:
#print(words_no_E_A_15plus)
        
#Question: 
#What are all of the words that have a B and an X and are less than 5 letters long?
words_B_X_5less = []
for word in words:
    if len(word) < 5 and "B" in word and "X" in word:
        words_B_X_5less.append(word)
#To Display Answer:
#print(words_B_X_5less)

#Question: 
#What are all of the words that both start and end with Y?
words_startY_endY = []
for word in words: 
    if word[0] == "Y" and word[-1] == "Y":
        words_startY_endY.append(word)
#To Display Answer:
#print(words_startY_endY)

#Question: 
#What are all of the words with no vowel and not even a Y?
vowelsAndY = "AEIOUY"

words_no_vowels_includingY = []
for word in words:
    vowel_in_word = False
    for char in vowelsAndY:
        if char in word:
            vowel_in_word = True
            break 
    if not vowel_in_word:
        words_no_vowels_includingY.append(word)
# To display answer as an array
#print(vowel_in_word)

#Question: 
# What are all of the words that have all 5 vowels, in any order?
vowels = "AEIOU"
words_with_all_vowels = [] 
for word in words: 
    vowel_in_word = True
    for char in vowels:
        if char not in word:
            vowel_in_word = False
            break
    if vowel_in_word:
        words_with_all_vowels.append(word)
# To Display Answer
# print(words_with_all_vowels)

#Question: 
# What are all of the words that have all 5 vowels, in alphabetical order? 
words_with_alphabetical_vowels = []
vowels = "AEIOU"

for word in words:
    word_index = 0
    vowel_index = 0
    while word_index < len(word) and vowel_index < len(vowels):
        if word[word_index] == vowels[vowel_index]:
            vowel_index += 1
        word_index += 1
    if vowel_index == len(vowels):
            words_with_alphabetical_vowels.append(word)
#to display answer:
#print(words_with_alphabetical_vowels)


#Question: 
#How many words contain the substring "TYPE”?
type_count = 0
for word in words:
    if "TYPE" in word:
        type_count += 1
# To display an answer
# print(type_count)

#Question: 
#Create and print an array containing all of the words that end in "GHTLY"
end_in_GHTYL = []
for word in words:
    if word[-5:] ==  "GHTLY":
         end_in_GHTYL.append(word)
#To display all the words
#print(end_in_GHTYL)

#Question:
#What is the shortest word that contains all 5 vowels?

shortest_word_all_vowels = words_with_all_vowels[0]
for word in words_with_all_vowels:
    if len(word) < len(shortest_word_all_vowels):
        shortest_word_all_vowels = word
# To display answer:
#print(shortest_word)



#What is the longest word that contains no vowels? Assumes Y is allowed. 

vowels = "AEIOU"
words_no_vowels = []
for word in words:
    vowel_in_word = False
    for char in vowels:
        if char in word:
            vowel_in_word = True
            break 
    if not vowel_in_word:
        words_no_vowels.append(word)

longest_word_no_vowels = words_no_vowels[0]
for word in words_no_vowels:
    if len(word) > len(longest_word_no_vowels):
        longest_word_no_vowels = word

#To display Answer
#print(longest_word)
    

#Question
#Which of the letters Q, X, and Z is the least common?
letter_Q_count = 0
letter_X_count = 0
letter_Z_count = 0

for word in words:
    for char in word:
        if "Q" == char:
            letter_Q_count += 1
        if "X" == char:
            letter_X_count += 1
        if "Z" == char:
            letter_Z_count += 1
#To Display Answer: 
# if letter_Q_count and letter_X_count > letter_Z_count:
#     print('letter Z count:', letter_Z_count)
# elif letter_Z_count and letter_X_count > letter_Q_count:
#     print('letter Q count:', letter_Q_count)
# else:
#     print('letter X count:', letter_X_count)

#  Question: answered same question as above but used dictionary
dic = {"X":0, "Q":0, "Z":0}
for word in words:
    for char in word:
        if char in dic:
            dic[char] += 1
min_letter = ""
min_count = float('inf')  
for letter , count in dic.items():
    print(letter, count)
    if count < min_count:
        min_letter = letter
        min_count = count
# to display answer
#print(f"letter {min_letter} count: {min_count}")


#Question
#What is the longest palindrome?
palindrome_list = []
palindrome_word = ''
palidrome_length = 0
for word in words:
    if word == word[::-1]:
        palindrome_list.append(word)

for word in palindrome_list:
    if len(word) > palidrome_length:
        palidrome_length = len(word)
        palindrome_word = word
# to display answer:
# print(palindrome_word)



# Question: 
# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for word in words:  
    word_index = 0
    while word_index < len(word)-1:
        if word[word_index] in alphabet:
            if word[word_index] == word[word_index+1]:
                alphabet = alphabet.replace(word[word_index],'')
        word_index += 1
#to display answer: 
#print(alphabet)
