
word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowelList = [char for char in word.lower() if char in vowels]
print("Vowels in the word:", vowelList)
