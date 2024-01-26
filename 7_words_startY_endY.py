from wordplay import words

#What are all of the words that both start and end with Y?

for word in words: 
    if word[0] == "Y" and word[-1] == "Y":
        print(word)