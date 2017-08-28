#! /usr/bin/python2.7
# coding:utf8
import sys
import subprocess
import time
import os
import signal
from configTunnel import userOfServer, server, interval, defaultPort, waitTime
from proc import killProcess,getPid

currentPath = sys.path[0]
plt = getPid(currentPath)
if len(plt) > 1:
    print( 'this process is exist :{}'.format(plt) )
    exit()

print( 'normal running tunnel' )
#try:
#    port = sys.argv[1]
#except:
#    port = defaultPort
port = defaultPort

binding = server + ':' + str(port)
local = 'localhost:22'
tunnel = server
if userOfServer != '':
    userOfServer = userOfServer;

ssh_cmd = 'ssh -fNR ' + binding + ':localhost:22 ' + userOfServer + '@' + server + ' -p ' + serverPort
print( '{}'.format(ssh_cmd) )

def isInconnectToServer():
    connection = os.system('ping -c 1 ' + server )
    if connection == 0:
        return True
    else:
        return False

def loopConnect():
    while True:
        print( '=====' + time.asctime(time.localtime()) + '=====' )
        os.system("date")
        if isInconnectToServer():
            sub = subprocess.Popen(ssh_cmd.split(' '))
            pid = sub.pid
            print( "start a new process pid = {}".format(pid) )
            sumTime = 0
            # If  unconnect to the server computer in the time of interval
            # it will break the loop to restart a tunnel SSH forwarded
            # check the network once a minute
            while sumTime < interval:
                time.sleep(waitTime)
                sumTime += waitTime
                if not isInconnectToServer():
                    break;
            #time.sleep(interval)
            #killProcess( getPid(ssh_cmd) );
            pidlist = getPid(ssh_cmd)
            print("=============> ssh pid list")
            print(pidlist)
            for pid in getPid(ssh_cmd):
                killProcess(int(pid))
            print( "kill the process pid = {}".format(pid) )
        else:
            print( "current netwoking is unconnect: {}".format(isInconnectToServer()) )
            time.sleep(waitTime)

if __name__ == '__main__' :
    loopConnect()

