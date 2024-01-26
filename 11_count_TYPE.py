from wordplay import words 

#How many words contain the substring "TYPE”?

count_TYPE = 0
for word in words:
    if "TYPE" in word:
        count_TYPE += 1
print(count_TYPE)