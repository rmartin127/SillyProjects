# Write your code here :-)
while True:
    print('Enter your age:', end = ' ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password, (Letters and Numbers only): ')
    password = input()
    if password.isalnum():
        print('To change your password please input the password again')
        validation = input()
        if len(validation) == len(password) and validation in password:
            break
        else:
            print('passwords do not match, try again')
    print('Passwords can only contain letters and numbers.')



