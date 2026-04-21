def demtu(s, word):
    return sum(1 for w in s.lower().split() if w.strip(',.!?;:')==word.lower())