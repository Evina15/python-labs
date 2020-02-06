'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

words = []
with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

#the shortest word
shortest_len = min(words, key=len)

for w in words:
    if len(w) == len(shortest_len):
        print(w)


#the longest word
longest_len = max(words, key=len)

for w in words:
    if len(w) == len(longest_len):
        print(w)

#total number of words
total_number = []
for w in words:
    my_number = len(w)
    total_number.append(my_number)
print(sum(total_number))



