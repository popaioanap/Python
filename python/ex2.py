#Write a script that calculates how many vowels are in a string.


example = "Count number of vowels in a String in Python"
count=0
vowels = ["a", "e", "i", "o", "u"]

for i in range(len(example)):
    if example[i] in vowels:
        count+=1
        
print(count)