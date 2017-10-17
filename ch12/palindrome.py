class PalindromeString(str):

    def is_palindrome(self):
        i = 0
        j = len(self) - 1
        while i < j:
            if self[i] != self[j]:
                return False
            i = i + 1
            j = j - 1
        return True

word = PalindromeString('radar')
word2 = PalindromeString('rader')
print(word, 'length is', len(word), 'and uppercase is', word.upper())
print(word, word.is_palindrome())
print(word2, 'length is', len(word2), 'and uppercase is', word2.upper())
print(word2, word2.is_palindrome())
