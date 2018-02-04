# Herfindahl-Hirschman at the Movies

## Disney Acquires Fox
In a move that’s been rumored for weeks and discussed for years the Disney behemoth purchased a large chunk of Fox this morning for $52.4 billion. One thing that stood out to me in the coverage of such a massive merger was the anemic attention given to any potential anti-trust implications in the wake of what appeared to be a significant concentration in certain fields of media. I know the DOJ has been somewhat weak in the area for several decades, but the overwhelming feeling of foregone conclusion in media coverage felt off to me.

A few people expressed dissent, as mentioned in the article linked above, but it seems like the overwhelming majority, from Wall Street, to reporters and analysts presume the deal will go forward. Additionally, at least some of those expressing skepticism appear somewhat more focused on the erratic nature of the current administration rather than market power concerns. It’s possible I’m just overly suspicious due to my day job of monitoring and analyzing energy market processes and outcomes, which have some natural tendencies towards these outcomes, but I thought that even a superficial look would be a fun evening project.

## What to Measure?
In terms of quick and dirty analyses with real endorsement from enforcement bodies, the Herfindahl-Hirschman Index (HHI) seemed like a great entry point. Wikipedia has a good opening line:

The Herfindahl index (also known as Herfindahl–Hirschman Index, HHI, or sometimes HHI-score) is a measure of the size of firms in relation to the industry and an indicator of the amount of competition among them.
HHI is something I’ve occasionally calculated in other endeavors, so I’m familiar with the 0–10,000 structure of the metric and how to calculate it. The Department of Justice defines handy tiers of HHI values that industries can fall into when agencies are conducting analysis:

Below 1,500 — Not Concentrated
1,500–2,500 — Moderately Concentrated
Greater than 2,500 — Highly Concentrated
These values don’t inherently force action, but they provide a heuristic through which to consider a particular market. So now I’ve got a metric, but how the heck are we gonna apply this to a wide-ranging media conglomerate?

## Python Scraping Mojo
While there are a few ways we could go about this, as a longtime fan of (comics representations of ) the Fantastic Four movies were the first thing on my mind (as opposed to, say, TV). I also had an idea about how to (hopefully easily) represent the market shares of respective firms. For a casual analysis I wanted something attainable in a single evening, and I thought Box Office Mojo might have what I was looking for. While imperfect, it seemed like box office share per studio for all tracked releases in a given year could be a sufficient proxy for market share in any given year.

So, now I had an idea and a data source, but how to quickly acquire and handle it? Python. I build webscrapers and interfaces semi-frequently to satisfy both professional and personal curiosity, and fortunately had seen everything Box Office Mojo had going on before. In fact, this was a particularly easy lift as the relevant data existed as a table within the page and you could iterate over years and page numbers constructing the relevant URLs and collecting data inside of the same loop.

The one snag I hit as part of that process was in the number of pages. Initially I tried to be clever and grabbed their descriptive table of all years, divided the number of movies by 100 and rounded down to get a page count (100 movies per page). This didn’t quite work. It gave me a cap on the possible number of pages, but in earlier years (the data goes back to 1980), they didn’t actually have numbers for every movie. I set an exception for year+page combos that were under the possible limit, but might not have data. A crude solution, but effective. I’m sure you could also get the page number from the html of the first page somewhere, but I never really want to muck around in html any more than I have to.

1999 through 2017 had complete data, or at least the number of pages lined up with the number of movies released. 1980–1982 and 1996 were also fine, but I’m just going with the continuity of the last 17 years (1999–2016). I saved every year+page dataframe separately just in case something broke along the way, then rolled everything up into one file by walking through teh download location.

## Who’s Really in Charge?
The last piece before actually calculating HHI is the potentially very tedious matching of studios and distributors to their actual ownership. Fortunately, HHI is often calculated with only the top 50 firms in a given market, greatly reducing the amount of manual QA/QC I needed to perform. Additionally, the top 50 studios for this 17 year period I’m interested in account for over 98% of the total take in that same time frame ($143.58 out of $145.77 billion). However, an overall better move would have been to pull from the studio pages themselves, which I didn’t know existed until I started to sort that out.

I ended up assigning the top 70 major studios, which involved checking against 86 smaller studios. I missed 3 smaller studios around the 50 firm mark as their abbreviations weren’t clear to me, but they shouldn’t have an impact as I’m replacing them with close to identical dollar amounts (to be honest, this part totally sucked, and I would rethink my initial data grabbing process now that I know more).

## Results

Three things are immediately apparent: HHI might have been rising already, this merger shifts the concentration up, and the volatility of the movie industry causes interesting year-to-year fluctuations (which is expected). At this point, it’s useful to go back to the DOJ and consider their more detailed guidance on HHI, specifically:

b) Post-Merger HHI Between 1000 and 1800. The Agency regards markets in this region to be moderately concentrated. Mergers producing an increase in the HHI of less than 100 points in moderately concentrated markets post-merger are unlikely to have adverse competitive consequences and ordinarily require no further analysis. Mergers producing an increase in the HHI of more than 100 points in moderately concentrated markets post-merger potentially raise significant competitive concerns depending on the factors set forth in Sections 2–5 of the Guidelines.
In my data, the 2016 HHI moves from 1261 to 1741.

Given the box office successes of 2017 so far, a similar spread certainly seems possible. All of this is rough, but I hope it demonstrated how anyone can try and think about what you see in the news to work through what’s happening and what isn’t.

Like always, everything’s on GitHub.
