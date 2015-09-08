#coding=utf-8
import os,sys,shutil

##path=sys.argv[1]
##dest=sys.argv[2]
path='D:\\result'
dest='D:\\share\\vlc.py'

file=open(path,encoding='utf-8')
ftw=open(dest,'w',encoding='utf-8')
for line in file:
    if line!='\n':
        item=line.split()
        if item[6]== 'PlayButton::updateButtonIcons':
            ftw.write('click("%s.png")\n'%item[8])
        else:
            ftw.write('click("%s.png")\n'%item[6])
file.close()
ftw.close()
