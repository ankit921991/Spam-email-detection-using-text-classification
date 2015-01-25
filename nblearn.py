import re
import math
import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]

#inputPath = "/home/ankit/Desktop/csci544-hw1/spam_training.txt"  
#outputPath = "/home/ankit/Desktop/csci544-hw1/"

posC = 0.0
pWordCount = 0.0
negC = 0.0
nWordCount = 0.0

f = open(inputPath,"r")
lines = f.readlines()

if "spam_training" in f.name:
    pos = "HAM"
    neg = "SPAM"
    outfile = "spam.nb" 
else :
    pos = "POS"
    neg = "NEG"
    outfile = "sentiment.nb"
f.close()
# to calculte prio probabilities of SPAM and HAM class
for line1 in lines:
    line = re.sub("[\n+]","",line1)
    if pos+" " in line:
        posC = posC + 1
        hCount = (len(line.split(" "))-1)
        pWordCount = pWordCount + hCount 
    elif neg+" " in line:
        negC = negC + 1
        sCount = (len(line.split(" "))-1)
        nWordCount = nWordCount + sCount 

pspam = negC/(negC + posC)
pham = posC/(posC + negC)
#print("HAM " + str(pWordCount))
#print("SPAM " + str(nWordCount))
#print(str(nWordCount + pWordCount))

# calculted prior probabilities for SPAM and HAM class

dictNeg = {}
dictPos = {}
for line in lines:
    lineWNL = re.sub("[\n+]","",line)
    if neg+" " in lineWNL:
        words = lineWNL.split(" ")
        for word in words:
            #if dictNeg.has_key(word):
            if word in dictNeg :
                dictNeg[word] = dictNeg[word] + 1.0
            elif word != neg:
                dictNeg[word] = 1
    else :
        words = lineWNL.split(" ")
        for word in words:
            #if dictPos.has_key(word):
            if word in dictPos:
                dictPos[word] = dictPos[word] + 1.0
            elif word != pos:
                dictPos[word] = 1.0

print(neg + " " + str(negC))
print(pos + " " + str(posC))
f = open(outputPath + outfile,"w")
#f.write("SPAM_PROP " + str(math.log(nWordCount/(nWordCount + pWordCount))) + "\n")
#f.write("HAM_PROP " + str(math.log(pWordCount/(nWordCount + pWordCount))) + "\n")

f.write(neg + "_PROP " + str(negC) + "\n")
f.write(pos + "_PROP " + str(posC) + "\n")

for key, value in dictPos.items():
    f.write(pos+ " " + key + " " + str(math.log(value/pWordCount)) + "\n")

for key, value in dictNeg.items():
    f.write(neg + " " + key + " " + str(math.log(value/nWordCount)) + "\n")
f.close()






