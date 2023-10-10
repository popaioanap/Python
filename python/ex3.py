#Write a script that receives two strings and prints the number of occurrences of the first string in the second.



def count_occurrences(first_string, second_string):
    count = 0
    index = 0

    while index < len(second_string):
        index = second_string.find(first_string, index)
        if index == -1:
            break
        count += 1
        index += 1

    return count

# Input from the user
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

# Call the function and print the result
occurrences = count_occurrences(first_string, second_string)
print(f"The first string occurs {occurrences} times in the second string.")
