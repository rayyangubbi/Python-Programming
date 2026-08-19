text = input("Enter a word: ")

if text.lower() == text[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")
