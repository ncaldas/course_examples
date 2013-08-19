def is_palindrome(s):
    inversed = ''
    for letter in s:
        inversed = letter + inversed
    if s == inversed: 
        return True
    else:
        return False

def is_palindrome(s):
    return s[::-1] == s

def rotate_word(n,m):
    m = m % 26
    rotate = ''
    for letter in n:
        num = ord(letter) + m 
        if num >= 97 and num <= 122:
            rotate += chr(num)
        elif num < 97:
            rotate += chr(123-(97-num))
        else:
            rotate += chr(96+(num-122))
    return rotate

def is_sorted(a):
    return a == sorted(a)

def is_anagram(n,m):
    if letter in n == letter in m:
        return True 
            #but how to run over all the letter?

def has_duplicates(l):
    distinct = []
    for element in l:
        if element in distinct:
            return True
    else:
        distinct.append(element)

def has_duplicates(l):
    if len(set(l)) == len(l):
        return False
    else: 
        return True

def remove_duplicates(a):
    return list(set(a))

def get_words():
    f = open("words.txt", "r")
    f = f.read
    u = []
    for element in f:
        if element in u not in f:
            u += element
    return u.append(element)

def get_words_freq():
    f = open("words.txt, "r")
    f = f.read
    words = {}
    for element in word:
        if element in f:
            f[element] += 1
        else:
            f[element] = 1
    return words

def invert_dict(d):
    f = {}
    for element in d:
        if element in f:
            f[element] += 1
        else:
            f[element] = 1



