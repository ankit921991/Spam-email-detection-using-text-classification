import os
import sys
import re

inputPath = sys.argv[1]
outputPath = sys.argv[2]

pos = ""
neg = ""
#outfile = "svm.sentiment.test"
#outputPath_2 = outputPath + "svm.sentiment.model_2"
outputPath_2 = outputPath + "svm.spam.model_2"


for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)
    f = open (inputPath + files[0],'rU',errors = 'ignore')
    if "HAM" in f.name or "SPAM" in f.name:
        pos = "HAM"
        neg = "SPAM"
        #outfile = "spam_svm_test.txt"
        outfile = "spam.svm.training" 
    elif "POS" in f.name or "NEG" in f.name:
        pos = "POS"
        neg = "NEG"
        outfile = "sentiment.svm.training"
        
    break
    f.close()
    
dictFeatures = {}
dictValues = {}
featureCount = 1
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

fout = open(outputPath_2,"w")
for key, value in dictFeatures.items():
    fout.write(key +" "+ str(value)+"\n")
fout.close()

fout = open(outfile,"w")

for root, dirs, files in os.walk(inputPath, topdown=True):
    files = sorted(files)
    for file in files:
        f = open(inputPath + file,'rU',errors = 'ignore')
        if pos in f.name:
            head = "1"
        else:
            head = "-1"
        lines = f.readlines()
        
        dictValues = {}
        for line in lines:
            #str = str + re.sub("[\n]+"," ",fileLines[i])
            line = line.lower()
            line = re.sub('\s+',' ',line)    
            line = re.sub("\s$","",line)
            #line = re.sub('[^a-zA-Z\s]+','',line) # remove special characters
            #line = re.sub('[\W_0-9]+',' ',line)    
            words = line.split(" ")
            for word in words:
                if dictFeatures[word] not in dictValues:
                    dictValues[dictFeatures[word]] = 1.0
                else:
                    dictValues[dictFeatures[word]] = dictValues[dictFeatures[word]] + 1.0
        
        fout.write(head)
        #fout.write("0")
        for key, value in sorted(dictValues.items()):
            fout.write(" "+str(key) +":"+ str(value))    
        fout.write("\n")
                    
    f.close()
fout.close()
    
