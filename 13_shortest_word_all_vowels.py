from wordplay import words

#What is the shortest word that contains all 5 vowels?

#creating an array with all words with all vowels

words_with_all_vowels = []
vowels = 'AEIOU'
for word in words:
    vowel_in_word = True
    for char in vowels:
        if char not in word:
            vowel_in_word = False
            break
    if vowel_in_word:
        words_with_all_vowels.append(word)

shortest_word = words_with_all_vowels[0]

#finding the shortest word
for word in words_with_all_vowels:
    if len(word) < len(shortest_word):
        shortest_word = word
print(f'Shortest Word: {shortest_word}, Length: {len(shortest_word)}')
