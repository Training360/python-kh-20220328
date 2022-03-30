def separate_words(text):
    state = "out_word"
    word_part = ""
    words = []
    c: str
    for c in text:        
        if c.isalpha() and state == "out_word":
            word_part += c
            state = "in_word"
        elif c.isalpha() and state == "in_word":
            word_part += c
        elif not c.isalpha() and state == "out_word":
            pass
        else:
            words.append(word_part)
            word_part = ""
            state = "out_word"
    if len(word_part) > 0:
        words.append(word_part)
    return words

print(separate_words("Ez bonyi, ugye"))