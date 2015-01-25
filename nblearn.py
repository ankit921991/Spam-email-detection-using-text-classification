import re
import math
ham = 0.0
hWordCount = 0.0
spam = 0.0
sWordCount = 0.0

f = open("/home/ankit/Desktop/csci544-hw1/spam_training.txt","r")
lines = f.readlines()
f.close()
# to calculte prio probabilities of SPAM and HAM class
for line1 in lines:
    line = re.sub("[\n+]","",line1)
    if "HAM " in line:
        ham = ham + 1
        hCount = (len(line.split(" "))-1)
        hWordCount = hWordCount + hCount 
    elif "SPAM " in line:
        spam = spam + 1
        sCount = (len(line.split(" "))-1)
        sWordCount = sWordCount + sCount 

pspam = spam/(spam + ham)
pham = ham/(ham + spam)
#print("HAM " + str(hWordCount))
#print("SPAM " + str(sWordCount))
#print(str(sWordCount + hWordCount))

# calculted prior probabilities for SPAM and HAM class

dictSpam = {}
dictHam = {}
for line in lines:
    lineWNL = re.sub("[\n+]","",line)
    if "SPAM " in lineWNL:
        words = lineWNL.split(" ")
        for word in words:
            #if dictSpam.has_key(word):
            if word in dictSpam :
                dictSpam[word] = dictSpam[word] + 1.0
            elif word != "SPAM":
                dictSpam[word] = 1
    else :
        words = lineWNL.split(" ")
        for word in words:
            #if dictHam.has_key(word):
            if word in dictHam:
                dictHam[word] = dictHam[word] + 1.0
            elif word != "HAM":
                dictHam[word] = 1.0

print("SPAM " + str(spam))
print("HAM " + str(ham))
f = open("/home/ankit/Desktop/csci544-hw1/spam.nb","w")
#f.write("SPAM_PROP " + str(math.log(sWordCount/(sWordCount + hWordCount))) + "\n")
#f.write("HAM_PROP " + str(math.log(hWordCount/(sWordCount + hWordCount))) + "\n")

f.write("SPAM_PROP " + str(spam) + "\n")
f.write("HAM_PROP " + str(ham) + "\n")

for key, value in dictHam.items():
    f.write("HAM " + key + " " + str(math.log(value/hWordCount)) + "\n")

for key, value in dictSpam.items():
    f.write("SPAM " + key + " " + str(math.log(value/sWordCount)) + "\n")
f.close()






