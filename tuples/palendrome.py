# function to check whether palindrome or not
r = (1,2,3,3,2,1)

def palindrome(r):

    index = len(r) - 1
    s = 0

    while s < index:
        if r[s] != r[index]:
            return False
        s += 1
        index -= 1
    return True

if palindrome(r):
    print("The Tuple is palindrome")

else:
    print("The Tuple is not palindrome")