def analyze_text(text):
    print("Your text is:\n", text)
    print()

    # Replace sentence-ending symbols with '.'
    text_splitter = ['.', '!', '?']
    new_text = text
    for symbol in text_splitter:
        new_text = new_text.replace(symbol, ".")
    print("This is new input:", new_text)

    # Split into sentences and words
    sentences = new_text.split(".")
    words = new_text.split()
    sentence_list = [s.strip() for s in sentences if s.strip() != ""]
    print("This is sentences:", sentences)
    print("This is words:", words)
    print("This is list:", sentence_list)
    print()

    overall_count = {}
    sentence_number = 1

    for sentence in sentence_list:
        words_i = sentence.split()
        print("Sentence", sentence_number, ":", len(words_i), "words")

        word_count = {}
        for w in words_i:
            w_lower = w.lower()
            # Count per sentence
            if w_lower in word_count:
                word_count[w_lower] += 1
            else:
                word_count[w_lower] = 1
            # Count overall
            if w_lower in overall_count:
                overall_count[w_lower] += 1
            else:
                overall_count[w_lower] = 1

        sorted_items = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        top3 = sorted_items[:3]

        print("  Top 3 words: ", end="")
        for i in range(len(top3)):
            key = top3[i][0]
            value = top3[i][1]
            if i < len(top3) - 1:
                print(key + "(" + str(value) + ")", end=", ")
            else:
                print(key + "(" + str(value) + ")")

        sentence_number += 1

    print()
    print("Total sentences:", len(sentence_list))
    print("Total words:", len(words))

    sorted_overall = sorted(overall_count.items(), key=lambda x: x[1], reverse=True)
    top_overall = sorted_overall[:3]
    print("Top 3 words overall:", end=" ")
    for i in range(len(top_overall)):
        key = top_overall[i][0]
        value = top_overall[i][1]
        if i < len(top_overall) - 1:
            print(key + "(" + str(value) + ")", end=", ")
        else:
            print(key + "(" + str(value) + ")")

text_1 = input("Enter your text 1: ")
text_2 = input("Enter your text 2: ")
analyze_text(text_1)
analyze_text(text_2)