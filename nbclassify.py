import re
import math
import os
import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]

#inputPath = "/home/ankit/Desktop/csci544-hw1/spam.nb"  
#outputPath = "/home/ankit/Desktop/csci544-hw1/SPAM_dev/"

pos = ""
neg = ""
outfile = ""
f = open(inputPath,"r")
lines = f.readlines()

if "spam.nb" in f.name:
    pos = "HAM"
    neg = "SPAM"
    outfile = "/home/ankit/Desktop/csci544-hw1/spam.out" 
else :
    pos = "POS"
    neg = "NEG"
    outfile = "/home/ankit/Desktop/csci544-hw1/sentiment.out"
f.close()

posDict = {}
negDict = {}
spamC = 0.0
hamC = 0.0
for line in lines:
    if neg+"_PROP" in line:
        words = line.split(" ")
        spamC = float(words[1])
        #print("spamProb " + str(spamProb))
    elif pos+"_PROP" in line:
        words = line.split(" ")
        hamC = float(words[1])
        #print("hamProb " + str(hamProb))
    else:
        if pos+" " in line:
            str1 = re.sub("[\n]+","",line)
            words = str1.split(" ")
            posDict[words[1]] = float(words[2])  
        elif neg+" " in line:
            str1 = re.sub("[\n]+","",line)
            words = str1.split(" ")
            negDict[words[1]] = float(words[2])

hamProb = math.log(hamC/(hamC+spamC))
spamProb = math.log(spamC/(hamC+spamC))
spamCNew = spamC
hamCNew = hamC            

print("hamProb " + str(hamProb))
print("spamProb " + str(spamProb))
'''
count = 0
for key, value in negDict.items():
    print(key + " " + str(value))
    count = count + 1
'''

fileName = ""
spamProbability = 0.0
hamProbability = 0.0
posDictNew = {}
negDictNew = {}
posDictNewLen = 0.0
negDictNewLen = 0.0

for root, dirs, files in os.walk(outputPath, topdown=True):
    for file in files:
        f = open(outputPath + file,'rU',errors = 'ignore')
        lines = f.readlines()
        linetotal = ""
        for line in lines:
            linetotal = linetotal + re.sub("[\n]+"," ",line)
        
        lineSPR = re.sub('[\W_0-9]+',' ',linetotal) # remove special characters
        #lineSPR = linetotal
        lineWS = re.sub('[\s]+',' ',lineSPR)#remove multiple spaces by single
        str1 = re.sub("\s$","",lineWS)
        words = str1.split(" ")
        for word in words:
            if word not in posDict:
                if word not in posDictNew:
                    posDictNew[word] = 1.0
                else:
                    posDictNew[word] = posDictNew[word] + 1
                    
        for word in words:
            if word not in negDict:
                if word not in negDictNew:
                    negDictNew[word] = 1.0
                else :
                    negDictNew[word] = negDictNew[word] + 1                    
                    
posDictLen = float(len(posDict))
negDictLen = float(len(negDict))                    
posDictNewLen = float(len(posDictNew))
negDictNewLen = float(len(negDictNew))
posDictLenTotal = float(posDictNewLen + posDictLen)
negDictLenTotal = float(negDictNewLen + negDictLen)
print("posDictLen "+str(posDictLen))
print("posDictNewLen " + str(posDictNewLen))

fsp = open(outfile,"w")
for root, dirs, files in os.walk(outputPath, topdown=True):
    for file in files:
        
        f = open(outputPath + file,'rU',errors = 'ignore')
        
        lines = f.readlines()
        linetotal = ""
        for line in lines:
            linetotal = linetotal + re.sub("[\n]+"," ",line)
        
        lineSPR = re.sub('[\W_0-9]+',' ',linetotal) # remove special characters
        #lineSPR = linetotal
        lineWS = re.sub('[\s]+',' ',lineSPR)#remove multiple spaces by single
        str1 = re.sub("\s$","",lineWS)
        words = str1.split(" ")
        spamProbability = 0.0
        hamProbability = 0.0
        
        for word in words:
            if word in posDict:
                hamProbability = hamProbability + float(posDict[word])
            else :
                hamProbability = hamProbability + float(math.log(posDictNew[word]/posDictLenTotal))
        for word in words:
            if word in negDict:
                spamProbability = spamProbability + float(negDict[word])
            else :
                spamProbability = spamProbability + float(math.log(negDictNew[word]/negDictLenTotal))    
        
        if((spamProbability + spamProb) > (hamProbability + hamProb)):
            #print("SPAM")
            if pos in f.name:
                fileName = pos
            else :
                fileName = neg
            fsp.write(fileName + " " + neg +"\n")
        else:
            #print("HAM")
            if pos in f.name:
                fileName = pos
            else :
                fileName = neg
            fsp.write(fileName + " " + pos + "\n")
        
        
    f.close()        
fsp.close()

fsp = open(outfile,"r",errors = 'ignore')
lines = fsp.readlines()
fsp.close()
h=0
s=0
h1=0
s1=0
spamf =0
hamf = 0
for line in lines:
    words = line.split(" ")
    if  pos in words[1]:
        h1 = h1 + 1
    elif  neg in words[1]:
        s1 = s1 + 1
        
    if  pos in words[0]:
        hamf = hamf + 1
    elif  neg in words[0]:
        spamf = spamf + 1
    
    if pos in words[0] and pos in words[1]:
        h = h + 1
    elif neg in words[0] and neg in words[1]:
        s = s + 1
        
print(pos+" TOTAL :: " + str(h1))
print(neg+" TOTAL :: " + str(s1))
print(pos+" TRUE :: " + str(h))
print(neg+" TRUE :: " + str(s))
print("TOTAL "+ pos +" FILES :: " + str(hamf))
print("TOTAL "+ neg +" FILES :: " + str(spamf))
print("PRECISION " + pos +" :: " + str(float(h/h1)))
print("RECALL "+ pos +" :: " + str(float(h/hamf)))
print("PRECISION "+ neg +" :: " + str(float(s/s1)))
print("RECALL "+ neg +" :: " + str(float(s/spamf)))
        
        