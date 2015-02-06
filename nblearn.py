import re
import math
import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]

classes = []  # to store all possible classes ex: HAm SPAm etc

#to get the name of .nb file from the training file name
f = open(inputPath,"r")
trainingFileName = f.name
words = trainingFileName.split("_")
outfile = words[0]+".nb"
lines = f.readlines()
f.close()
#-------------------------------------------------------

#To get the names of all possible classes
for line1 in lines:
    line = re.sub("[\n+]","",line1)
    words = line.split(" ")
    if words[0] not in classes:
        classes.append(words[0]) 
#-------------------------------------------------------

classesLength = {}  # to store number of records for each class   
classWordCount = {}  # to store word counts for each class
totalclassCount = len(lines) # total number of records or lines
totalCountDict = {}
totalVocabularyLength = 0.0

#to get vocabulary
for line1 in lines:
    line = re.sub("[\n+]","",line1)
    line = re.sub("[\s+]"," ",line)
    line = re.sub("\s$","",line)
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word not in words[0]:
            if word not in totalCountDict:
                #print(word + " ")
                totalCountDict[word] = 1.0
                
totalVocabularyLength = len(totalCountDict)

#To get classesLength,classWordCount values
for line1 in lines:
    line = re.sub("[\n+]"," ",line1)
    line = re.sub("[\s+]"," ",line)
    line = re.sub("\s$","",line)
    words = line.split(" ")
    if words[0] not in classesLength:
        classesLength[words[0]] = 1.0
        classWCount = float(len(words)-1)
        classWordCount[words[0]] = classWCount
    else:
        classesLength[words[0]] = classesLength[words[0]] + 1.0
        classWCount = float(len(words)-1)
        classWordCount[words[0]] = classWordCount[words[0]] + classWCount
#---------------------------------------------

probabilityOfClass = {} # to store probability of individual classes
for word in classes:
    probabilityOfClass[word] =  (classesLength[word]/totalclassCount)

_dict = {"":{}} #to store words counts and word for each classes

for word in classes:
    #print(word + " -> " + str(probabilityOfClass[word]))
    _dict[word] = {} 

# to populate _dict
for line in lines:
    lineWNL = re.sub("[\n+]","",line)
    for _class in classes:    
        if _class+" " in lineWNL:
            words = lineWNL.split(" ")
            for word in words :
                if word in _dict[_class] and word not in classes:
                    word = word.lower()
                    _dict[_class][word] = _dict[_class][word] + 1.0
                elif word != _dict[_class] and word not in classes:
                    word = word.lower()
                    _dict[_class][word] = 2.0
        
#----------------------------------------------------

f = open(outputPath,"w")

for w in classes:
    str1 = w+" "+str(classesLength[w])+" "+str(classWordCount[w])+","
    f.write(str1)
f.write("\n")
f.write("totalVocabularyLength " + str(totalVocabularyLength))
f.write("\n")


for _class in classes:
    for key, value in _dict[_class].items():
        f.write(_class+ " " + key + " " + str(math.log(value/(classWordCount[_class]+totalVocabularyLength))) + "\n")
f.close()

#------------------------------------------------------






