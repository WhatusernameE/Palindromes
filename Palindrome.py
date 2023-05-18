# Write a program that can take in a string and determine if it is a Palindrome or not
# (NOTE: A palindrome is a word that is the same forwards and backwards).

while True:

    user = input("\nEnter a word and we will find if it is a palindrome.")

    palindrome = user[::-1]

    if user == palindrome:
        print("Your word is a palindrome!", user.capitalize() + ".")
    else:
        print('Your word is not a palindrome :(')