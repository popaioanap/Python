#Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.


def most_common_letter(text):
    
    # Create a dictionary to store the frequency of each letter
    letter_frequency = {}
    
    # Iterate through the text and count letter frequencies
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1
    
    # Find the letter with the highest frequency
    most_common = max(letter_frequency, key=letter_frequency.get)
    
    # Return the most common letter and its frequency
    return most_common, letter_frequency[most_common]

text = input()
common_letter, frequency = most_common_letter(text)
print(f"The most common letter is '{common_letter}' ({frequency} times)")
