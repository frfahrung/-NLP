import math
import glob
import os
import json
import numpy
import re
import io

docList = glob.glob(os.path.join('./training_data', '*.json'))
# docList = glob.glob(os.path.join('./testing_data', '*.json'))
vocab = [line.rstrip() for line in open('./output/vocabulary.txt')]

def getWordList(doc):
    wordList = []
    with open(doc) as json_data:
        content = json.load(json_data, strict=False)
        for sentence in content["sentences"]:
            for words in sentence["tokens"]:
                word = words["originalText"]
                wordList.append(word)
    return wordList

def countDoc(word):
    numberOfWordjDoc = 0
    for doc in docList:
        wordList = getWordList(doc)
        if word in wordList:
            numberOfWordjDoc +=1
    return numberOfWordjDoc

def countDocVector():
    countDocList = []
    i=1
    for word in vocab:
        print(i)
        countDocList.append(countDoc(word))
        i+=1
    return countDocList

def IDF(numOfDoc,countDocOfWord):
    return math.log10(numOfDoc*1.0/(countDocOfWord+1))

def IDFvector():
    idfVector = []
    numOfDoc = len(docList)
    numOfVocab = len(vocab)
    countDocOfWord = countDocVector()
    for i in range(numOfVocab):
        idfVector.append(IDF(numOfDoc,countDocOfWord[i]))
    return idfVector

def outputText(idfVector):
    output_file = io.open('./output/idf_train.txt', 'w', encoding='utf8')
    # output_file = io.open('./output/idf_test.txt', 'w', encoding='utf8')
    for idf in idfVector:
        output_file.write(str(idf) + '\n')
    output_file.close()

outputText(IDFvector())
