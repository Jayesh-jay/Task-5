string = "Guvi Geeks Network private Limited"
string = string.lower()
vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for char in string:
  if char in vowel_counts:
    vowel_counts[char] += 1
total_vowels = sum(vowel_counts.values())

# Print the results
print("Total number of vowels:", total_vowels)
print("Count of each vowel:")
for vowel, count in vowel_counts.items():
  print(vowel, ":", count)