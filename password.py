import random
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
print("please input into the console how long you want your random password to be")
x = int(input())
endpassword = ""
for i in range(0, x):
    num = random.randint(0, 72)
    endpassword = endpassword + alph[num]
print(endpassword)
