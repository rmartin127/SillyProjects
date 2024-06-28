# Write your code here :-)
import pyperclip
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print('message received: please wait while we check for phone numbers')
phNumber = phoneNumRegex.findall(message)
count = 0
while count < len(phNumber):

    print(f'Number found: {phNumber[count]} copy to clipboard? (y/n)')

    answer = input()
    if answer == 'y' or 'yes':
        pyperclip.copy(phNumber[i])
