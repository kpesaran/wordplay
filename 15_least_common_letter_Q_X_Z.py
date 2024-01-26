from wordplay import words


#Which of the letters Q, X, and Z is the least common?

letter_Q_count = 0
letter_X_count = 0
letter_Z_count = 0

for word in words:
    for char in word:
        if "Q" == char:
            letter_Q_count += 1
        if "X" == char:
            letter_X_count += 1
        if "Z" == char:
            letter_Z_count += 1

if letter_Q_count and letter_X_count > letter_Z_count:
    print('letter Z count:', letter_Z_count)
elif letter_Z_count and letter_X_count > letter_Q_count:
    print('letter Q count:', letter_Q_count)
else:
    print('letter X count:', letter_X_count)