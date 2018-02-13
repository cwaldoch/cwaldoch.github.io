# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 07:58:16 2018

@author: cwaldoch
"""
import pdb
wN = str(5)

strDate = '2018-02-08'

pTitle = 'Weekly Roundup-No. '+wN+' ' + strDate
fTitle = strDate + '-Weekly-Roundup-No.-'+wN+'.md'

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
