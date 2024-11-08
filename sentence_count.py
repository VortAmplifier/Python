# Project link https://dailypythonprojects.substack.com/p/count-words-in-a-sentence-with-python
#
sentence = input("Enter a sentence: ")
print("The number of words in the sentence is: ", end = "")
word = 0
count = 0
for count_word in sentence:
    if count_word == " ":
        word += 1
word += 1
sent = ""
list_count = []
list_word = []
        
num_words = word
print(num_words)

print("The longest word in the sentence is: ", end = "")

for count_word in sentence:
    if count_word == " ":
        list_word.append(sent)
        sent = ""
        list_count.append(count)
        count = 0
    else:
        sent = sent + count_word
        count += 1

list_word.append(sent)
list_count.append(count)

cnt = 0

for max_index in list_count:
    if max_index == max(list_count):
        break
    cnt += 1

longest_word = list_word[cnt]
print(longest_word)
