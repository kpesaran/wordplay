from wordplay import words

#What are all of the words that have all 5 vowels, in any order?

vowels = 'AEIOU'
for word in words:
    vowels_in_word = True 
    for char in vowels:
        if char not in word:
            vowels_in_word = False
            break
    if vowels_in_word:
        print(word)

    






