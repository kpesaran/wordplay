from wordplay import words

#What are all the words containing a Q but not a U

for word in words:
    if "Q" in word and "U" not in word:
            print(word)