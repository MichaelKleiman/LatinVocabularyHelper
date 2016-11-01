'''
Created on Nov 1, 2016

I've had no formal Python, so the style might not be 'correct'

counts the number of "known words", and prints out the count

@author: Michael
'''
import os
import time
sav = os.path.join(os.path.dirname(__file__), 'save.txt')

saves = open(sav, "r")
x = 0
for i in range(0, 997):
    l = saves.readline()
    if '1' in l:
        x = x + 1
    
        
print(x)
time.sleep(100)