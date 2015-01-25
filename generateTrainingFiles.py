import os
import sys
import re

inputPath = sys.argv[1]
outputPath = sys.argv[2]

#inputPath = /home/ankit/Desktop/csci544-hw1/SPAM_training/
#outputPath = "/home/ankit/Desktop/csci544-hw1/"


# code to generate training files by replacing special characters by space

pos = ""
neg = ""
outfile = ""

for root, dirs, files in os.walk(inputPath, topdown=True):
    f = open (inputPath + files[0],'rU',errors = 'ignore')
    if "HAM" in f.name or "SPAM" in f.name:
        pos = "HAM"
        neg = "SPAM"
        outfile = "spam_training.txt" 
    elif "POS" in f.name or "NEG" in f.name:
        pos = "POS"
        neg = "NEG"
        outfile = "sentiment_training.txt"
    break
    f.close()
    


fout = open(outputPath + outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
        if pos in f.name:
            head = pos + " "
        else:
            head = neg + " "
        fileLines = f.readlines()
        str = ""
        for i in range (len(fileLines)):
            str = str + re.sub("[\n]+"," ",fileLines[i])
        str = str.lower()
        str = head + str    
        lineSPR = re.sub('[\W_0-9]+',' ',str) # remove special characters
        #lineSPR = str        
        lineWS = re.sub('\s+',' ',lineSPR)#remove multiple spaces by single
        str1 = re.sub("\s$","",lineWS) #remove space at the end
        str1 = str1 + "\n"
        fout.write(str1)
        f.close()
    fout.close()

    
