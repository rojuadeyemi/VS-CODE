import re

b =  re.findall(r"(\+)?(\d{3})?(\d)?(-|\s|\.)?(\d{3})(-|\s|\.)?(\d{4})(-|\s|\.)?(\d{4})"," My phone number is either +2349065551147 or 09086532044 or 090-8127-2345 090.6786-5678, 090 5677 4534") 

#print([''.join(i) for i in b])
gr = re.search(r"(\d+)(\w+)","3456") 

import os
os.chdir("/storage/emulated/0/Project")

with open("alice.txt") as file:
	text = file.read()

#b = re.search(r"Al(ice|tea)", text)
#b = re.findall(r"Alice", text)

b = re.sub(r"Alice", "Aderoju" ,text )
#print(b)