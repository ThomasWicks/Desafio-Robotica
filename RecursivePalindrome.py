def Palidrome(word):
    if len(word) < 1:
        return "This word is a Palidrome"
    else:
        if word[0].lower() == word[-1].lower():
            return Palidrome(word[1:-1])
        else:
            return "This word is not a Palidrome"

if '__main__' == __name__:
    print("Input a word:")
    word = input()
    print(Palidrome(word))
    