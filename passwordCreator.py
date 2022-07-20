#This program generates a random password of the length specified by the user & saves it to a folder.

import random

passLength = int(input("Enter the length of the password: "))
password = ""
for i in range(passLength):
    password = password + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,./<>?")
print('We generated ' + password + ' for you.')

savePass = input('Do you want to save the password? (y/n): ')
if savePass == 'y':
    accountName = input('What website is this password for? ')

    file = open('password.txt', 'a')
    file.write(accountName + "\n" + password + "\n\n")
    file.close()
    print('Password saved to password.txt')
elif savePass == 'n':
    print('Password not saved.')
else:
    print('Invalid input.')
    print('Password not saved.')
