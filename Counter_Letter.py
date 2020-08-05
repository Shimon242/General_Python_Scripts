def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if not letter in result:
      result[letter] = 0
    # Add or increment the value in the dictionary
    result[letter] += 1
  return result

print(count_letters("AaBbCc"))

print(count_letters("Math is fun! 2+2=4"))


print(count_letters("This is a sentence."))
