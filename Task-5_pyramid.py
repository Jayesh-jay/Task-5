for i in range(1, 21):
    for j in range(20 - i):
        print(" ", end=" ")
    # loop for numbers in increasing order
    for k in range(1, i + 1):
        print(k, end=" ")

    #loop for numbers in decreasing order
    for l in range(i - 1, 0, -1):
        print(l, end=" ")

    # next line
    print()