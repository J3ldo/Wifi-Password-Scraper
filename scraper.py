import re
import subprocess

#will get all wifis on the machine
output = subprocess.getoutput("netsh wlan show profiles")
#fetches all the names
items = re.compile(r"All User Profile     : .*")

#finds all the names
matches = items.finditer(str(output))
all_wifis = []
for i in matches:
    #appends the names
    all_wifis.append(i.group()[23:])


allpasseslist = []
for i in all_wifis:
    #gets a pass from the wifi
    output2 = subprocess.getoutput(f"netsh wlan show profiles {i} key=clear")
    #finds the passwotd
    passes = re.compile(r"Key Content            : .*")
    allpasses = passes.finditer(str(output2))
    #appends the passwords into a dictionary and prints the name and password
    for passw in allpasses:
        print(f"{i}: {passw.group()[25:]}")
        allpasseslist.append({i : passw.group()[25:]})

#prints out the list of all passes
print(allpasseslist)
