# coding:utf8
import os
import getpass
import re
import signal



def getPid( keyword = None ) :
    ret_list = []
    
    if keyword is None:
        return []
    reader = os.popen('ps aux | grep "' + keyword + '"' );

    #print( 'ps aux | grep "{}"'.format(keyword) )

    line = reader.readline();
    while line != '' :
        try:
            line.index('grep')
            #print( line )
            line = reader.readline();
            continue;
        except Exception as e:
            pass;
        #print( line )
        tmp = line.split(' ');
        resList = [];
        for i in tmp:
            if i != '':
                resList.append(i)

        #print( '{}'.format(resList) );
        ret_list.append(resList[1]);
        line = reader.readline();
    return ret_list;

def killProcess( pid, keyword = None ) :
    os.kill(pid, signal.SIGKILL)
        
if __name__ == '__main__':
    pidList = getPid('ssh -fNR xshadow.cn:6667:127.0.0.1:22 fy@xshadow.cn')
    pidList = getPid('xshadow.cn')
    for pid in pidList:
        print( "kill -> " + pid );
        killProcess(int(pid));
