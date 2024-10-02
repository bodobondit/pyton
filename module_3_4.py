def single_root_words(root_word, *other_words):
    same_words = []
    root_word_ = root_word.lower()
    for word in other_words:
        word_ = word.lower()
        if word_.find(root_word_) != -1:
            same_words.append(word)
        if root_word_.find(word_) != -1:
            same_words.append(word)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
