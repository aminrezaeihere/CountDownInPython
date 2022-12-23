import random
print("this is a password generator that includes symbols numbers and alphabet(both capital and lower case) " )
ch = "ABCDEFGHIJKLMNOPQRSTYXWZabcdefghmnlopkrstxywz1234567890!@#$%^&*()"
pw_num = int(input("how long do you want your password to be?: "))
k = 0
pwd = ""
while k < pw_num:
    pw2 = random.choice(ch)
    k += 1
    pwd += "".join(pw2)
print(pwd)
