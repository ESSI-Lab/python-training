the_input = input("Enter a text: ")
print("Your text is:\n", the_input)
print()

text_splitter = ['.', '!', '?']
new_input = the_input
for symbol in text_splitter:
    new_input = new_input.replace(symbol, ".")
print("This is new input:", new_input)

sentences = new_input.split(".")
words = new_input.split()
the_list = [s.strip() for s in sentences if s.strip() != ""]
print("This is sentences:", sentences)
print("This is words:", words)
print("This is list:", the_list)
print()

sentence_number = 1
for sentence in the_list:
    words_i = sentence.split()
    print("Sentence", sentence_number, ":", len(words_i), "words")
    #print(words_i)
    sentence_number += 1

    word_count = {}
    for w in words_i:
        w_lower = w.lower()
        if w_lower in word_count:
            word_count[w_lower] += 1
        else:
            word_count[w_lower] = 1
    #print(word_count)

    sorted_items = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top3 = sorted_items[:3]
    #print(top3)

    print("The top 3 words: ", end="")
    for i in range(len(top3)):
        key = top3[i][0]
        value = top3[i][1]
        if i < len(top3) - 1:
            print(key + "(" + str(value) + ")", end=", ")
        else:
            print(key + "(" + str(value) + ")")

print()
print("Total sentences:", len(the_list))
print("Total words:", len(words))
print("Top 3 words overall:")
