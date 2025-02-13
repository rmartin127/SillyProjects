#!/usr/bin/python3

import requests as r
import sys
import argparse
import getpass




#Initialize Arguments
parser=argparse.ArgumentParser()
parser.add_argument("-f", "--file",default="transcript",help="File name to output,the pdf file extension is added after default is transcript.pdf")
parser.add_argument("--full",action="store_true",help="If used, pulls your full name from the settings of your academy account that will be displayed in the transcript")
args = parser.parse_args()

Filename = args.file +'.pdf'

print(f'''
     ╔═════════════════════════════════════════════════════╗
     ║MarcieLee's Hack The Box Academy Transcript requestor║
     ╚═════════════════════════════════════════════════════╝
      ''')


# Set the session Cookie
sessionCookie='htb_academy_session='+ getpass.getpass("Input your academy Session Cookie here: ")+';'

#Checks for requesting the Full Name (AKA Bob Smith) or default username (aka marcielee)
if args.full == True:
    Name = "full_name"
else:
    Name = "name"
print("Grabbing your transcript, please standby")

# Writes the Transcript
with open(Filename, "wb") as f:
    url = f'https://academy.hackthebox.com/account/transcript?nameIdentifier={Name}'
    info = r.get(url, timeout=30.000, headers={'cookie':sessionCookie},allow_redirects=False)
    if info.status_code != 200:
        print('invalid cookie')
        f.close()
        exit()
    else:
        f.write(info.content)
        f.close()
        print(f"saved transcript as {Filename}")
