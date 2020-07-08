# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:32:01 2020

@author: AsidTrip
"""
'''
Made this to click on cards for Balloon Monkey City Game on steam
all it does is click on the listed coordinates

'''


import time
import pyautogui as pag

print(pag.size())


'''
    clicker points
    950, 550      Box
    550, 440 card one
    805, 440 card two
    1060, 440 card three
    1315, 440 card four
    
'''


def click_function():
    
    
    for i in range(2000):
        pag.click(950, 550)
        time.sleep(2)
        

        pag.click(550,440)
        pag.click(805, 440)
        pag.click(1060, 440)
        pag.click(1315, 440)
        
        time.sleep(1)
        
        pag.click(550,440)
        pag.click(805, 440)
        pag.click(1060, 440)
        pag.click(1315, 440)
        
        time.sleep(2)
    
        if ((i % 15) == 0):
            pag.click(950,950)
            time.sleep(2)
                
    
    
#Main
    
click_function()

