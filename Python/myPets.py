# Write your code here :-)
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ', end='')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
