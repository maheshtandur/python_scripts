# This script find a string most occerence 

import sys
import os
import re
from collections import Counter

this_file =  os.path.realpath(__file__)
this_dir = os.path.join(os.path.dirname(this_file))
ip_file_name = os.path.join(this_dir, "ip_logs.txt")

ipv4_pattern = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

ip_list = []

def find_ip ():
    print ("Find a string occerene in a file")
    fr = open(ip_file_name, "r")
    for line in fr:
        if re.search('^[0-9]', line):
            for val in line.split(' '):
                if re.search(ipv4_pattern, val):
                    ip_list.append(val)
    
    print(f'Total Number of IP Address: ', len(ip_list))
    print ("List if IP Address extracted")
    print(ip_list)
    print("\n")

    ip_count = dict(Counter(ip_list))
    print(ip_count)

    found = 0
    found1 = 0
    found2 = 0
    found3 = 0
    rm_dup_list = list(dict.fromkeys(ip_list))
    print (rm_dup_list)
    for i in rm_dup_list:
        for j in ip_list:
            if i == j:
                found = found + 1
        print(i, " -- ", found)
        found = 0




def main():
   
    find_ip()


if __name__ == '__main__':
    sys.exit(main())
