def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(is_palindrome('radar'))
print(is_palindrome('raddar'))
print(is_palindrome('ruddar'))

