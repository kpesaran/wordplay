from wordplay import words 

#Create and print an array containing all of the words that end in "GHTLY"

end_in_GHTLY = []

for word in words:
    if word[-5:] == 'GHTLY':
        end_in_GHTLY.append(word)
print(end_in_GHTLY)
