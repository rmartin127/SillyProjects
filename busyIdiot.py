# Write your code here :-)
import pyinputplus as pyip
import sys
while True:
    print('Would you like to know how to keep an idiot busy for hours?')
    response = pyip.inputMenu(['yes', 'no'], allowRegexes=[r'^[yYnN]$'])
    if response == 'yes' or response == 'y' or response == 'Y':
        continue
    elif response == 'no' or response == 'n' or response == 'N':
        print("I guess you don't want to know")
        break
