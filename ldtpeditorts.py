#coding=utf-8
import os,sys,shutil

path=sys.argv[1]
dest=sys.argv[2]
##path='D:\\gcalc.py'
##dest='D:\\share\\gcalc.py'

reserve={'wait':'wait(%s)','click':'click("%s-%s.png")','waittillguiexist':'wait("%s.png",FOREVER)',
         'waittillguinotexist':'waitVanish("%s.png",FOREVER)'}

file=open(path)
ftw=open(dest,'w') 
ftw.write('import shutil\n') 
for line in file:
    if line!='\n':
        item=line.split()
        if item[0] in reserve:
            if item[0]=='wait':
                ftw.write(line.lstrip())
            elif item[0]=='click':
                ftw.write(reserve[item[0]]%(item[1].strip('(",'),item[2].strip('")'))+'\n')
            else:
                ftw.write(reserve[item[0]]%(item[1].strip('(",)'))+'\n')               
file.close()
ftw.close()

