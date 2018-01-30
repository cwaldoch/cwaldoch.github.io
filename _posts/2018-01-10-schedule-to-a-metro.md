# What’s a schedule to a Metro?

Back in the fall I stopped driving to work. As far as I knew the Metro had
largely been on fire since before we even moved to the area, but, for the good
of my mental health the hate-despair relationship I had cultivated with the
Beltway had to end. Bonus, I like trains! And not just the idea of trains, but I
legitimately get a dumb fuzzy we’re-all-in-this-together feeling on urban light
(or heavier commuter) rail. It reminds me that not everywhere in America fully
succumbed to personal-automobile-centric planning, and I enjoy actually using
the infrastructure around me in a non-antagonistic way (when it comes to the bus
I am more technically appreciative of its efficiency, but being the shallow
human I am, less dreamily enthralled by its more pedestrian status). Despite my
inherently positive outlook on urban transit, I can’t turn off the
critical/analytical/why? part of my brain, and recently I’ve been baffled by
WMATA’s on-time statistics.

At the end of my commute via train I take a bus. That bus departs on a 30 minute
schedule. There is a backup bus, but it is slower, and leaves within 7–8 minutes
of the first bus, which does leave me with a window, but not a great one. On the
way home I’m able to track the buses directly and walk out of my office onto
one, and I walk home from the station, so I almost never stress over my evening
commute. The morning is different. While I’m fortunate to have a flexible
workplace, I normally plan on getting to the office between 7:30–7:40, and
changes to that can throw off my schedule for the day. It feels like this is
happening a lot. It seemed bad enough that I started waking up earlier to catch
a train before the one that should have been fine. I used “seemed” and “feels”
because I don’t actually know. But I think I can. To that end, I’m going to be
focusing on my morning commute here: Braddock Road to Vienna.

#### When are trains supposed to come?

When I stopped driving I went to the Metro website to look for a time table and
gave up. All they provide is this:

![](https://cdn-images-1.medium.com/max/800/1*x5kxytqs1l5-MJcLYzi76Q.png)

Which is fine, but I’m used to looking at a table and seeing projected times.
Instead, I internalized the 8 minute intervals and 5AM start.

While they don’t seem to provide an accessible schedule as a simple table
anywhere, you can make use of their trip planner to get the same results, just
slowly. Monkeying around with this a bit it turns out my optimal train to catch
is at 6:34, and it should take 17 minutes to arrive at Rosslyn. The ideal
Rosslyn train departs at 6:54 and should arrive in the Vienna station at 7:17,
25 minutes later. My bus departs at 7:29, so on its face this leaves me plenty
of time. In fact, if the system ran on schedule I could take the next train at
each station, and still arrive by 7:25, providing me with a spare minute or two
once I’ve ascended the stairs, crossed the 66-moat, and embarked on the bus.
This is the commute that Google maps, the Transit app, and Metro’s trip planner
all told me would work. Unfortunately, this doesn’t happen in practice.

#### Metro’s on-time Scorecard

In November [I touched on the process required to pull down and start working
with your own SmarTrip card data
](https://medium.com/@waldoch/collecting-and-processing-wmata-smartrip-use-history-with-python-60e15b7a5d2b)(register
yours if you haven’t, you’ll never have to fumble at those often-broken fare
machines again!). Within those pages, WMATA also reports the on-time scores of
the last 3 months of transit for that card at the MyTripTime Dashboard link from
the main page for a given SmarTrip card. Here they report my overall on-time
score:

![](https://cdn-images-1.medium.com/max/800/1*QL7CoYeppDCh542mVf4_Pg.png)

and then specific scores for my most common trips:

![](https://cdn-images-1.medium.com/max/800/1*lcuxLEI4rqIfaeWrlbpLmA.png)

The numbers here are a bit confusing. The minutes are based on my time swiping
in and out at each station. Most of the time I’m not immediately getting on a
train, so there’s inherently some time built in. However, the range metro gives
themselves (38–59 minutes) is **21 minutes longer than the ideal commute.
**Those 21 minutes are like adding an entire additional commute leg, an increase
of 55% over the ideal commute, and a shockingly wide window considering that at
the point when I arrive at the station the system has been operating for ~90
minutes. Long enough to hopefully sort out the system’s first kinks of the day,
but well before the day’s compounded errors take hold. Crucially, I’m near the
first wave of the bulk of commuters, so any issues with my commute are a bad
sign from the remainder of that daily tide.

Most people can’t freely add an extra 50% to their commute time, and those who
can are less likely to be negatively impacted in the first place.

These numbers indicate that slightly less than 1.5 out of 10 of my morning
commutes are not on time. What do those numbers look like under less generous
conditions?

#### Back to the Data

First I updated the previous results with the last ~6 weeks of commuting. I also
learned that old data rolls off the system. My original code looked back to
October, 2015, but now December, 2015 is the last available month. If you want
your data, go and get it. I wrote a little script to look for my morning
commutes and output the results as a csv to eyeball it for errors:

![](https://cdn-images-1.medium.com/max/1000/1*Yz0FEwS6KdRUam7pdvvM4g.png)

While looking at the results I manually added in the trains for my morning
commute M1 is my typical train recently at a 6:34 scheduled time, M2 is supposed
to be at 6:42, and so on. Any entry at Braddock that is < the time of a train[n]
and ≥ train[n-1] was assigned to train[n]. From there I wrote another little
script to iterate over every trip on each train and calculate if I arrived
within 1 to 21 minutes of my predicted arrival:

![](https://cdn-images-1.medium.com/max/1000/1*OAyI599qO9igjJItQdlryA.png)

Finally, I added some code to plot the different arrival by % on-time with
minutes added from 1–20 (as well as a weighted average)and got these results:

![](https://cdn-images-1.medium.com/max/1000/1*nzug-PbbnXmdQ41ubpXdng.png)

I am slightly generous to the scheduling in some ways, so it makes sense that my
ultimate result at even 20 minutes over the ideal 38 would be greater than 86%,
but overall I think this presents a poor image of a more realistic on-time
consideration. Only 60% of my trips have completed within 5 minutes of the ideal
travel time, but it takes another 5 to reach 80%. Unfortunately, my most
traveled trip isn’t on time, but the reason I shifted to that earlier train was
to make sure I made the bus. It seems that I’ve probably continued to make the
bus at a similar rate as before (since the purple line is one of my more
reliable trips), but my trips have been (and presumably felt) longer, which
prompted me to look into this in the first place.
