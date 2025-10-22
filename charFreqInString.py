def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage
text = input("Enter a string: ")
frequency = char_frequency(text)
print("Character frequencies:", frequency)
