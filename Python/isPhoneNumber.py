# Write your code here :-)
import pyperclip
import re
phoneNumRegex = re.compile(r'\D?\d{3}.*?\d{3}.*?\d{4}')
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12))::
        if not text[i].isdecimal(
            return False
    return True
message = 'Call me at 415-555-1011 tomorrow. (415)555.9999 is my office.'
print('message received: please wait while we check for phone numbers')
phNumber = phoneNumRegex.findall(message)
count = 0
while count < len(phNumber):

    print(f'Number found: {phNumber[count]} copy to clipboard? (y/n)')

    answer = input()
    if answer == 'y':
        pyperclip.copy(phNumber[count])
        print('Copied Successfully')
    if answer == 'n':
        print('ok no problem')
    count += 1

print('Done')
