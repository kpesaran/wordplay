from wordplay import words

#What are all of the words with no vowel and not even a Y?

vowels_and_Y = "AEIOUY"
for word in words:
    vowel_in_word = False
    for char in vowels_and_Y:
        if char in word:
            vowel_in_word = True
            break 
    if not vowel_in_word:
        print(word)

