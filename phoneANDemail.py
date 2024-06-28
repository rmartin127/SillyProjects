# Write your code here :-)
import pyperclip, re
# phoneNumRegex = re.compile(r'\D?\d{3}.*?\d{3}.*?\d{4}')
phoneNumRegex = re.compile(r'''
((\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegEx = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = pyperclip.paste()
matches = []
for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
for groups in emailRegEx.findall(text):
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
