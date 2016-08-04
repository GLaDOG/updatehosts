import urllib2
import platform
import hashlib

orig_file = 'hosts.orig'
hostsfile = 'hosts'
searchtext = '255.255.255.255'
hostaddr = '127.0.1.1'
hostsurl = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'

hostname = platform.node()
insert_line = hostaddr + '\t' + hostname + '\n'
try:
    response = urllib2.urlopen(hostsurl)
except urllib2.URLError, e:
    print e.reason
contents = response.read()
if not hashlib.md5(contents).hexdigest() == hashlib.md5(open(orig_file, 'rb').read()).hexdigest():
    insertloaction = contents.index(searchtext)
    contents = contents[:insertloaction] + insert_line + contents[insertloaction:]
    with open(hostsfile, 'w') as f:
        f.write(contents)
    print 'Done!'
    try:
        response = urllib2.urlopen(hostsurl)
    except urllib2.URLError,e:
        print e.reason
    contents = response.read()
    with open(orig_file, 'w') as f:
        f.write(contents)
    print 'Update!'
else:
    print 'No Need!'
