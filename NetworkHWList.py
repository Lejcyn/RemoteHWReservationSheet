import os,re
f= os.popen('arp -a') 
data = f.read()

for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
  print(line)
  if line[1] == "01-00-5e-00-00-16":
    print(line[0]+"IP found")