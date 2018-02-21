### America's Oil Imports

We are not utterly dependent on foreign oil. We particularly don't rely on foreign oil from nominally hostile countries. The former has been true both relatively recently and in the past, the latter has almost always been the case since the US began relying on petroleum to move and produce. The singular period in which oil from elsewhere was both truly critical to the US and not generally available was the 70s. This time was the product of an emerging global market with a limited set of suppliers and a concentration of demand. Since then, supply has diversified and OPEC's sway has dwindled. 

This is all not to say that oil hasn't occasionally been expensive (commonly experienced directly by most Americans "at the pump"), but access has been consistent and diverse enough for a long enough period of time that the last ~20 years of "foreign oil" grandstanding should have been considered political malpractice outside of relatively small pockets of time. Fossil fuel resource exploration and extraction also follows boom and bust cycles naturally as low prices tend to suppress investment in future supply, but that is certainly not the underpinning of the fear in American politics around oil. Rather, I believe this meme has its roots in those oil shocks of the 70s and the phenomenon of generational memory. But first, data.

## Data+Python
The EIA has a [nice database](https://www.eia.gov/dnav/pet/pet_move_impcus_a2_nus_ep00_im0_mbbl_m.htm) of U.S. petroleum imports stretching back to 1981, which begins to differentiate different import sources in 1993. There are many columns, with long, annoying names. Fortunately, they're also standardized so with a little Python string splitting action I can get the regional or country names I want. I threw in US Production too to make things more clear. 

```
import pandas as pd
import pdb
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('oil_imports.csv')

colList = list(df.columns)
colList2 = colList[3:]

actualNames = [x.split(' of ')[0].split(' from ')[1] for x in colList2]
   
columns = colList[:3]
columns.extend(actualNames)
colDict = dict(zip(colList, columns))

df.rename(columns = colDict, inplace=True)
df.fillna(0)

for x in df.columns:
    print(x)

sumCats = ['All Imports', 'US Production',
    'Non-OPEC Countries',
    'Persian Gulf Countries',
    'OPEC Countries']
    
df['dates'] = pd.to_datetime(df['Date'])
for x in df.columns:
    
    if x in sumCats:       
        plt.plot(df[x], label = x)
        
xTicks = list(range(0,len(df),30))        
xTickLabels = [df['Date'].values[x] for x in xTicks]       
        
plt.xticks(xTicks, xTickLabels, rotation=70)
plt.title(r'US Oil Info 1/1981-11/2017')
plt.ylabel('Thousands of Barrels')
plt.xlabel('Date')
plt.legend()
plt.tight_layout()
plt.show()
```

## Graphs

![Oil Graph #1](https://farm5.staticflickr.com/4610/40345677812_b411f07ce4_z.jpg)

Unfortunately, this doesn't go back far enough. In fact, it's somewhat tantalizing to end when it does for the OPEC vs. Non-OPEC comparison. We need to go further. An older and more useful EIA table can be [found here](https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0507). While there's no immediately clear way to download the data directly, if you graph it you'll be given an option to grab the results. 

![Oil Graph #2](https://farm5.staticflickr.com/4744/39680380834_777ff58c55_z.jpg)

I had to do a bit of interpolating daily barrels out to monthly values to fit the format I was doing (hence the steps), but overall, this graph is suddenly far more informative. Both times the US encountered an "energy crisis" real or somewhat invented (1970s vs 1990), OPEC had an outsized share of our imports.  One more note, this graph doesn't tell the whole story. The US has a large position in terms of the refining and production of various petroleum products, and not all oil is created equal, with various uses for different grades. Additionally, oil is a fungible, global commodity. All of that is to say that not all of the oil produced in and imported to the US is being consumed here.

## Generations and Memory

I have a theory that the ability for this thread to continually find its way into modern American politics is the result of the true oil shocks occurring when our current political class was in its formative years.To start, I need some ages. [This WSJ infographic](http://online.wsj.com/public/resources/documents/info-CONGRESS_AGES_1009.html) was useful to quickly pull the ages I was looking for.

In 2001, the average House age was ~55, and ~59 in the Senate. By 2011, legislators had aged up to 57 in the House, and 62 in the senate. For the first oil crisis in 1973, those 2001 legislators were on average in their mid 20s to early 20s, while the 2011 crop would have been in their late teens and mid 20s. While the pathways towards adult hood have become more disparate recently, personalities and opinions tend to cohere fairly early  in life. [Recent research has also indicated that those living under greater stress tend to move into adulthood earlier](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3792649/). Given the relative largess of many legislators and the lack of intergenerational economic movement in America it could be reasonable to surmise a slightly later identity coherence for our average legislator, pushing out the age of adulthood "acquisition". Taken together, it doesn't seem terribly risky to guess that these major political events shaped the positions of modern legislators well past middle age.









