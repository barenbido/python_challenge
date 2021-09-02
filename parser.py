
#!/usr/bin/python

import re
#regex library

# opening and reading the file
with open(input('Enter file location:')) as fh:
 fstring = fh.readlines()
 
 
#declare regex for ip address r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
rx =re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lst = []
## Extract IPv4 addresses by regex
for line in fstring:
	if (rx.findall(line) != None):
		lst.append(rx.findall(line))
		
#Deduplicate
ips = []
for i in lst:
    if i not in ips:
        ips.append(i)

#Sort and clear null value
ips.sort()
ips = list(filter(None,ips))

## final output
print ('-------------- IP Addresses found in file -----------')
for i in ips:
        print ('[+]: ' + str(i[0]))    
print ('-----------------------------------------------------')
