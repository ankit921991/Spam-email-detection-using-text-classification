import os
import sys
import re

inputPath = sys.argv[1]
outputPath = sys.argv[2]

# code to generate training files by replacing special characters by space

pos = ""
neg = ""
outfile = "final_sent_test.txt"
#outfile = "final_spam_test.txt"

head = ""   
print(outputPath + outfile)
fout = open(outputPath + outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)    
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
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

    
