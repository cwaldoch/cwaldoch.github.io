# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:34:25 2018

@author: Connor
"""
import datetime
import numpy as np

dateStart = datetime.datetime.strptime('20180127', '%Y%m%d')
dateNow = datetime.datetime.now()
dayDiff = dateNow - dateStart

weekNum = str(int(np.ceil(dayDiff.days/7)))


strDate = '2018-02-08'

pTitle = 'Weekly Roundup-No. '+weekNum+' ' + strDate
fTitle = strDate + '-Weekly-Roundup-No.-'+weekNum+'.md'

openingText = 'This is a story.'
sectionNames = ['things', 'stuff', 'other things', 'other stuff']
sectionText = [['1', '2'], ['1', '2', '2'], ['a', 'b', 'c'], ['r', 'b', 'f']]
sectionLinks = [['1', '2'], ['1', '2', '2'], ['a', 'b', 'c'], ['y', 'u', 't']]

sectionZip = list(zip(sectionText, sectionLinks, sectionNames))

imageLink = r'z.png'
sectionContent = {}
for sTexts, sLinks, sName in sectionZip:
    sectionContainer = []
    #
    sectionContentZip = list(zip(sTexts, sLinks))
    for sText, sLink in sectionContentZip:
        sectionContainer.append([sText, sLink])
        sectionContent[sName] = sectionContainer
	
file = open(fTitle,'w') 

for key in sectionContent:
    sItems = sectionContent[key]
    for sItem in sItems:
        #pdb.set_trace()
        if key == list(sectionContent.keys())[0] and sItem == sItems[0]:
        			
            file.write('### ' + pTitle)
            file.write('\n')
            file.write(openingText)
            file.write('\n')
            file.write(r'![]('+imageLink+')')
            file.write('\n')
			
        if sItem == sItems[0]:
            file.write('## ' + key)
            file.write('\n')
            file.write('* ['+sItem[0]+']('+sItem[1]+')')
            file.write('\n')
        else:
            file.write('* ['+sItem[0]+']('+sItem[1]+')')
            file.write('\n')
 
file.close() 
