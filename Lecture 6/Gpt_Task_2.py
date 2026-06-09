def rev(word, idx=0):
    if idx == len(word):
        return ""

    return rev(word, idx + 1) + word[idx]


print(rev("Hello"))