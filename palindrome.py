string=input("Enter the word:")
word = ("")
for i in string:
    word= i + word
if (string == word):
    print("True")
else:
    print("False")