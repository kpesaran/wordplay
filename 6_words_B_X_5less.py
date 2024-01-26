from wordplay import words

#What are all of the words that have a B and an X and are less than 5 letters long?

for word in words:
    if len(word) < 5 and "B" in word and "X" in word:
        print(word)

        