#coding=utf-8
import os,sys,shutil

##path=sys.argv[1]
##dest=sys.argv[2]
path='D:\\libreoffice_systap.tap'
dest='D:\\share\\libreoffice.py'

dic={'0x81':['Insert','Fields','Date'],'0x82':['Insert','Fields','Time'],
     'clientClose':['clientClose','Cws']}

file=open(path,encoding='utf-8')
ftw=open(dest,'w',encoding='utf-8')
for line in file:
    if line!='\n':
        item=line.split()
        if item[6]== '_ZN9framework14MenuBarManager18GetMenuItemHandlerEt':
            for i in dic[item[-1].split('=')[-1]]:
                 ftw.write('click("%s.png")\n'%i)           
        else:
            for i in dic[item[6]]:
                 ftw.write('click("%s.png")\n'%i)  
file.close()
ftw.close()
