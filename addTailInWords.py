def add_ing_or_ly(s):
    if s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"

# Example usage
text = input("Enter a string: ")
result = add_ing_or_ly(text)
print("Result:", result)
