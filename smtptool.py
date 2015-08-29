#!/usr/bin/python3

import argparse

#
# dictionary with SMTP session settings
#
smtp_options = {"to":'test@localhost',"from":'test@localhost',
                "server":'localhost',"body":'',
                "ehlo":'localhost',"attach":''}

# additional arguments about number of messages/sessions and etc
""" number of concurrent threads. Number of messages that will be send
    is calculated as multiplication of threads and repeat values.
    N = Threads * Repeat  
"""
extra_options = { "dir":'', # directory contains prepared eml files to send
                  "repeat":1, # send email N times. By default send one email only once.
                  "threads":1,
}

                                                  
def args_initialization():
    parser = argparse.ArgumentParser()
    for k,v in smtp_options.items():
        parser.add_argument(k)
        print("Adding new argument:  " + k)

    for  k,v in extra_options.items():
        parser.add_argument(k)

    parser.parse_args()


args_initialization()

