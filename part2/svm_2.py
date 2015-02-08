import os
import sys
import re

inputPath = sys.argv[1]
outputPath = sys.argv[2]

pos = ""
neg = ""

#outfile = "spam.svm.test"
outfile = "sentiment.svm.test"

#outputPath_2 = outputPath + "svm.spam.model_2"
#outputPath_2 = outputPath + "svm.spam.model_2"

dictFeatures = {}
featureCount = 0

f = open ('svm.sentiment.model_2','rU',errors = 'ignore')
lines = f.readlines()
for line in lines:
    featureCount = featureCount + 1
    words = line.split(" ");
    if len(words)>0 :
        dictFeatures[words[0]] = int(words[1])     
f.close()
featureCount = featureCount + 1    
#dictFeatures = {}
dictValues = {}

fout = open(outputPath + outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
        lines = f.readlines()
        for line in lines:
            #str = str + re.sub("[\n]+"," ",fileLines[i])
            line = line.lower()
            #line = re.sub('[^a-zA-Z\s]+','',line)
            line = re.sub('[\s]+',' ',line)    
            line = re.sub("\s$","",line)
             # remove special characters
            #line = re.sub('[\W_0-9]+',' ',line)    
            words = line.split(" ")
            for word in words:
                if word not in dictFeatures:
                    #print(word + "->" + str(featureCount))
                    dictFeatures[word] = featureCount
                    featureCount = featureCount + 1
    f.close()
fout.close()


fout = open(outfile,"w")
for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
        
        lines = f.readlines()
        dictValues = {}
        for line in lines:
            #str = str + re.sub("[\n]+"," ",fileLines[i])
            line = line.lower()
            #line = re.sub('[^a-zA-Z\s]+','',line) # remove special characters
            line = re.sub('\s+',' ',line)    
            line = re.sub("\s$","",line)
            
            #line = re.sub('[\W_0-9]+',' ',line)    
            words = line.split(" ")
            for word in words:
                if dictFeatures[word] not in dictValues:
                    dictValues[dictFeatures[word]] = 1.0
                else:
                    dictValues[dictFeatures[word]] = dictValues[dictFeatures[word]] + 1.0
        
        
        fout.write("0")
        for key, value in sorted(dictValues.items()):
            fout.write(" "+str(key) +":"+ str(value))    
        fout.write("\n")
                    
    f.close()
fout.close()
    
