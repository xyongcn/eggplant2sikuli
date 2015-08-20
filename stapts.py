#coding=utf-8
import os,sys,shutil

##path=sys.argv[1]
##dest=sys.argv[2]
path='D:\\calculator_result.result'
dest='D:\\share\\calculator.py'

file=open(path)
ftw=open(dest,'w') 
ftw.write('import shutil\n') 
for line in file:
    if line!='\n':
        item=line.split(' : ')
        if item[3] == 'math_equation_insert_digit':
            ftw.write('click("frmCalculator-btnNumeric%s.png")\n'%item[-1][-2])        else:
            ftw.write('click("%s.png")\n'%item[3])           
file.close()
ftw.close()
