def smallest_palindrome(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    smallest = s
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) < len(smallest):
                smallest = substring
    return smallest

s = input("Enter a string: ")
print("Smallest palindrome substring:", smallest_palindrome(s))
