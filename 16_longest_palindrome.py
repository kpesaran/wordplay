from wordplay import words


palindrome_word_list = []
for word in words:
    if word == word[::-1]:
        palindrome_word_list.append(word)
    


longest_palindrome_word = palindrome_word_list[0]

for word in palindrome_word_list:
    if len(word)> len(longest_palindrome_word):
        longest_palindrome_word = word

print(f'Longest Palidrome: {longest_palindrome_word}, length: {len(longest_palindrome_word)}')
