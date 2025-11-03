def MatchPattern(text : str, pattern : str):
    indexes = []
    for i in range (0, len(text)):
        if text[i:i+len(pattern)] == pattern:
            indexes.append(i)
    return indexes
