def shortest_substrings(s, x):
    result = []

    for i in range(len(s)):
        for j in range(i + x, len(s)):
            if s[i] == s[j]:
                substring = s[i:j + 1]
                if len(substring) >= x and substring not in result:
                    result.append(substring)

    min_length = min(len(substring) for substring in result)
    for substring in result:
        if len(substring) == min_length:
            print(substring)