import re
def checkpassword(password):
  
    low = re.search(r"[a-z]", password)
    up = re.search(r"[A-Z]", password)
    num = re.search(r"[0-9]", password)
    if ((low == None) or (up == None) or (num == None)):
        return "Bad Password"
    else:
        return "Good password"

if __name__ == "__main__":
    password = input("New password: ")
    print(checkpassword(password))
