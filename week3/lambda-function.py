# lambda declaration
snack = lambda: print("Ringoz")
snack()

# lambda function that accepts arguments
num_square = lambda num: num ** 2
print("The square of num is",  num_square(8))

# checking if a string is  a  palindrome
isPalindrome = lambda string: "Palindrome" if string == string[::-1] else "Not palindrome."
string = input("Enter string:")

print(isPalindrome(string))
