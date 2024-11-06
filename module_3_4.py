def single_root_words(root_word, *other_words):
    same_words = []

    for i in range(len(other_words)):
        if root_word in other_words[i]:
            same_words.append(other_words[i])
        up_other_words = str(other_words[i])
        if up_other_words.upper() in root_word.upper():
            same_words.append(other_words[i])
    i += 1
    print(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
