def checkPalindrome(string):
    if len(string)== 1 or len(string)== 0:
        return True

    elif (string[0]==string[-1]):
        return checkPalindrome(string[1:-1])

    else:
        return False


if __name__ == "__main__":
    while True:
        userIn = input("Enter palindrome : ")

        if userIn != "q":
            if (checkPalindrome(userIn)):
                print("Palindrome!!!")
            else:
                print("Not a palindrome")
            
            continue
        break
