#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import io
import glob

prefixPerson = [line.rstrip() for line in open('./selectClue/per_front.txt')]
prefixOrg = [line.rstrip() for line in open('./selectClue/org_front.txt')]
suffixOrg = [line.rstrip() for line in open('./selectClue/org_back.txt')]
OrgDict = [line.rstrip() for line in open('./selectDict/all_org.txt')]
commonDict = [line.rstrip() for line in open('./selectDict/common.txt')]

wordList = [word for line in open('./notag/POL1106.CUT', 'rb') for word in line.strip().split('|')]

def printOutput(temp):
    print ( " ".join([t for t in temp]) )

def checkdict(temp, word):
    temp[0] = word
    temp[1] = '1' if temp[0] in prefixPerson else '0'
    temp[2] = '1' if temp[0] in prefixOrg else '0'
    temp[3] = '1' if temp[0] in suffixOrg else '0'
    temp[4] = '1' if temp[0] in OrgDict else '0'
    temp[5] = '1' if temp[0] in commonDict else '0'
    printOutput(temp)\

for word in wordList:
    temp = ['','','','','','']
    if word != '' and word != ' ':checkdict(temp, word)
