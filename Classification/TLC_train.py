import math
import glob
import os
import json
import numpy
import re

docList = glob.glob(os.path.join('./training_data', '*.json'))
# docList = glob.glob(os.path.join('./testing_data', '*.json'))
vocab = []

def getWordList(doc):
    wordList = []
    with open(doc) as json_data:
        content = json.load(json_data, strict=False)
        for sentence in content["sentences"]:
            for words in sentence["tokens"]:
                word = words["originalText"]
                wordList.append(word)
    return wordList

# def createVocab():
#     for doc in docList:
#         wordList = getWordList(doc)
#         for word in wordList:
#             if word not in vocab:
#                 vocab.append(word)
#     sorted(vocab)

def createVocabFromFile():
    with open('vocabulary.txt') as inputfile:
        for line in inputfile:
            vocab.append(line)

def countDoc(word):
    numberOfWordjDoc = 0
    for doc in docList:
        wordList = getWordList(doc)
        if word in wordList:
            numberOfWordjDoc +=1
    return numberOfWordjDoc

def TF( word, wordList):
    return wordList.count(word)

# def TFvector(doc):
#     tfVector = []
#     wordList = getWordList(doc)
#     for word in vocab:
#         tfVector.append(TF(word, wordList))
#     return tfVector

def IDF(word):
    return math.log10(len(docList)*1.0/(countDoc(word)+1))

# def IDFvector():
#     idfVector = []
#     for word in vocab:
#         idfVector.append(IDF(word))
#     return idfVector

def savetocsvfile(IDFInput):
    numpy.savetxt("train.csv", IDFInput, fmt='%4.4f', delimiter=",")

def LTCdocVector():
    numOfDoc = len(docList)
    numOfVocab = len(vocab)
    ltc = numpy.zeros((numOfDoc,numOfVocab+1))
    pattern = re.compile("[\.\/training_data\/]+[5].*")
    # pattern = re.compile("[\.\/test_data\/]+[5].*")
    for i in range(len(docList)):
        wordList = getWordList(docList[i])
        temp1 = 0
        temp2 = 0
        temp3 = []
        for word in vocab:
            temp1 = math.log10(TF(word, wordList)+1.0)*IDF(word)
            temp2 += math.pow(temp1,2)
            temp3.append(temp1)
        temp4 = math.sqrt(temp2)
        for j in range(len(vocab)):
            ltc[i][j] = temp3[j]/temp4
        if pattern.match(docList[i]):
            ltc[i][numOfVocab] = 0
        else:
            ltc[i][numOfVocab] = 1
    return ltc

# def printTF():
#     for doc  in docList:
#         print (TFvector(doc))
#         print '\n'
#
# def printIDF():
#     print (IDFvector())
#
# def printLTC():
#     numpy.set_printoptions(threshold=numpy.nan, precision=3)
#     print (LTCdocVector())

createVocabFromFile()
savetocsvfile(LTCdocVector())
