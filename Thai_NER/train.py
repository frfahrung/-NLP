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

wordList = [word for line in open('./notag/tagged/POL1106.CUT', 'rb') for word in line.strip().split('|')]
classification = ['(org)', '(org_start)', '(org_cont)', '(org_end)', '(per)', '(per_start)', '(per_cont)', '(per_end)', '(loc)', '(loc_start)', '(loc_cont)', '(loc_end)']

def printOutput(temp):
    print ( " ".join([t for t in temp]) )

def checkdict(temp):
    temp[1] = '1' if temp[0] in prefixPerson else '0'
    temp[2] = '1' if temp[0] in prefixOrg else '0'
    temp[3] = '1' if temp[0] in suffixOrg else '0'
    temp[4] = '1' if temp[0] in OrgDict else '0'
    temp[5] = '1' if temp[0] in commonDict else '0'
    printOutput(temp)

def addClass(word, c):
    newstr = word
    status = False
    if c in word:
        status = True
        newstr = word.replace(c, "")
        if all( [c != '(loc)', c != '(loc_start)', c != '(loc_cont)', c != '(loc_end)'] ): temp[6] = c
        else: temp[6] = '(other)'
    else: temp[6] = '(other)'
    temp[0] = newstr
    return status

def checkClass(word, temp):
    status = False
    for c in classification:
        if status: break
        status = addClass(word, c)
    checkdict(temp)

for word in wordList:
    temp = ['','','','','','','']
    if word != '' and word != ' ':checkClass(word, temp)
