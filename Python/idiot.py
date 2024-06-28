# Write your code here :-)
import pyinputplus as pyip
Language = pyip.inputMenu(['English', 'Espanol'], numbered=True)
if Language == '1':
    while True:
        prompt = 'Want to know how to keep an idiot busy for hours?\n'
        response = pyip.inputYesNo(prompt)
        if response == 'no':
            break
else:
    while True:
        prompt = '¿Quieres saber como mantener ocupado a un idiota durante horas?\n'
        response = pyip.inputYesNo(prompt, yesVal='Si', noVal='no')
        if response == 'no':
            break
print('Thank you have a nice day')
