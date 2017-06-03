#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import io

prefixPerson = [line.rstrip() for line in open('./selectClue/PerClue/person_front.txt')]
suffixPerson = [line.rstrip() for line in open('./selectClue/PerClue/person_back.txt')]
# firstname = [line.rstrip() for line in open('./selectDict/for_person/firstname.txt')]
prefixOrg = [line.rstrip() for line in open('./selectClue/OrgClue/org_front.txt')]
suffixOrg = [line.rstrip() for line in open('./selectClue/OrgClue/org_back.txt')]

wordList = [word for line in open('./test/98JUL5_1.txt', 'rb') for word in line.split('|')]

def tagging(tag, wordIndex, length):
    print wordList[wordIndex]
    if wordIndex+1 < len(wordList):
        print (" ".join([wordList[wordIndex+index+1] for index in range(length-1)]))
    print tag

def findPerLength(wordIndex):
    if(wordList[wordIndex+1] == 'ฯ' or wordList[wordIndex+1] == ' '): return 4
    return 5

def findOrgLength(wordIndex):
    orglength = 1
    for i in range(8):
        if wordList[wordIndex+i] in suffixOrg:
            length = i
    return orglength

def findTag(wordIndex) :
    if wordList[wordIndex] in prefixPerson: return '(per)'
    elif wordList[wordIndex] in prefixOrg: return '(org)'
    return ''

wordIndex = 0
while wordIndex < len(wordList):
    tag = findTag(wordIndex)
    if tag == '(per)': length = findPerLength(wordIndex)
    elif tag == '(org)': length = findOrgLength(wordIndex)
    else : length = 1

    tagging(tag, wordIndex, length)
    wordIndex += length
