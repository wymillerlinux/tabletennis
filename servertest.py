'''
Miller Ping Test program
Written by Wyatt Miller (wjmiller2016@gmail.com)
Copyright 2016, licensed by the MIT license

Out of inspriation, I used Python to create a ping test program that runs
on a time scheduler (i.e. cron) and reports the total ping successes or
failures on servers/workstations that has been tested.

todo: gotta make sure this program works on all operatings systems (i.e nt, posix, etc.)
''' 
import os
import sys

success = 0
failure = 0

def pingtest(hostname, servername):
    global success
    global failure
    response = os.system("ping " + hostname)

    if response == 0:
        print servername, 'is up!'
        success += 1
    else:
        print servername, 'is down!'
        failure += 1

print "Miller Ping Test program, Copyright Wyatt Miller 2016-2017"

print "Testing to see if all servers that are in your home/office are running!"

print "\nTesting your own computer for loopback!"
pingtest('127.0.0.1', 'Computer')

print "\nTesting gateway!"
pingtest('192.168.1.1', "Gateway")

print "\nTesting file server!"
pingtest('192.168.1.100', "File server")

print "\nTesting over!"
print success, "successes!"
print failure, "failures!"
print "Copyright Wyatt Miller, 2016-2017, MIT"