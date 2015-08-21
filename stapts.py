#coding=utf-8
import os,sys,shutil

##path=sys.argv[1]
##dest=sys.argv[2]
path='D:\\calculator-test-full'
dest='D:\\share\\calculator.py'

file=open(path,encoding='utf-8')
ftw=open(dest,'w',encoding='utf-8') 
##ftw.write('import shutil\n') 
for line in file:
    if line!='\n':
        item=line.split(' : ')
        if item[3] == 'gtk_button_clicked':
            if item[-1][0]=='×':
                subst='*'
            elif item[-1][0]=='−':
                subst='-'
            elif item[-1][0]=='√':
                subst='root'
            else:
                subst=item[-1][0]
            ftw.write('click("frmCalculator-btnNumeric%s.png")\n'%subst)
        else:
            ftw.write('click("%s.png")\n'%item[3])           
file.close()
ftw.close()
