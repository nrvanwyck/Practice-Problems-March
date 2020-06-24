def constructNote(magazine, note):
    if len(set(note) - set(magazine)) > 0:
        return False
    available_words = {word: magazine.count(word) for word in set(magazine)}
    needed_words = {word: note.count(word) for word in set(note)}
    for word in needed_words:
        if available_words[word] < needed_words[word]:
            return False
    return True
