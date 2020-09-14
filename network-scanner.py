import nmap
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup

ip = input("Enter IP :")

nm = nmap.PortScanner()
nm.scan(hosts=ip+"/24",arguments='-sn')

hosts_lists = []
mac_lists = []
mac_vendor_list = []

hosts_lists = nm.all_hosts()

for i in hosts_lists:
    mac = get_mac_address(interface='wlan0/eth0',ip=i)
    if mac != None:
        mac_lists.append(mac)
    else:
        continue

for i in mac_lists:
    result = MacLookup().lookup(i)
    mac_vendor_list.append(result)

for i in hosts_lists:
    print(i)
    
for i in mac_lists:
    print(i)   

for i in mac_vendor_list:
    print(i)
