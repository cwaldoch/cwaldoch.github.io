### Automating Markdown Posts with Python

As I wrote last week's roundup post I realized there was no reason why I couldn't automate that process. It's easy enough to give python lists of items and have those lists be written to a text file in some particular order. There were a handful of issues as I prototyped the code, so let's walk through it!

```
import datetime
import numpy as np

dateStart = datetime.datetime.strptime('20180127', '%Y%m%d')
dateNow = datetime.datetime.now()
dayDiff = dateNow - dateStart

weekNum = str(int(np.ceil(dayDiff.days/7)))
strDate = dateNow.strftime("%Y-%m-%d")
imageLink = r'z.png'
```

First I'm importing datetime and numpy since I'm going to pull a bit from each of those libraries. The next 4 lines of code are devoted purely to generating the week number and the current date as a string for the post title. In order to figure out what the week number is I'm hardcoding the starting date, calling the current date, and then subtracting the start. This returns a datetime timedelta object with the time difference in various increments. This object, dayDiff, is conveinently very easy to use:
```
dayDiff.days
```
returns an integer of the day difference. From there, I'm dividing the number of days by 7 and rounding up (the numpy.ceil() function), the converting it to an int and a string. An int to drop the decimal, and a string so that it can be placed into the title text. I'm forcing the number of weeks to line up because i's conceivable I would want to post early some week when I know I won't be available on a Friday. Finally, I'm converting the datetime object for the current date into a string of the format that I use for the post title and also the filename as it appears on GitHub. I also include a link to some image which I will include near the top of the post.

These next lines are fairly straight forward, I'm just generating the post title and filename using the variable I generated in the first 8 lines of code.
```
pTitle = 'Weekly Roundup-No. '+weekNum+' ' + strDate
fTitle = strDate + '-Weekly-Roundup-No.-'+weekNum+'.md'
```

Now I'm going to create receptacle for the #content

```
openingText = 'This is a story.'
sectionNames = ['things', 'stuff', 'other things', 'other stuff']
sectionText = [['1', '2'], ['1', '2', '2'], ['a', 'b', 'c'], ['r', 'b', 'f']]
sectionLinks = [['1', '2'], ['1', '2', '2'], ['a', 'b', 'c'], ['y', 'u', 't']]
```
These are not the best. I think a good step would be to just pull from some other file I write to, but for now I'm going to copy and past links and text directly into lists in my code. The opening text goes right below a post title, the rest should be pretty self explanatory. The major pitfall of this organizational technique is making sure the section text and links line up. 

Next up I'm zipping everything together to make the upcoming loops more amenable.
```
sectionZip = list(zip(sectionText, sectionLinks, sectionNames))
```
post-zipping this looks like:
```
[(['1', '2'], ['1', '2'], 'things'),
(['1', '2', '2'], ['1', '2', '2'], 'stuff'),
(['a', 'b', 'c'], ['a', 'b', 'c'],
'other things'), (['r', 'b', 'f'],
['y', 'u', ''], 'other stuff')]
```

The next bit of code creates a dictionary that will allow me to build the looping structure for writing the post. Dictionaries are great. You get to have an arbitrary "key" that then refers to an object or set of objects. This allows you to name variables with other variables in a loop where you don't always know what the variable names will be until you're in the loop.

```
sectionContent = {}
for sTexts, sLinks, sName in sectionZip:
    sectionContainer = []
    #
    sectionContentZip = list(zip(sTexts, sLinks))
    for sText, sLink in sectionContentZip:
        sectionContainer.append([sText, sLink])
        sectionContent[sName] = sectionContainer
```

First, I initiate an empty dictionary. Second I start the loop by pulling a text, link, and name object from the sectionZip. For the first of these in this example, sTexts = ['1','2'], sLinks = ['1', '2'], and sName = 'things'. Then I'm creating an empty sectionContainer, which will contain the relevant section material. I also zip the section content together. Finally, I loop through the elements of that section, assign them to the list, and then assign that list to the sectionContent dictionary with the section name as the key. This is probably not the efficient way to do any of this, but it's functional, and I mostly wrote it on the train to work, so I feel pretty ok.

Next up, the meat of this code, the actual post generation.

```
file = open(fTitle,'w') 

for key in sectionContent:
    sItems = sectionContent[key]
    for sItem in sItems:
        if key == list(sectionContent.keys())[0] and sItem == sItems[0]:
        			
            file.write('### ' + pTitle)
            file.write('\n')
            file.write(openingText)
            file.write('\n')
            file.write(r'![]('+imageLink+')')
            file.write('\n')
            
        if len(sItem[1]) > 0:			
            if sItem == sItems[0]:
                file.write('## ' + key)
                file.write('\n')
                file.write('* ['+sItem[0]+']('+sItem[1]+')')
                file.write('\n')
            else:
                file.write('* ['+sItem[0]+']('+sItem[1]+')')
                file.write('\n')
        else:
            if sItem == sItems[0]:
                file.write('## ' + key)
                file.write('\n')
                file.write('* '+sItem[0])
                file.write('\n')
            else:
                file.write('* '+sItem[0])
                file.write('\n')
 
file.close() 
```

While this is the longest chunk of code here it's really pretty straightforward. It iterates over every key in the sectionContent dictionary, pulls out the content and writes it to a .md file (markdown). The '\n' strings I insert are line breaks. The  if/else around the length of sItem[1] is for section texts that don't have links. If there's no links that content will be an empty '' value, so a length that's not greater than 0. The result of this test post [looks like this](http://connorwaldoch.com/blog/2000/01/01/example-auto-post).

I set all of this up so that I can drop links into a script, hit run, have the output get put in the correct folder, sync via git and have the post show up without me editing directly on my phone.
