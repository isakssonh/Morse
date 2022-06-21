# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:27:26 2021

@author: hans.isaksson
"""

import winsound
import time
#import numpy as np

short=400 #ms
long=1200 #ms
letterpause = 1 #sec

winsound.Beep(440,1000) #Alert, start listening.
time.sleep(letterpause)

A=[short, long]
B=[long,short,short,short]
E=[short]
F=[short,short,long,short]
H=[short,short,short,short]
J=[short,long,long,long]
M=[long,long]
N=[long, short]
O=[long,long,long]
S=[short,short,short]
Y=[long,short,long,long]
two=[short,short, long, long, long]

frequency = 1046  # Set Frequency To x Hertz (880 Hz is an A)
duration = 100  # Set Duration To 1000 ms == 1 second

#def morsebeep(frequency, duration):
#    winsound.Beep(frequency, duration)

word='SOS'

#for j in range(0, len(word)): 
#    letter=word[j]


def morse(letter, frequency, letterpause):
    for k in letter:
        winsound.Beep(frequency,k)
    time.sleep(letterpause)

#morse(two, frequency, letterpause)
#morse(M, frequency, letterpause)
# morse(S, frequency, letterpause)
      
morse(B, frequency, letterpause)
morse(Y, frequency, letterpause)
morse(E, frequency, letterpause)
#morse(A, frequency, letterpause)

#len=len(word)

#for j in np.arange(0,len-1):
#    morse(word[j], frequency, letterpause)
#for j in word:
#    print(j)