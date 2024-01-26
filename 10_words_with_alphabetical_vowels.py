from wordplay import words

# What are all of the words that have all 5 vowels, in alphabetical order? 

vowels = 'AEIOU'
for word in words:
    word_index = 0
    vowel_index = 0
    while word_index < len(word) and vowel_index < len(vowels):
        if word[word_index] == vowels[vowel_index]:
            vowel_index +=1
        word_index +=1
    if vowel_index == len(vowels):
        print(word)




