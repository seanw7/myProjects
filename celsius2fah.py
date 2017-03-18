# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:19:48 2017

@author: SW
"""



def c_to_f(c):
    fah= c *9/5+32
    if fah < -273.15:
        print ("Below Absolute Zero: Impossible temp")
    print ("{} degrees celsius converts to {} degrees fahrenheit".format(c,fah))

def calcTemp():
    while True:
        inputTemp = int(input("Please input temperature in Celsius for conversion: "))
        c_to_f(inputTemp)

while True:
    print('Calculator Initialized')
    try:
        calcTemp()
    except ValueError:
        print('Error: Use Integers only please')
        continue


