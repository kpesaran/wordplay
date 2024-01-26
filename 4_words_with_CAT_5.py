from wordplay import words

#What are all of the words that contain the word CAT and are exactly 5 letters long?

for word in words:
    if len(word) == 5 and "CAT" in word:
        print(word)