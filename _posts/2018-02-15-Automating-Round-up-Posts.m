As I wrote last week's roundup post I realized there was no reason why I couldn't automate that process. It's easy enough to give python lists of items and have those lists be written to a text file in some particular order. There were a handful of issues as I prototyped the code, so let's walk through it!

"""
import datetime
import numpy as np

dateStart = datetime.datetime.strptime('20180127', '%Y%m%d')
dateNow = datetime.datetime.now()
dayDiff = dateNow - dateStart

weekNum = str(int(np.ceil(dayDiff.days/7)))
strDate = dateNow.strftime("%Y-%m-%d")
"""

First I'm importing datetime and numpy since I'm going to pull a bit from each of those libraries. The next 4 lines of code are devoted purely to generating the week number and the current date as a string for the post title. In order to figure out what the week number is I'm hardcoding the starting date, calling the current date, and then subtracting the start. This returns a datetime timedelta object with the time difference in various increments. This object, dayDiff, is conveinently very easy to use:
```
dayDiff.days
```
returns an integer of the day difference. From there, I'm dividing the number of days by 7 and rounding up (the numpy.ceil() function), the converting it to an int and a string. An int to drop the decimal, and a string so that it can be placed into the title text. I'm forcing the number of weeks to line up because i's conceivable I would want to post early some week when I know I won't be available on a Friday. Finally, I'm converting the datetime object for the current date into a string of the format that I use for the post title and also the filename as it appears on GitHub.

These next lines are fairly straight forward, I'm just generating the post title and filename using the variable I generated in the first 5 lines of code.
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
