is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")
print(is_palindrome("Dziadek lubi babcie !"))