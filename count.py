#WAP to ask for a sentence and count the number of words.

sentence= input("Enter the sentence as you like: ").split()
# words=sentence.split()
# words_count=len(words)
words_count=len(sentence)
print(f"The total number of words in the given sentence:{words_count}")
