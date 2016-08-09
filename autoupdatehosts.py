import urllib2
import hashlib
import platform
import shutil

class Hosts():
    hostOS = platform.system()
    hostsurl = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    
    def __init__(self):
        if self.hostOS == 'Windows':
            self.flag = False
            self.hostsBak = ''
            self.hostsOrig = ''
        elif self.hostOS == 'Linux':
            self.flag = True
            self.hostsBak = 'hosts.orig'
            self.hostsOrig = 'hosts'
            self.searchtext = '255.255.255.255'
            self.hostname = platform.node()
            self.hostaddr = '127.0.1.1'
            self.insertLine = self.hostaddr + '\t' + self.hostname + '\n'
        try:
            response = urllib2.urlopen(self.hostsurl)
        except urllib2.URLError, e:
            print e.reason
        self.contents = response.read()
    
    def updateHosts(self):
        with open(self.hostsBak, 'w') as f:
            f.write(self.contents)
        shutil.copy(self.hostsBak, self.hostsOrig)
        if self.flag:
            with open(self.hostsOrig, 'r+') as f:
                content = f.read()
                i = content.index(self.searchtext)
                content = content[:i] + self.insertLine + content[i:]
                f.seek(0)
                f.write(content)
                f.truncate()
        print 'Done'
    
    def checkHostsHash(self):
        if self.flag:
            whichHosts = self.hostsBak
        else:
            whichHosts = self.hostsOrig
        if hashlib.md5(self.contents).hexdigest() == hashlib.md5(open(whichHosts, 'rb').read()).hexdigest():
            return True
        else:
            return False
def auto():
    hostsinstance = Hosts()
    if not hostsinstance.checkHostsHash():
        hostsinstance.updateHosts()
    else:
        print 'No Need'