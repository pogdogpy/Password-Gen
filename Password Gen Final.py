#Created By pogdog#2220 <3

import random
import string
import time
print("Welcome To Pogdogs' Password Generator, Please Enter Your Desired Characters Below")
time.sleep(1)

input_string = input('Enter characters separated by space ')
print("\n")
user_list = input_string.split()



random.shuffle(user_list)
print(*user_list, sep = "")

print("Your Password Has Been Generated, Thanks For Using My Tool")
time.sleep(10)
exit()


