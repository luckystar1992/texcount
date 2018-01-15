#coding:utf-8

import os,sys

def readTex(fileName):
    curPath=os.path.dirname(fileName)
    lineArray=[]
    with open(fileName,'r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            if '\include' in line or '\input' in line:
                fileName=line.split("{")[1][0:-1]+".tex"
                lineArray.extend(readTex(os.path.join(curPath,fileName)))
            else:
                lineArray.append(line)
    return lineArray

def count(lineArray):
    count=0
    for line in lineArray:
        if not line.startswith("\\"):
            count+=len(line.split(" "))
    return count

def printHelp():
    print("-------Tex Count Toolkits-------")
    

if __name__ == '__main__':
    texFile=sys.argv[1]
    print count(readTex(texFile))
