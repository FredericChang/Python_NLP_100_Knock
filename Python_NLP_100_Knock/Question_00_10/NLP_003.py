
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text = text.replace('.', '') #delte point
text = text.replace(',', '') #delte comma
words = text.split(' ') #split each word by empty
word_list = []

for word in words:
    word_list.append(len(word))

print(word_list)