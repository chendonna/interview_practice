def  calculate(expression):
    len_e = len(expression)
    i = 0
    # traverses through the list and concatenates the expression so that all
    # products will first be calculated, creating a list with only summations
    while (i < len_e):
        if expression[i] == '*':
            product = int(expression[i-1]) * int(expression[i+1])
            # puts the product in the i - 1 index (before the multiplication sign)
            expression[i-1] = str(product)
            # creates a list that takes out the multiplication sign and the value after
            # it so that the expression will only have the products and addition signs
            expression = expression[:i] + expression[i+2:]
            len_e -= 2 # decreases length by 2 to compensate for deleting 3 elements of the expression

            # dont increment i in this case we want i to be at the index after
            # the product which it currently is
        else:
            i += 1

    # this leaves it so that all integers in the expression can just be summed up
    sum = 0
    for n in expression:
        if n != '+':
            sum += int(n)

    return sum

print(calculate(['1', '*', '2', '*', '1', '*', '4']))
