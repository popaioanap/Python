import re

def extract_number(text):
    # Use regular expression to find the first number in the text
    match = re.search(r'\d+', text)
    
    if match:
        # Extract and return the first number found
        return int(match.group())
    else:
        return "Nu avem cifre"

text = input()
result = extract_number(text)
print(result) 


