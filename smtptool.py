#!/usr/bin/python3

import argparse

#
# dictionary with SMTP session settings
#
smtp_options = {"--to":['test@localhost', "recipient of the message"],
                "--from":['test@localhost',"sender of the message."],
                "--server":['localhost',"IP address or hostname of a server to connect"],
                "body":['',"You can use prepared eml file to fill message body."],
                "--ehlo":['localhost',"EHLO value in SMTP session"],
                "--attach":['',"Attach file to a message"]}

# additional arguments about number of messages/sessions and etc
""" number of concurrent threads. Number of messages that will be send
    is calculated as multiplication of threads and repeat values.
    N = Threads * Repeat  
"""
extra_options = { "--dir":['',"Use dir option to send the whole content of directory"], # directory contains prepared eml files to send
                  "--repeat":[1,"Send email N times. Default value is 1"], # send email N times. By default send one email only once.
                  "--threads":[1,"Number of concurrent threads sending emails. Default : 1 thread."]
}

                                                  
def args_initialization():
    parser = argparse.ArgumentParser()
    for k,v in smtp_options.items():
        parser.add_argument(k,help=v[1])
       
    for  k,v in extra_options.items():
        parser.add_argument(k,help=v[1])

    args = parser.parse_args()


args_initialization()

