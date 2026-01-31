text = input("Enter a string: ")

clean_text = text.strip().lower()
reversed_text = clean_text[::-1]

if clean_text == clean_text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")