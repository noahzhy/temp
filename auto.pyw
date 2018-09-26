import os
import sys

def auto_makefile():
    file_dir = os.getcwd()
    cppfiles=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.cc':
                cppfiles.append(file)
    return cppfiles

def auto_headfiles():
    headfiles = "all :"
    for value in allfiles:
        headfiles = headfiles + "\t"  + value[:-3]

    headfiles = headfiles + '\n'
    return headfiles

def auto_mainbody():
    mainbody = ""
    for value in allfiles:
        mainbody = mainbody + value[:-3] + ": " + value[:-3] + ".o" + '\n'
        mainbody = mainbody + "\t" + "g++ -o " + value[:-3] + " " + value[:-3] + ".o" + '\n'
        mainbody = mainbody + value[:-3] + ".o: " + value[:-3] + ".cc" + '\n'
        mainbody = mainbody + "\t" + "g++ -c " + value[:-3] + ".cc" + '\n'

    return mainbody

def auto_clean():
    clean = "clean:" + '\n'
    for value in allfiles:
        clean = clean + "\t" +  "rm  " + value[:-3] + '\n'

    clean = clean + "\t" + "rm  *.o"
    return clean

allfiles = auto_makefile()
for value in allfiles:
    print(value)
print("-------------READ-------------")
makefile = auto_headfiles() + auto_mainbody() + auto_clean()
print(makefile)

f = open("makefile", "w")
f.write(makefile)
f.close()

print("--------------OK--------------")
