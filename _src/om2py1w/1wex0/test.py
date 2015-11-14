#coding:utf-8
from sys import argv
 
script,filename=argv

print "Do you want to print the history note?"

target = open(filename,"a+")

y=raw_input("Y/N")

if y=="Y":
    print "Here's your file %r" % filename
    print "Here's your history note:"
    
    print target.read()   

print "Please input your note here:"
x=raw_input("> ")

#target.open(filename,"w")
target.write(x)

target.close()