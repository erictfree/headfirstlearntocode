def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
           return is_palindrome(word[1:-1])
        else:
            return False

words = ['tacocat', 'radar', 'yak', 'rader', 'kayjak']
for word in words:
    print(word, is_palindrome(word))
