# https://dailypythonprojects.substack.com/p/python-project-analyze-text-with
# Text Analysis program
# Practicing loops, common string methods, program logic

text = input("Enter a block of text for analysis: ")
total_characters = len(text)
total_words = text.split()
replace_text = text
sentence_punctuation = "!.\"?"
punc_not_sentence = ",:,-,(,)"
word_count = []
total_punctuation = sentence_punctuation + punc_not_sentence
total_sentences = 0

for l in text:
    if l in sentence_punctuation:
        total_sentences += 1

for punc in total_punctuation:
    replace_text = replace_text.replace(punc, "")

words = replace_text.lower().split()
for word in words:
    count = words.count(word)
    word_count.append(count)
    
maximum_word_count = max(word_count)

for index in range(len(words)):
    if maximum_word_count == word_count[index]:
        most_freq_word = words[index]
    
print("Text Analysis Results:")
print("______________________")
print(f"Total Characters: {total_characters}")
print(f"Total Words: {len(total_words)}")
print(f"Total sentences: {total_sentences}")
print(f"Most Frequent Word: {most_freq_word} (used {maximum_word_count} times)")
