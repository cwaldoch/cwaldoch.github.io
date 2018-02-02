# Commuting with a price on carbon

Recently I’ve been thinking about the cost of my daily commute. Via transit, I
pay $7.50 each way, $15 total. From Alexandria on the blue north to Rosslyn,
then an orange West to Vienna, and finally a bus from the station to my office.
I get a $0.50 discount for transferring from rail to bus and vice versa. WMATA
has extremely limited options in terms of “all-you-can-travel” monthly passes.
They’ve been making changes to the program recently, but only some tiers include
bus travel, and last I checked they didn’t have an adequate option for my normal
commute. Driving is ~19 miles each way, and I got around 30mpg. Gas prices were
typically in the range of $2.20-$2.40, so I’ll use $2.30. Each day that works
out to $2.913 for gas. In 2017, [the IRS used $0.535 as the standard mileage
rate](https://www.irs.gov/newsroom/2017-standard-mileage-rates-for-business-and-medical-and-moving-announced),
so we’ll add another $20.865. . . and, wait, I’m already past the $15 I spend on
public transit. Without even adding in some kind of price for the externality of
CO2 I’m already saving money, at least according to the IRS.

Originally I had intended to write up a fun breakdown of the emissions intensity
for driving and the rail+bus option (including an attempt at reverse engineering
[an old WMATA tool for this sort of
thing](https://planitmetro.com/greenhouse-gas-emissions-savings-calculator-2/)),
then find the price on carbon that creates pricing parity at the point of the
individual user. However, I was both surprised by just how high the standard
mileage reimbursement rate was, and unprepared for this possibility given the
relative sticker shock of handing $15 to WMATA each day. For daily spending
perspective, I eat lunch out maybe once every 4 months, and then it’s a $9
falafel platter from the place next to my office.

In order to drum up a bit of intrigue, let’s drop the mileage rate entirely.
Perhaps you’re someone like me (most people in this case I’m guessing) who is
vaguely away that driving costs more than just the gas, but hasn’t truly
internalized the steady stream of change flowing out of your tailpipe. First, a
trip to fueleconomy.gov to check the emissions from my car, [which comes out to
299 grams per mile](http://www.fueleconomy.gov/feg/Find.do?action=sbs&id=32532).
Not terrible in the grand scheme of American automobile purchases, but truly
awful in the context of global consumption. WIth that rate and the 453.592 grams
per pound we get:

(19*2*299)/453.592 = 25.05 lbs of CO2 per daily commute

On the metro end of things we can use the [Emission Factors for Greenhouse Gas
Inventories from the
EPA](https://www.epa.gov/sites/production/files/2015-11/documents/emission-factors_nov_2015.pdf)
(which unfortunately doesn’t seem to have been updated in the past two years).

![](https://cdn-images-1.medium.com/max/800/1*6TvqZq1AjlZGDQHAFYEK_A.png)

While not perfect, I believe these are the numbers that WMATA used for its own
tool mentioned above. Additionally, when I calculated my own values (scripts on
GitHub), I was able to reach similar values by assuming fully seated train cars
and working back from the train car kW values and local generation mix. On
additional important piece of context, unless I missed something I should be
using straight CO2 values here (in an endeavor to keep things simpler), not CO2e
and not other emissions like CH4.

I got about 20 miles by rail and 2 by bus, so:

((20*0.133)+(2*0.058))*2 = 5.552kg -> 12.23lbs CO2/day

However, I’m under the impression that the Metro system is a bit heavier than
typical subways given its dual role, so I’m going to bump it up to 0.15:

((20*0.150)+(2*0.058))*2*2.20462 = 13.739lbs CO2/day

Here’s a table to sum where we are:

![](https://cdn-images-1.medium.com/max/800/1*GGajNgpomQ2jdSYuD2QUJQ.png)

And here’s what it would take for a price on carbon to equalize the upfront
costs in each of those endeavors (where the orange and blue lines cross)

![](https://cdn-images-1.medium.com/max/800/1*y4nlDDkMkmWnz76P-KkFCw.png)

between $2,142 and $2,143. Which is quite a lot. As a thought experiment, what
if the emissions intensity in the local generation system was lower enough to
pass on a 50% emissions savings to the transit option?

![](https://cdn-images-1.medium.com/max/800/1*iSjyBCft9PyYwV_o1taykg.png)

Here the change occurs right around $1,332. Still pretty dang high given carbon
costs in the real world haven’t come close to that value. The point of this is
not to be discouraged, but aware. A price on carbon won’t always achieve parity
in a visible enough way for people to change their behavior, so it’s important
to consider the context of our systems, what prices people see, and what changes
could result in.

Also, one more caveat: America loves trucks. Automakers sell pickup trucks by
the boatload, and they‘re significantly less efficient than my car. In 2016, the
top 3 lines of best selling vehicles were pickup trucks, and they combined for
1.7M in sales. The total for all trucks is higher. If we take a 2016 Ford F-150
with 4WD and drop it in using the same sources for values as above, the graph
looks a bit different.

![](https://cdn-images-1.medium.com/max/800/1*y6r4VUmQdQ1i6yr7q4Zsng.png)
