def find_all_occurrences(text, sub):
    result = []
    i = 0
    while i < len(text) - len(sub) + 1:
        if text[i:i + len(sub)] == sub:
            result.append(i)
            i += len(sub)
        else:
            i += 1
    return result