'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

reverse_order = []
for w in words:
    reverse_order.append(w[::-1])

with open("words_reverse.txt", "w") as fout:
    fout.write("\n".join(reverse_order))