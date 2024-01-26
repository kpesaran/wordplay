from wordplay import words

#What are all of the words containing an X and a Y and a Z

for word in words:
    if "X" in word and "Y" in word and "Z" in word:
       print(word) 