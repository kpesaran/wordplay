from wordplay import words

#What are all of the words that have no E or A and are at least 15 letters long?

for word in words:
    if len(word) >= 15:
        if 'E' not in word and "A" not in word:
            print(word)