from wordplay import words

# What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively?

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for word in words:  
    word_index = 0
    while word_index < len(word)-1:
        if word[word_index] in alphabet:
            if word[word_index] == word[word_index+1]:
                alphabet = alphabet.replace(word[word_index],'')
        word_index += 1
print(alphabet)
        








