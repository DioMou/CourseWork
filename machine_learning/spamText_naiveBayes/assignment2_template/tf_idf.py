# tf_idf_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018
# Modified by Jaewook Yeom 02/02/2020
# Modified by Kiran Ramnath 02/13/2021

"""
This is the main entry point for the Extra Credit Part of this MP. You should only modify code
within this file for the Extra Credit Part -- the unrevised staff files will be used when your
code is evaluated, so be careful to not modify anything else.
"""

import numpy as np
import math
import collections
from collections import Counter, defaultdict
import time
import operator


def compute_tf_idf(train_set, train_labels, dev_set):
    """
    train_set - List of list of words corresponding with each mail
    example: suppose I had two mails 'like this city' and 'get rich quick' in my training set
    Then train_set := [['like','this','city'], ['get','rich','quick']]

    train_labels - List of labels corresponding with train_set
    example: Suppose I had two mails, first one was ham and second one was spam.
    Then train_labels := [1, 0]

    dev_set - List of list of words corresponding with each mail that we are testing on
              It follows the same format as train_set

    Return: A list containing words with the highest tf-idf value from the dev_set documents
            Returned list should have same size as dev_set (one word from each dev_set document)
    """



    # TODO: Write your code here
    trainCounter=collections.Counter()
        
    countDiff=collections.Counter()
    hamPosteriorDict={}
    spamPosteriorDict={}
    sumHam=0.0
    sumSpam=0.0
    resultLableList=[]
    for eachSetIndex in range(len(train_labels)):
        tempHamCount=collections.Counter()
        tempHamCount=tempHamCount+trainCounter
        trainCounter.update(train_set[eachSetIndex])
        newCountDiff=trainCounter-tempHamCount
        # if eachSetIndex==2:
        #     print(tempHamCount)
        #     print(trainCounter)
        #     print(newCountDiff)
        allOneCounter=collections.Counter()
        for eachEleInDiff in newCountDiff:
            allOneCounter.update({eachEleInDiff:1})
        #if eachSetIndex==2 or eachSetIndex ==1 or eachSetIndex ==0:
            #print(allOneCounter, 'this is 2')
        countDiff=countDiff+allOneCounter
        # if eachSetIndex==3:
        #     print(allOneCounter,'this is 3')
        #     print(countDiff)
    print(countDiff['is'])
    with open('tif.txt','w') as filehandle:
        for item in countDiff:
            filehandle.write('%s  ' % item)
            filehandle.write('%s\n' % countDiff[item])
    
    for eachSetIndex in range(len(dev_set)):
        devCounter=collections.Counter()
        devCounter.update(dev_set[eachSetIndex])
        pList=[]
        wordList=[]
        for eachWordInDevC in devCounter:
            wordList.append(eachWordInDevC)
            pList.append(devCounter[eachWordInDevC]*math.log(len(train_set)/(1+countDiff[eachWordInDevC]))/len(dev_set[eachSetIndex]))
        if eachSetIndex ==1:
            print(devCounter)
            print(len(train_set),countDiff['is'],len(dev_set[eachSetIndex]))
            print(pList)
        maxIdex=pList.index(max(pList))
        resultLableList.append(wordList[maxIdex])
    
    # return list of words (should return a list, not numpy array or similar)
    with open('resulEXC.txt','w') as filehandle:
        for item in resultLableList:
            filehandle.write(str(item))
    return resultLableList
    
