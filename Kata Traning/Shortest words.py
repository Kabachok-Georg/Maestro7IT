def find_short(s):
    words = s.split(' ')
    words.sort(key=len)
    return len(words[0]) # l: shortest word length

find_short("need more money")
