#!/usr/bin/env python3

#Author: Brian Bode
# This program can take any text file, extract any ipv4 addresses found,
# and run GeoIP and RDAP checks


from __future__ import print_function
from __future__ import absolute_import

__code_desc__ = "logTrace"
__code_version__ = 'v1'
__code_debug__ = False

## Standard Libraries
import os
import sys
import argparse
import socket
import json
import requests
from pprint import pformat, pprint

## Third Party libraries
import re
from ipwhois import IPWhois
## Modules

def logParse(fstring):

	

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
	traceRDAP(ips)

def geoLoc(ip):
	geoIP='http://api.ipstack.com/{0}?access_key=5dcc2ad37796ca17aa947108974459c2'
	print ('GeoIP:')
	try:
		# print (geoIP.format(ip))
		res = requests.get(geoIP.format(ip))
		# print(res.status_code)
		if res.status_code == 404:
			return None
		data = res.json()
		print('City: ' + data["city"] + '| Region: ' + data["region_name"] +'| Country: '+ data["country_name"])
		
		
		return
	except:
		print ('Unable to resolve Geolocation. It is recommended to check the source and be sure this is actually an IP address.')
	return

def traceRDAP(ips):
	
	for i in ips:
		print ('-------------- Detailed information by for:' + i[0] + '------------')
		geoLoc(i[0])
		try:
			obj = IPWhois(i[0])
			res=obj.lookup()
			pprint(res)
		except:
			print ('unable to resolve RDAP, It is recommended to check the source and be sure this is actually an IP address.')
		print ('--------------------------------------------------------------')
def main():
	parser = argparse.ArgumentParser(description=__code_desc__)
	parser.add_argument('-V', '--version', action='version', version=__code_version__)
	parser.add_argument('-f', '--file', required=True)
	args = parser.parse_args()
	file_name = args.file
	with open(file_name) as fh:
		fstring = fh.readlines()
	logParse(fstring)
	pass

if __name__=="__main__":
	main()
