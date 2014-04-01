#date 2014-3-28
# --- encoding : utf-8 ---
#func auto start transmisson when get the disk info and umount my disk 


#!/usr/bin/python 

import os
import sys
import time
import argparse

#global variables 
prefix="/Volumes/"
mydiskname=[prefix+'hello',prefix+'psnail',prefix+'system']


#umount the disk
def umountdisk(disknamelist,forceumount):
    #need the root privilege to exeute umount
    if os.environ.get('USER') != 'root':
        print "current user is not root"
        sys.exit(1)
    #lsof the diskname and tell the process
    for diskname in disknamelist:
        if os.path.exists(diskname):
            cmd="lsof "+diskname
        else :
            break

        res=os.popen(cmd).readlines()
        reslen=len(res)
        if reslen > 3 and not forceumount:      #why 3 : the root has two metadataserver process 
            print("the processes use "+diskname+" follow:")
            for line in res:
                 print(line)
        elif reslen > 3 and forceumount:
            killprocess(res)
            os.popen("umount "+diskname)
        else :
            os.popen("umount "+diskname)

    #option -f kill all process use the diskname 
    #umount the disk 

#kill the app
def killprocess(res):
    reslen=len(res)
    for i in range(1,reslen):
        print res[i]


#auto start the appname when event happen
def autostart(diskname):
    #find  the the app already open or start a new instance with -n
    if os.path.exists(diskname):
        #print diskname
        open(diskname)

#autostart server
def autostartserver(timeseq,disknamelist):
    while True:
        for diskname in disknamelist:
            autostart(diskname)
        time.sleep(timeseq)

def open(diskname):
    psnaildiskapp=('Transmission.app',)
    if diskname == "/Volumes/psnail":
        for app in psnaildiskapp:
            res=os.popen("ps -ef | grep "+app).readlines()
            #why 2 :one is ps ,the other one is the diskutils.py
            if len(res) == 2 :      
                os.popen("open /Applications/"+app)
            #    print('start '+app)
            else :
                #print("it has start")
                pass
    elif diskname == "/Volumes/hello" :
        pass
    else :
        pass

if __name__ == "__main__":
    #option 
    #umountdisk(mydiskname)
    #timeseq=60*1
    #autostartserver(timeseq,mydiskname)
    parse=argparse.ArgumentParser("diskutils")
    parse.add_argument("-s","--start",action="store_true",help="start the autostartserver")
    parse.add_argument("-u","--umount",action="store_true",help="umount the disk ")
    parse.add_argument("-f","--forceumount",action="store_true",help="force to umount the disk")
    args=parse.parse_args()
    if args.start :
        timeseq=60*1
        autostartserver(timeseq,mydiskname)
    elif args.umount :
        umountdisk(mydiskname,False)
    elif args.forceumount :
        umountdisk(mydiskname,True)
