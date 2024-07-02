def reverse_string(string):
    # Base Case - String contains one character
    if (len(string) == 0):
        return ""

    # Recursive case
    else:
        return string[-1] + (reverse_string(string[:-1]))

print(reverse_string("Bunyamin"))