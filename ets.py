#coding=utf-8
import os,sys,shutil

h=path[path.rindex('\\')+1:path.index('.')]
target=os.path.join(dest,h+'.sikuli')

if not os.path.isdir(target):
    os.makedirs(target)
source=os.path.join(path,'Images')
for file in os.listdir(source):
    if "png" in file:
        sfile=os.path.join(source,file)
        shutil.copy(sfile,target)

res={'DoubleClick':'doubleClick','Click':'click','TypeText':'type',
     'WaitFor':'wait','Return':'Key.ENTER','Escape':'Key.ESC','Tab':'Key.TAB'
    }

source=os.path.join(path,'Scripts')
name=os.listdir(source)[0]
newname=os.path.join(target,h+'.py')
file=open(os.path.join(source,name))
ftw=open(newname,'w') 
ftw.write('import shutil\n') 
file.seek(3)
for line in file:
    item=line.split()
    if item[0]=='TypeText':
        sep=item[1].split(',')
        for i in sep:
            b=res.get(i,i)
            ftw.write('%s(%s)\n'%(res[item[0]],b))
    elif item[0]=='WaitFor':
        sep=item[1].split(',')
        b=sep[1][:-1]+'.png\"'
        ftw.write('%s(%s,%s)\n'%(res[item[0]],b,sep[0]))
    else:
        b=item[1][:-1]+'.png\"'
        ftw.write('%s(%s)\n'%(res[item[0]],b))
file.close()
ftw.close()

