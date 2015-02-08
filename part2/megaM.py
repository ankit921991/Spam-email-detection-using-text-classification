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
outfile = "megam.sentiment.test"
'''
for root, dirs, files in os.walk(inputPath, topdown=True):
    f = open (inputPath + files[0],'rU',errors = 'ignore')
    if "HAM" in f.name or "SPAM" in f.name:
        pos = "HAM"
        #pos = ""
        neg = "SPAM"
        outfile = "megaM_training.txt" 
        #outfile = "megaM_test.txt" 
    elif "POS" in f.name or "NEG" in f.name:
        pos = "POS"
        #pos = "1"
        neg = "NEG"
        outfile = "megaM_sent_training.txt"
        #outfile = "megaM_test.txt" 
    break
    f.close()'''



fout = open(outputPath + outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)    
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
        '''
        if pos in f.name:
            #head = pos + " "
            head = "1 "
        else:
            #head = neg + " "
            head = "0 "
        #print(head+"  ")'''    
        fileLines = f.readlines()
        str = ""
        for i in range (len(fileLines)):
            str = str + re.sub("[\n]+"," ",fileLines[i])
        str = str.lower()
        head = "0 "  
        lineSPR = str  
        #lineSPR = re.sub('[\W_]+','',str) # remove special characters
        lineSPR = re.sub('[^a-zA-Z\d\s]+','',str) # remove special characters
        #lineSPR = str         
        lineWS = re.sub('\s+',' ',lineSPR)#remove multiple spaces by single
        str1 = re.sub("\s$","",lineWS) #remove space at the end
        str1 = head + str1    
        str1 = str1 + "\n"    
        fout.write(str1)
    break
    f.close()
    fout.close()

    
