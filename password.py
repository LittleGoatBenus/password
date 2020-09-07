import random
import string

#range = input("please enter the range of your password ")
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&/?!" # random characters

length = int(input("password length: "))

for i in range(length):
    passwd = random.choice(string)
    print(passwd, end="") # prints string into 1 line
