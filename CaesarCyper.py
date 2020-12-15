def Caeser(psw,shift):
    result = ""
    for i in range(len(psw)):
        char = psw[i]      
        if (char.lower()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    return result

print("Digite uma senha")
psw = input()
print("digite um shift")
shift = int(input())

print ("Cipher: " + Caeser(psw,shift))