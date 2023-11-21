string=input("Enter the string:")
print(string)

freq_char={}

for i in string:
    if i in freq_char:
        freq_char[i]=freq_char[i]+1
    else:
        freq_char[i] = 1
result= max(freq_char, key = freq_char.get)

print("Most frequent character: ",result)