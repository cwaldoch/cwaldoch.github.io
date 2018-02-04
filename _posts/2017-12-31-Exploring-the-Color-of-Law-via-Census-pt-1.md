# Exploring The Color of Law via the Census, pt. 1

## What is this?
I’ve been reading far more non-fiction recently than I have in any period since I finished college/grad school. I think the impetus for this shift has been my general dismay at the current administration and elements in American society whose relevance I was shamefully ignorant of. In order to better understand the current social-political cycle we’re in, as well as past arcs and their under-girding in long-term economic/social/demographic/whatever trends. It occurred to me that I could add my own personal homework to the writing that captivates (or shames) me most. In pursuit of that, I’m going to try and take a concept or *something* out of each book I read this year and explore it with Python+data. I don’t necessarily go in with a specific goal here, just exploration of a concept or an argument presented in something I’m currently reading or have finished. Here’s this post’s Github repo.

## The Color of Law
Recently I’ve been reading The Color of Law (lightning review: extremely digestible, an important topic, succinct and powerful in argument, very much worth reading). I was born on the north side of Chicago (my parents eventually moved us out to suburbs), and between the institutionalized housing discrimination described therein, as well as recently having read up on the Nixon years, MLK’s work, and Harold Washington’s tenure as mayor I’ve realized just how pathetically little I knew about my hometown’s role in enduring structural racism. It feels a bit academic, but I’m fascinated with looking for data around this topics like this (over a century of housing discrimination in direct conflict with the constitution+evolving local demographics in general).

For anything associated with geographic demographics I immediately go to the census website and start checking out the availability of data. In this case, I was initially fascinated by the idea of graphically representing specific blockbusting cases mentioned in the book with some kind of flow diagram or crude maps.

## Data Acquisition
However, blockbusting as a formalized and supported tactic was outlawed on the surface by the end of the 1960s, and consistent, well-formatted demographic data on race at at least the county level isn’t (as far as I can tell) readily available from the census’ website until 1970. Despite this, I did find county level demographic data for every year from 1970 to now. Even better, I accidentally stumbled on a pre-existing aggregation of this data on the National Bureau’s of Economic Research's website. While I occasionally read an NBER working paper or two, I had no idea they hosted any sets of data (in this case it’s for The Surveillance, Epidemiology, and End Results (SEER) Program of the National Cancer Institute, who pulled the individual datasets together so nicely). These guys know their audience, because even .sas7bdat versions are available (this is where I make a face. . . SAS is less than my favorite thing to work with). Ultimately, I end up with a ~500MB .csv file that I won’t even bother attempting to open in Excel to poke at.

## What’s Interesting?
Now that I’m directly mucking about with a dataframe I have a few thoughts on producing interesting results, some of which I might address separately in a future post.

A method to identify counties with the largest absolute and % change might be an interesting proxy for reading up on news+year pairing in specific locations.
Do those counties conform with narratives I already read in the book?
Do the largest changes slow, indicating a kind of stratification?
Can I identify urban+suburban pairings that are inherently linked via white flight?
Can you identify inflection points based on events I have knowledge of or can track?
Realistically, I doubt I can infer anything directly toward the structural prejudices underpinning what has occurred in American housing since the end of Reconstruction, but I can at least provide a better mental picture to myself on what some of these change could look like.

## Onwards into Python

To start, we only need pandas, although that will probably change. I didn’t know anything about this data heading in, so I had to check out the column headers:


Ok, so what are unique values in the ‘race’ column?


From there I returned to the NBER website and followed a link out to SEER in order to get the data layout/dictionary and understand what those values meant:


I also need to take a look at what’s in a row of this data:


Turns out that I should probably make a unique identifier since the countyFIPS isn’t totally there. Plus, I want to be able to pull out state associations more easily going forward. TO do that, let’s use a zip inside of a list comprehension:


So now that I have the layout in my head as a concept I can think about how to parse the data and churn out some associations. Before I start filtering data down I know it’s pretty likely I’ll want lists of the unique values in identifier columns. In this case, county, race, and year are all identifiers I think will come in handy when parsing the data.


Before I continue, I should check how these values work as identifiers to filter the data down. In this case, I’m simply taking the first values in a given column to filter the dataframe down (and store it in a new variable in order to maintain t he original).


Over 13 million rows to only 38, that’s not bad! However, that’s still quite a few for a single county+year+race pairing, what’s in there?


Oh right, age and sex. Very useful for more nuanced analysis, but not necessary for where I’m starting, which is going to rely on aggregating county-level populations purely by race. Because the only distinctions left in each row were age and sex, it seems like the identifiers I initially chose will be enough to get a broad picture.

Now I’ll write a basic structure for the loop then start to work through what might happen on the inside (also, I’m importing pdb up top so I can do some interactive work mid-code):


Immediately I realize I’ve made a mistake. I just pointed out that I would get multiple rows as a result from the county->year->race filter, so rather than iterating over the resulting rows I should sum them by race. Thankfully pandas has a great builtin groupby function (note: for now I’m ignoring the hispanic flag because the impetus of the book and what I’m thinking about is the systemic disenfranchisement of African Americans from the housing market and subsidies enjoyed [overwhelmingly, but not solely] by white Americans):


From here I did a bunch of testing and had a few issues, but ended up with data packaged away into nested dictionaries.


Each key in resultsDict should be an individual county, whose mapped value is also a dictionary whose keys are years:


Key here is remembering where I put things and relying on the ordering to have not somehow gotten wonky partway through.

