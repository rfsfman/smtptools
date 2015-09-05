#!/usr/bin/python3

import argparse
import re
import smtplib
from email.mime.text import MIMEText
from email.parser import Parser
#
# dictionary with SMTP session settings
#
smtp_options = {"to":['test@localhost', "recipient of the message"],
                "From":['test@localhost',"sender of the message."],
                "server":['localhost',"IP address or hostname of a server to connect"],
                "body":[None,"You can use prepared eml file to fill message body."],
                "ehlo":['localhost',"EHLO value in SMTP session"],
                "attach":['',"Attach file to a message"],
                "file":["","Open prepared eml"]}

# additional arguments about number of messages/sessions and etc
""" number of concurrent threads. Number of messages that will be send
    is calculated as multiplication of threads and repeat values.
    N = Threads * Repeat  
"""
extra_options = { "dir":['',"Use dir option to send the whole content of directory"], # directory contains prepared eml files to send
                  "repeat":[1,"Send email N times. Default value is 1"], # send email N times. By default send one email only once.
                  "threads":[1,"Number of concurrent threads sending emails. Default : 1 thread."]
}

# TODO 
"""emailRegex = re.compile(r'''(
    (([\w])+  | (\w\.\w) )                 #local part
    @
    ([a-zA-Z0-9.-]{4,253}  |        #domain part
    \[ (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \.
    (\d{1,2}| 1\d{1,2} | 2[0-5]{2})
    \]) |
    ([a-zA-Z0-9-]+\.[a-zA-Z]{2,}) 
    )''')
""" 
    
    
def create_mail(options):
    if !options["file"]:
        if options["body"] != None:
        msg = MIMEText(str(options["body"]))
    
        else:
            msg  = MIMEText("This is empty body")
        
        msg['Subject'] = 'Testing email from smtptool'    
        msg['From'] = options["from"]
        msg['To'] = options["to"]
        return msg
    else:
        msg = email.message_from_file(options["file"])
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

def  input_validation(email):
    # TODO
    pass
    

def run():
    # TODO
    args = args_initialization()
    options = {}
    options["body"] = args.body
    if args.to != None:
        options["to"] = args.to
    else:
        options["to"] = smtp_options["to"][0]

    if args.From != None:
        options["from"] = args.From
    else:
        options["from"] = smtp_options["From"][0]
    

    if args.server != None:
        options["server"] = args.server
    else:
        options["server"] = smtp_options["server"][0]

    if args.repeat != None and args.repeat > extra_options["repeat"]:
        options["repeat"] = args.repeat
    else:
        options["repeat"] = extra_options["repeat"]

    if args.file != None:
        options["file"] = args.file
        
    message = create_mail(options)        
    for i in range(0,options["repeat"]):
        send_mail(message, options["server"]) 


if __name__ == '__main__':     
    run()
        


