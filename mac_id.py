#!/usr/bin/env python

#author rahil sharma 
# usage python rsdetectfake.py mon0 VOLSBB authorized mac_id
#here we find a access point started with same ssid but different mac address
#check if packet has Dot11beacon layer present
#extract ip ssid and mac address
#while giving command line inputs give original mac and ssid these will be used for comparing
#if ssids of both machines is same then only we compare their mac ids 
#if match not found then it is a fake access point 
#display it
import sys, os, signal 
from scapy.all import *

interface = sys.argv[1]   
ssid = "'"+sys.argv[2]+"'"
mac = sys.argv[3]

def monitorSSID(p):      
     if p.haslayer(Dot11Beacon):        
          pssid = p.sprintf("%Dot11Elt.info%")
          pmac = p.sprintf("%Dot11.addr2%")
          if(ssid == pssid):  			
               if not (pmac==mac):
                    print "FAKE AP found -> "+pmac      



sniff(iface=interface,prn=monitorSSID)

