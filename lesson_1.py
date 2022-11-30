def linear_search(string:str):
    ans = ""
    anscnt = 0
    dct = {}
    if not isinstance(string, str):
        return "It's not a string"
    for now in string:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for key in dct:
        if dct[key] > anscnt:
            ans = key
            anscnt = dct[key]
    return ans

print(linear_search())
