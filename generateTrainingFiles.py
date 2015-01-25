import os
import sys
import re
path = "/home/ankit/Desktop/csci544-hw1/"
os.chdir(path)
fout = open("/home/ankit/Desktop/csci544-hw1/spam_training.txt","w")

# code to generate training files by replacing special characters by space
for root, dirs, files in os.walk("/home/ankit/Desktop/csci544-hw1/SPAM_training/", topdown=True):
    for file in files:
        f = open("/home/ankit/Desktop/csci544-hw1/SPAM_training/" + file,'rU',errors = 'ignore')
        if "HAM" in f.name:
            head = "HAM "
        else:
            head = "SPAM "
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

    
