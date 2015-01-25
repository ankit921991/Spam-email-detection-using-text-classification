import re
import math
import os


f = open("/home/ankit/Desktop/csci544-hw1/spam.nb","r")
lines = f.readlines()
f.close()

hamDict = {}
spamDict = {}

for line in lines:
    if "SPAM_PROP" in line:
        words = line.split(" ")
        spamC = float(words[1])
        #print("spamProb " + str(spamProb))
    elif "HAM_PROP" in line:
        words = line.split(" ")
        hamC = float(words[1])
        #print("hamProb " + str(hamProb))
    else:
        if "HAM " in line:
            str1 = re.sub("[\n]+","",line)
            words = str1.split(" ")
            hamDict[words[1]] = float(words[2])  
        elif "SPAM " in line:
            str1 = re.sub("[\n]+","",line)
            words = str1.split(" ")
            spamDict[words[1]] = float(words[2])

hamProb = math.log(hamC/(hamC+spamC))
spamProb = math.log(spamC/(hamC+spamC))
spamCNew = spamC
hamCNew = hamC            

'''
count = 0
for key, value in spamDict.items():
    print(key + " " + str(value))
    count = count + 1
'''

fileName = ""
spamProbability = 0.0
hamProbability = 0.0
hamDictNew = {}
spamDictNew = {}
hamDictNewLen = 0.0
spamDictNewLen = 0.0





for root, dirs, files in os.walk("/home/ankit/Desktop/csci544-hw1/SPAM_dev/", topdown=True):
    for file in files:
        f = open("/home/ankit/Desktop/csci544-hw1/SPAM_dev/" + file,'rU',errors = 'ignore')
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
            if word not in hamDict:
                if word not in hamDictNew:
                    hamDictNew[word] = 1.0
                else :
                    hamDictNew[word] = hamDictNew[word] + 1
                    
        for word in words:
            if word not in spamDict:
                if word not in spamDictNew:
                    spamDictNew[word] = 1.0
                else :
                    spamDictNew[word] = spamDictNew[word] + 1                    
                    
hamDictLen = float(len(hamDict))
spamDictLen = float(len(spamDict))                    
hamDictNewLen = float(len(hamDictNew))
spamDictNewLen = float(len(spamDictNew))
hamDictLenTotal = float(hamDictNewLen + hamDictLen)
spamDictLenTotal = float(spamDictNewLen + spamDictLen)
fsp = open("/home/ankit/Desktop/csci544-hw1/spam.out","w")
for root, dirs, files in os.walk("/home/ankit/Desktop/csci544-hw1/SPAM_dev/", topdown=True):
    for file in files:
        f = open("/home/ankit/Desktop/csci544-hw1/SPAM_dev/" + file,'rU',errors = 'ignore')
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
            if word in hamDict:
                hamProbability = hamProbability + float(hamDict[word])
            else :
                hamProbability = hamProbability + float(math.log(hamDictNew[word]/hamDictLenTotal))
        for word in words:
            if word in spamDict:
                spamProbability = spamProbability + float(spamDict[word])
            else :
                spamProbability = spamProbability + float(math.log(spamDictNew[word]/spamDictLenTotal))    
        
        if((spamProbability + spamProb) > (hamProbability + hamProb)):
            #print("SPAM")
            if "HAM." in f.name:
                fileName = "HAM"
            else :
                fileName = "SPAM"
            fsp.write(fileName + " SPAM\n")
        else:
            #print("HAM")
            if "HAM." in f.name:
                fileName = "HAM"
            else :
                fileName = "SPAM"
            fsp.write(fileName + " HAM\n")
        
        
    f.close()        
fsp.close()

fsp = open("/home/ankit/Desktop/csci544-hw1/spam.out","r",errors = 'ignore')
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
    if  "HAM" in words[1]:
        h1 = h1 + 1
    elif  "SPAM" in words[1]:
        s1 = s1 + 1
        
    if  "HAM" in words[0]:
        hamf = hamf + 1
    elif  "SPAM" in words[0]:
        spamf = spamf + 1
    
    if "HAM" in words[0] and "HAM" in words[1]:
        h = h + 1
    elif "SPAM" in words[0] and "SPAM" in words[1]:
        s = s + 1
        
print("HAM TOTAL :: " + str(h1))
print("SPAM TOTAL :: " + str(s1))
print("HAM TRUE :: " + str(h))
print("SPAM TRUE :: " + str(s))
print("TOTAL HAM FILES :: " + str(hamf))
print("TOTAL SPAM FILES :: " + str(spamf))
print("PRECISION HAM :: " + str(float(h/h1)))
print("RECALL HAM :: " + str(float(h/hamf)))
print("PRECISION SPAM :: " + str(float(s/s1)))
print("RECALL SPAM :: " + str(float(s/spamf)))
        
        