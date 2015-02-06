import re
import math
import os
import sys

inputPath = sys.argv[1]  #input file path from command line
outputPath = sys.argv[2] #out file path command line
outfile = ""

# code to obtain output file name from the training file
f = open(inputPath,"r")
fileName = f.name
fileName = fileName.split(".")
outfile = fileName[0]+".out"
lines = f.readlines()
f.close()

#--------------------------------------------------------

classes = []
classLengthCount = {}
classWordCount = {}

#to retrieve meta attributes from file
firstLine = lines[0]
firstLine = re.sub("\n","",firstLine)
firstLine = re.sub(",$","",firstLine)
firstLine = firstLine.split(",")

#to retrieve vocabulary length from file
secondLine = lines[1]
secondLine = re.sub("\n","",secondLine)
secondLine = secondLine.split(" ")
totalVocabularyLength = float(secondLine[1])

#to populate class length and class words dictioonary
_dict = {"":{}}
for classLine in firstLine:
    line = classLine.split(" ")
    classes.append(line[0])
    _dict[line[0]] = {}
    classLengthCount[line[0]] = float(line[1])
    classWordCount[line[0]] = float(line[2])


#to populate words and probabilities in respective dictionaries
for line in lines:
    if lines[0] not in line and lines[1] not in line:
        str1 = re.sub("[\n]+","",line)
        words = str1.split(" ")
        _dict[words[0]][words[1]] = float(words[2]) 

fileName = ""
#fsp = open('OOOOP.txt',"w")
probabilityOfClass = {}

for w in classes:
    probabilityOfClass[w] = 0.0

#----------------------------------------------------------****
f = open(outputPath,'rU',errors = 'ignore')
lines = f.readlines()
linetotal = ""
#print("file " + f.name)
for lineSPR in lines:
    #linetotal = linetotal + re.sub("[\n]+"," ",line)
    
    #lineSPR = re.sub('[^a-zA-Z\s]+','',line) # remove special characters
    #lineSPR = linetotal
    lineWS = re.sub('[\s]+',' ',lineSPR)#remove multiple spaces by single
    str1 = re.sub("\s$","",lineWS)
    str1 = str1.lower()
    words = str1.split(" ")
    
    for _class in classes:
        probabilityOfClass[_class] = 0.0
        
    for _class in classes:
        for word in words:
            if word in _dict[_class]:
                probabilityOfClass[_class] = probabilityOfClass[_class] + float(_dict[_class][word])
            else :
                probabilityOfClass[_class] = probabilityOfClass[_class] + float(math.log(1/(classWordCount[_class]+totalVocabularyLength)))
    
    max = -99999999.99999
    result = ""
    
    for key, value in probabilityOfClass.items():
        if value > max:
            max = value
            result = key        
    
    fileName =  f.name
    fileName = fileName.split(".")
    fileN = fileName[0]
    #fsp.write(fileN + " " + result +"\n")
    print(result)
f.close()        
#fsp.close()      

  