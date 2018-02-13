pTitle = 'Weekly Roundup-No. '+wN+' ' + strDate
fTitle = strDate + '-Weekly-Roundup-No.-'+wN+'.md'

openingText = ['']
sectionNames = []
sectionText = []
sectionLinks = []
imageLink = r''
sectionContent = {}
for sTexts, sLinks, sName in sectionText, sectionLinks, sectionNames:
	sectionContainer = []
	for sText, sLink in sTexts, sLinks:
		sectionContainer.append([sText, sLink])
	sectionContent[sName] = sectionContainer
	
file = open(fTitle,”w”) 
file.write(“Hello World”) 

for key in sectionContent:
	sItems = sectionContent[key]
	for sItem in sItems:
		
		if key == sectionContent.keys()[0] and sItem == sItems[0]:
			
			file.write('###' + pTitle)
			file.write('')
			file.write(openingText)
			file.write('')
			file.write(r'![]('+imageLink+')')
			
		if sItem == sItem[0]:
			file.write('## ' + key)
			file.write('')
			file.write('* ['+sItem[0]+']('+sItem[1]+')')
		else:
			file.write('* ['+sItem[0]+']('+sItem[1]+')')
 
file.close() 
