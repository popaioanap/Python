#Write a function that validates if a number is a palindrome.


def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Compare the original string with its reverse
    return num_str == reversed_str

num = int(input())
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