Now I’m going to work this data back out into a dataframe. While there are other (probably much more efficient) ways to handle this process, I like to set up dicts because then I don’t need to know how many or what values the keys are going to be. Had I sat down and sketched out something more concrete I probably would have appended values to a list and then to another list, eventually converting out that list of lists into a dataframe. I’m not here to be efficient though, just learn and practice (and I need more practice with dictionaries).

but . . .

Another mistake. Because I didn’t label anything I don’t actually know which population value is which when there’s no value for a race flag. This occurs to me as I write code for unspooling the data. I need to go back and construct the data differently. :(

This fix will also allow me to go back and fixthat error I’m excepting, proving once again that you should solve your problems at the beginning instead of just hoping they won’t keep coming up. Now I fill in 0s for every county-year pairing that doesn’t have one of the race categories.


Now I can get to pulling those dictionaries apart and stitching them back into a dataframe that is a little easier on me conceptually. Also, I can save the resulting product so that I don’t need to process the initial csv every time I run the script. This saves a time, as my inefficient processing of those 13.8 million rows takes a few minutes on my computer.


Here I’m going through the keys of each dictionary and creating a stack of lists that I ultimately turn into a dataframe and save back to disk as a csv file. I named the columns very simply, ‘wp’ is white population, ‘wc’ is white change, and so on. The exported file is a hair over 6MB on disk and an Excel-friendly 146k rows.

At this point I also wrap the whole thing in a function so I can turn it on and off by just not calling it instead of commenting large blocks of code in and out of service:


As always, I’ve bit off more than I intended for a Saturday evening, but let’s finish it out by at least looking at one of the questions I had above.

Meaningful Changes in Black Populations
Looking back to my first question to myself, I was considering how to identify counties that have particularly high rates of change. From there, you could look these counties up and try to identify specific events that led to these outcomes. If you were looking for specific tactics (like blockbusting or the demolition of public housing) outliers in this process could be helpful in identifying counties to look at more closely. So, I add a column to my results data calculating the percent change from year to year at column.

There was one final glitch though, infinite values. Because any increase from 0 isn’t measurable as a percent, those values come through as infinite and are trouble in a bunch of other processes. To deal with this I scanned the total population changes of these cases, and since they were all quite small I made the executive decision to simply remove them, although I could revisit these counties in the future. To remove them I used numpy to change them to nans and then dropped the nans:


Now I need to filter down the results to get potentially meaningful county identification. Big changes in population are likely to be counties with tiny populations. It’s unlikely we’d be able to link any events to counties this small, so let’s roll back a bit and filter one of the earlier dataframes to remove counties with tiny populations. I’m adding a new column, the total county population, which didn’t previously exist


At this point I realized that there’s one additional flag that could be useful for distinguishing specific events. If a large swing is mirrored by the county’s majority race then it is more likely to be some kind of natural disaster or other event that affected the county’s population indiscriminately (or a records error). So, I add in a white percent change column, and then look for row that have the opposite sign for white and black population changes (i.e., +/-). We can be a bit clever here and use the numpy.sign() function on both columns and add them together. Values of +/- 2 are uninteresting, +/- 1 is more intriguing, and 0s are the potential jackpot as they could indicate divergent population trends. To make this more useful, very small percent changes could be rounded down to 0.


Now I’ll take a few more steps to whittle down the data and hopefully get useful results.


First, I add a new column to track total black population from the previous year by summing the current population with the change*-1. Then I’m filtering to only counties that have at least 50k in population (dfBC = dataframe Big Counties), a total black population of over 200, removing the county-year pairs with similar movement for both races, and finally splitting apart the filtered dataframe into big losses and gains. I end up with 4 rows in the Gain data, and 17 in the Loss data.

The Gain results are interesting:


3 take place in the same county in successive years (a good reminder that I should add columns for cumulative change in 2/3/5/10/all year cycles). What’s up with that county? The FIPS code identifies it as Jefferson County in New York. First, a look at this change:


Above this, I added: “import matplotlib.pyplot as plt”

The 1980–1985 period is the one I’m interested in here.
I don’t see anything immediately from some imprecise googling of the county and terms such as “demographics change”, so I shift into a look at the population centers within the county, Watertown and Fort Drum. Watertown also turns up very little, although I do find some county documentation mentioning that this rural, northern NY county is more diverse than those surrounding it.

Finally, hit on a year and possible cause. The spike in white population in the mid-1980s seems to be the reactivation of the 10th Infantry Light Division, but prior to that:

In April 1980, B Company, 76th Engineer Battalion (Combat Heavy) was reassigned from Fort Meade, Maryland. It was followed by the rest of the battalion, with the exception of D Company, three years later.
Was this unit primarily African-American? From looking at what documentation I can find, it seems the answer is no. They're not mentioned at all in an Army Corps report on the African American experience in the military. Instead of looking for specific years, perhaps I can find history on things mentioned in The Color of Law, such as public housing.

Eventually I find the Watertown Housing Authority’s website, which has a convenient list of projects:


Because Cloverdale was among the oldest apartments, and since it was demolished it seems like a strong candidate to show up in the data. Between 2003 and 2009 Watertown lost ~10% of its black population (7,810 to 7,010), but in the following 6 years, it grew by nearly a third, from 7,010 to 9,193. The first direction seems reasonable (i.e., evictions and resettlement in the years leading up to demolition), the next 6 years are confusing. Did additional housing open up? Was there some relocation deal as part of demolishing Cloverdale? Did a new factory open, or an old facility refurbish?

So, for now, I’m uncertain what the primary drivers in this county’s demographic changes were, and I’ve exhausted my single-day writing reservoir. I’m going to keep thinking about Watertown and Jefferson county, but my next post will probably try to bring in a little more of my personal expertise in the energy industry and environmental/health impacts of project siting.
