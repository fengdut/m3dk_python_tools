#! /usr/bin/env python
import os
from sys import argv
if len(argv) < 2:
	print ('wxy file mush be supplied')
	print ('updategfp.py  wxy.xxx')
	exit()

wxyfile=argv[1]
if(os.path.exists('EP.info')==False):
        print ('can not find EP.info')
        exit()

EPfile=open('EP.info','r')
line1=EPfile.readline()

pmaxs=line1.split()

pmax=float(pmaxs[1])
print ('pmax:',pmax)
line1=EPfile.readline()
ppas=line1.split()
ppa=float(ppas[1])
print ('ppa:',ppa)
line1=EPfile.readline()
ppes=line1.split()
ppe=float(ppes[1])
print ('ppe:',ppe)
EPfile.close()





wxyin=wxyfile


import f90nml
wxy=f90nml.read(wxyin)
pampl=wxy['chpar']['pampl']
wxynow=f90nml.read('wxy')
oldgfp=wxynow['WDAT']['gfp']

print('pampl:',pampl)
print('old gfp:',oldgfp)
newgfp=oldgfp * pampl/(0.5*(ppa+ppe)/pmax)


print (newgfp)
wxy['wdat']['gfp']=newgfp


from m3dk import write_wxy
write_wxy(wxy,wxyfile)



