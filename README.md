detect-fake-ap-using-mac-id-filteration
=======================================

Final Yr. Project B Tech CSE . Detecting Fake Ap using Mac Id Filteration
 
 
 author rahil sharma
date 15/3/2013 @rs



Full Paper can be found here :  http://www.ijmra.us/2013ijesr_december.php


# usage python rsdetectfake.py mon0 VOLSBB authorized mac_id
where 
mon0----our monitor mode interface

volsbb----our wifi access point name

ALGO USED:::::
#here we find a access point started with same ssid but different mac address
#check if packet has Dot11beacon layer present
#extract ip ssid and mac address
#while giving command line inputs give original mac and ssid these will be used for comparing
#if ssids of both machines is same then only we compare their mac ids 


