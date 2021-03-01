#!/usr/bin/python3
# Written by: Alsalt Alkharosi


import requests
import time
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def scanner():
    domain = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename,'r')
    output = open('subdomains.vcs','w')
    print(bcolors.FAIL+'[*] Scanning for subdomains'+bcolors.ENDC)
    time.sleep(3)
    print(bcolors.FAIL+'[*] This might take few minutes...'+bcolors.ENDC)

    for subdomain in file.readlines():

            directory = subdomain.strip('\n')
            url = 'http://'+directory+'.'+domain # You may change 'http://' to 'https://' if the website use 'SSL/TLS'
            try:
                requests.get(url)
            except requests.ConnectionError:
                print(bcolors.FAIL+'[-]'+url+bcolors.ENDC)
            
            except KeyboardInterrupt:
            	print('CTRL+C was clicked to stop the scan!')
            	exit(1)
            else:
                print(bcolors.OKGREEN+'[+]' + url+bcolors.ENDC)
                output.write('[+]'+url+'\n')


if __name__=='__main__':
    scanner()
