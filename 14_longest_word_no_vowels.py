from wordplay import words

#What is the longest word that contains no vowels? 


# - assumes Y is can be word

#Creating an array of words with no vowels
vowels = 'AEIOU'
words_with_no_vowels = []

for word in words:
    vowel_in_word = False
    for char in vowels:
        if char in word:
            vowel_in_word = True
            break
    if not vowel_in_word:
        words_with_no_vowels.append(word)

longest_word = words_with_no_vowels[0]

#Finding the longest word
for word in words_with_no_vowels:
    if len(word) > len(longest_word):
        longest_word = word

print(f'Longest Word: {longest_word}, Length: {len(longest_word)} ')
