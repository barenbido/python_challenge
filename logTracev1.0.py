#!/usr/bin/env python3
"""
    This program can take any text file, extract any ipv4 addresses found,
    and run GeoIP and RDAP checks
    Author: Brian Bode
    Version: 1.0
"""

from __future__ import print_function
from __future__ import absolute_import

__code_desc__ = "logTrace"
__code_version__ = 'v1'
__code_debug__ = False

## Standard Libraries
import re
import logging
import argparse
import ipaddress
from pprint import pprint,pformat
from urllib.error import HTTPError
from urllib.parse import urljoin

## Third Party libraries
import requests
from ipwhois import IPWhois

## Modules

def logParse(fstring):
    """ Given a string, extract IP addresses using re """

    lst = []
    rx = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    # Extract IPv4 addresses by regex
    for line in fstring:
        res = rx.findall(line)
        if res is not None:
            for r in res:
                lst.append(str(r))

    # Dedup
    lst = list(set(lst))

    #Sort and clear null value
    lst.sort()
    ips = list(filter(None, lst))

    ## final output
    return ips

def geoLoc(ip):
    """ from an IP, call api.ipstack to get geolocation data """
    try:
        ipObject = ipaddress.ip_address(ip)
        if ipObject.is_private is not True:
            try:
                base_url = 'http://api.ipstack.com/'
                url = urljoin(base_url, ip)
                params = { "access_key": "5dcc2ad37796ca17aa947108974459c2" }
                res = requests.get(url=url, params=params)
                data = res.json()
                #s = 'City: %s | Region' + data["city"] + '| Region: ' + data["region_name"] +'| Country: '+ data["country_name"])
                #print('City: ' + data["city"] + '| Region: ' + data["region_name"] +'| Country: '+ data["country_name"])
                return data
            except HTTPError as e:
                msg = "Caught HTTPError %s when calling requests for url: %s" % (e.code, url)
                logging.warning(msg)
                return None
    except ValueError:
        msg = "%s is not a valid IP address" % ip
        logging.warning(msg)
        return None

def traceRDAP(ip):
    """ from an IP, get rdap info from whois """
    try:
        ipObject = ipaddress.ip_address(ip)
        if ipObject.is_private is not True:
            try:
                obj = IPWhois(ip)
                res = obj.lookup_whois()
                return res
            except Exception as e:
                msg = 'unable to resolve RDAP, It is recommended to check the source and be sure this is actually an IP address.'
                logging.warning(msg)
                logging.warning(pformat(e))
                return None
    except ValueError:
        msg = "%s is not a valid IP address" % ip
        logging.warning(msg)
        return None

def main():
    # Configure logging
    logging.basicConfig(filename=__name__, level=logging.INFO)

    # Handle arguments
    parser = argparse.ArgumentParser(description=__code_desc__)
    parser.add_argument('-V', '--version', action='version', version=__code_version__)
    parser.add_argument('-f', '--file', required=True)
    args = parser.parse_args()

    # Slurp file into RAM
    with open(file=args.file, encoding="utf-8") as fh:
        fstring = fh.readlines()

    # Extract artifacts
    ips = logParse(fstring)
    for ip in ips:
        print("Found IP: %s" % ip)
        geoip = geoLoc(ip)
        rdap = traceRDAP(ip)
        if geoip:
            print('GeoIP:')
            pprint(geoip)
        if rdap:
            print('RDAP:')
            pprint(rdap)

if __name__=="__main__":
    main()
