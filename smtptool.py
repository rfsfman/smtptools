#!/usr/bin/python3

import argparse
import re
import smtplib
from email.mime.text import MIMEText

#
# dictionary with SMTP session settings
#
smtp_options = {"to":['test@localhost', "recipient of the message"],
                "from":['test@localhost',"sender of the message."],
                "server":['localhost',"IP address or hostname of a server to connect"],
                "body":[None,"You can use prepared eml file to fill message body."],
                "ehlo":['localhost',"EHLO value in SMTP session"],
                "attach":['',"Attach file to a message"]}

# additional arguments about number of messages/sessions and etc
""" number of concurrent threads. Number of messages that will be send
    is calculated as multiplication of threads and repeat values.
    N = Threads * Repeat  
"""
extra_options = { "dir":['',"Use dir option to send the whole content of directory"], # directory contains prepared eml files to send
                  "repeat":[1,"Send email N times. Default value is 1"], # send email N times. By default send one email only once.
                  "threads":[1,"Number of concurrent threads sending emails. Default : 1 thread."]
}

emailRegex = re.compile(r'''(
    (\s*)?[a-zA-Z0-9]{1,64}  | \w\.\w #local part
    @
    ([a-zA-Z0-9.-]{4,253}  |        #domain part
    \[ (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \])
    )''')
    
    
    
def create_mail(options):
    if options{"body"}[0] != None:
        msg = MIMEText(str(smtp_options{"body"}[0]))
        
    else:
        msg  = MIMEText("This is empty body")
        
    msg['Subject'] = 'Testing email from smtptool'    
    msg['From'] = options{"from"}[0]
    msg['To'] = options{"to"}[0]
    return msg    

def send_mail(mail,host):
    s = smtplib.SMTP(host)
    s.send_message(mail)
    
                                                  
def args_initialization():
    parser = argparse.ArgumentParser(description="Utility to send mails on specified server")
    for k,v in smtp_options.items():
        req = False
        if v[0] == None:
            req = True
        parser.add_argument("--"+k,help=v[1],required=req)
       
    for  k,v in extra_options.items():
        parser.add_argument("--"+k,help=v[1])

    return parser.parse_args()

def  input_validation():
    # TODO
    pass

def user_input():
    # TODO
    args = args_initialization()
    
     
user_input()
        


