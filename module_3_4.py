def single_root_(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


print(single_root_('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))