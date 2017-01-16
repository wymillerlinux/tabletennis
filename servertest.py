'''
Miller Ping Test program
Written by Wyatt Miller (wjmiller2016@gmail.com)
Copyright 2016, licensed by the MIT license

Out of inspriation, I used Python to create a ping test program that runs
on a time scheduler (i.e. cron) and reports the total ping successes or
failures on servers/workstations that has been tested.

todo: add function that reads output to file
'''

import os
import sys
import time

success = 0
failure = 0

def notsupported():
    print "This operating system is not currently supported. Email me!"
    print "wjmiller2016@gmail.com"
    sys.exit(0)

def pingtest(hostname, servername):
    global success
    global failure

    if sys.platform == 'linux2' or sys.platform == 'darwin':
        response = os.system("ping -c 4 " + hostname)
    elif sys.platform == 'win32':
        response = os.system("ping " + hostname)
    else:
        notsupported()

    if response == 0:
        print servername, 'is up!'
        success += 1
    else:
        print servername, 'is down!'
        failure += 1

print "Miller Ping Test program, Copyright Wyatt Miller 2016-2017"
print "Testing to see if all servers that are in your home/office/enterprise are"
print "running!"
time.sleep(3)

print "\nTesting your own computer for loopback!"
pingtest('127.0.0.1', 'Computer')
time.sleep(3)

print "\nTesting gateway!"
pingtest('192.168.1.1', "Gateway")
time.sleep(3)

print "\nTesting file server!"
pingtest('192.168.1.100', "File server")
time.sleep(3)

print "\nTesting game server!"
pingtest('192.168.1.110', "Game server")

print "\nTesting over!"
print success, "successes!"
print failure, "failures!"
print "Copyright Wyatt Miller, 2016-2017"
