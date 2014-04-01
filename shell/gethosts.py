#func get the lastest hosts file 
#time 2014-3-14
#!/usr/bin/python 

import urllib2
import os
import shutil

hosts="/etc/hosts"
localinfo="""
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1   localhost
255.255.255.255 broadcasthost
::1             localhost 
fe80::1%lo0 localhost
"""

def getfile():
    url="http://smarthosts.googlecode.com/svn/trunk/hosts"
    file=urllib2.urlopen(url)
    return file

def writefile(file,hostsinfo):
    backup(file)
    with open(hosts,"w") as filehandle:
        #local info write 
        filehandle.write(localinfo)
        filehandle.write(os.linesep)
        for line in hostsinfo:
            filehandle.write(line.strip()+os.linesep)

def backup(file):
    shutil.copyfile(file,file+".bak")

if __name__ == "__main__":
    file=getfile()
    writefile(hosts,file)
