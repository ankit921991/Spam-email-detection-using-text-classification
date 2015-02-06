import os
import sys
import re

inputPath = sys.argv[1]
outputPath = sys.argv[2]

# code to generate training files by replacing special characters by space

pos = ""
neg = ""
#outfile = "final_sent_test.txt"

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
 
head = ""   
print(outputPath + outfile)
fout = open(outputPath + outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)    
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
        lineSPR = head + str    
        #lineSPR = re.sub('[^a-zA-Z\s]+','',str) # remove special characters    
        #lineSPR = str        
        lineWS = re.sub('\s+',' ',lineSPR)#remove multiple spaces by single
        str1 = re.sub("\s$","",lineWS) #remove space at the end
        str1 = str1 + "\n"
        fout.write(str1)
    break
    f.close()
    fout.close()

    
