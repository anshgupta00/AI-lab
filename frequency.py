# 11)WAP to ask for a sentence and calculate the frequency of characters in the sentences.

# Ask the user for a sentence
sentence = input("Enter the sentence you like: ")

# Split the sentence into words
words = sentence.split()

# Print the words
print("Words in the sentence:", words)

# Dictionary to store total character frequencies across all words
total_char_frequency = {}

# Iterate over each word in the sentence
for word in words:
    # Split the word into characters
    characters = list(word)
    
    # Print the list of characters
    print(f"Characters in the word '{word}':", characters)
    
    # Count the frequency of each character in the word
    char_frequency = {}
    for char in characters:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    # Print the character frequency for this word
    print(f"Character frequencies in '{word}': {char_frequency}")
    
    # Update the total character frequency
    for char, freq in char_frequency.items():
        total_char_frequency[char] = total_char_frequency.get(char, 0) + freq

# Print the total frequency of each character in the entire sentence
print("\nTotal character frequency across the entire sentence:")
for char, freq in total_char_frequency.items():
    print(f"'{char}': {freq}")



