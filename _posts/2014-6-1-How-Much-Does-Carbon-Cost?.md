# How much does carbon cost?

## Exploring Green Electricity in Tennessee

*****

I recently moved to Tennessee. The state isn't exactly [known for its
environmentalism](http://en.wikipedia.org/wiki/Kingston_Fossil_Plant_coal_fly_ash_slurry_spill),
so I was surprised when I received the header in my mail a week or so ago.
Nothing similar had ever shown up in my mailbox when I lived in Illinois or
Indiana. What really excited me were some concrete numbers to work with.
Predicting carbon costs seems to be a favorite activity of energy economists
(right below arguing how a carbon cost system will actually be implemented [not
should be, that’s mostly been settled]), and since I seem to be one at least
partially, I felt it would be a betrayal of my adopted profession to not explore
the mailer’s implications.

Immediately, it was abundantly clear that my usage isn't typical. This makes
sense. I live alone in an apartment, don’t use the HVAC, and the only appliances
that remain plugged in (to an energy-saving “smart” power strip) are my PC,
speakers, and monitors.

The typical household use is easy enough to derive:

(X)(0.12) = 150kWh => X = 150/0.12 => X = 1,250kWh/Month

Additionally, you can find the $/kWh of renewables:

($4)/(150kWh) = $0.0266

I've only had 3 billing months but this is what my electricity consumption looks
like so far:

![](https://cdn-images-1.medium.com/max/800/1*LCVMQEBFUHOnO9L0qDwvxQ.png)

If I had signed up for a 3 block plan when I first moved in it would have
covered nearly all of my electricity use:

(450kWh)(3) = 1,350kWh => (1,350)/(485+611+346) = 0.936, so ~94%

But what does this even mean? Most of the time when you’re purchasing renewable
energy you’re purchasing the basically the same electricity mix as before, but
somewhere a renewable energy project is getting paid to produce energy in their
area. Last September, [Google entered a purchasing agreement with a wind farm in
Texas and provided a good
explanation:](http://googleblog.blogspot.com/2013/09/another-windy-day-in-texas-new-power.html)

> Due to the current structure of the market, we can’t consume the renewable
> energy produced by the wind farm directly, but the impact on our overall carbon
footprint and the amount of renewable energy on the grid is the same as if we
could consume it. After purchasing the renewable energy, we’ll retire the
renewable energy credits (RECs) and sell the energy itself to the wholesale
market. We’ll apply any additional RECs produced under this agreement to reduce
our carbon footprint elsewhere.

In my case, with TVA, i[t’s slightly
different.](http://www.tva.com/greenpowerswitch/providers/pdf/gpp_guidelines.pdf)
The program in place literally involves the addition of small renewable sources
of power to the TVA mix. Specifically small-scale generation with capacities of
50kW and lower. This agreement includes a 10 year price premium per kWh
depending on the generation source.

![](https://cdn-images-1.medium.com/max/800/1*6HwHti4BCkbqHJOg7LG7xg.png)

I still might not be getting those electrons, but they are getting added to my
utility’s daily load. Some updates near the end of 2013 have the program
providing [6MW allocated for non-residential customers and 4MW for
residential](http://www.tva.com/greenpowerswitch/providers/index.htm). As of
early 2014, the non-residential power pool was over-subscribed, leading to a
random selection structure, while the residential pool was under subscribed by
1.36MW, triggering a request for additional purchasers.

One nice thing about these numbers is that you don’t have to worry about typical
pitfalls when calculating power plant output, like efficiency and capacity
factor. In this case, the provider is promising that 10MW of renewables will be
constantly available. 4MW of residential doesn’t sound like much, but how many
households could that cover?

4MW refers to the capacity of the generating equipment, and due to the agreement
we expect that to be stable. MWh or MegaWatt-hour is the actual generation. How
do you calaculate MWh from a given MW? Simple, multiply it by the runtime in
hours. In this case, I’m going to work on an annual basis, and there are 8760
hours in a year (this is one of those numbers you never forget when working with
generation, just don’t miss the extra 24 in leap years).

(4MW)(8760hours) = 35,040 MWh/year

In kWh this is: (35,040MWh)(1000) = 35,040,000 kWh/year

Very quickly, that little 4MW has gotten much larger. Now, using our typical
household monthly energy consumption derived above we can calculate the number
of typical households these renewables could power.

(1250kWh)(12) = 15000 kWh/year =>(35040000)/(15000) = 2336 Households

Similarly, we can calculate the number of “blocks”:

150kWh/Block => 35040000/150 = 233,600 blocks

It’s taken a little bit, but let’s pivot towards the title and talk about the
cost of carbon. The [EPA’s Power Profiler tool
](http://oaspub.epa.gov/powpro/ept_pack.charts)provides a rough breakdown of
your utility’s emissions, and the national average. Here’s what my breakdown
looks like:

![](https://cdn-images-1.medium.com/max/800/1*U6VaVHHxGY__wYYWyYneFg.png)

![](https://cdn-images-1.medium.com/max/800/1*eYz7Mli1MV8AXdUwAyG-QA.png)

The TVA has less renewables and more coal than the national average, which isn’t
particularly surprising, but the real value of this tool is the emissions
breakdown is also provides:

![](https://cdn-images-1.medium.com/max/800/1*U-MCCHTRoeoOF-90WX3dKw.png)

NOx and SOx are important local and regional pollutants, but the focal point for
me here is CO2, and utilizing it to develop a price for carbon. Normally, I
might switch to using just Carbon at this point, but the [European Union
Emissions Trading System (EU ETS) prices tonnes of CO2,
](http://ec.europa.eu/clima/publications/docs/factsheet_ets_en.pdf)which saves
us a handful of conversions (for now).

So, if every kWh of renewables purchased above costs me $0.0266, that would
theoretically remove the entire 1.389lbs of carbon per kWh of generation, i.e.,
a credit for 1.389lbsCO2 costs $0.0266 under the TVA’s program. How does this
compare to the EU’s ETS?

Unfortunately, I might be an idiot because I couldn’t find a good, free source
of ETS pricing data. The most recent mention I found [was
here](http://www.businessgreen.com/bg/analysis/2337543/eu-carbon-price-rides-the-rollercoaster-as-emissions-fall)
quoting a price of around 5 Euros per tonne in the beginning of April. At the
same time, the conversion rate of Dollar:Euro was 0.7263:1. Back to a bit of
arithmetic:

(5 Euros)/($0.7263/Euro) = $6.884/tonne, but our emissions are in lbs

1 tonne = 2204.62 lbs => $6.884 will buy you 2204.62 lbs of CO2

But what is the TVA’s price on that ton of carbon?

$0.0266 = $/kWh of renewable energy, and each kWh removes 1.389lbs

(2204.62/(1.389) = 1587.199 => ($0.0266)(1587.199) = $42.2195/tonneCO2

$42 per tonne of CO2 is a little over 6x the price on the EU markets, and I
think that’s a good thing. It’s displaying a much more realistic cost of
alternatives within the confine of our existing infrastructure. The EU credits
are so cheap because the design of their system has essentially failed. Perhaps
programs like the TVA’s will produce a credible body of data for designing
effective future carbon pricing schemes.

As a final aside, I did attempt to compare this cost to TVA projections.
Utilities publish documents known as Integrated Resource Plans (IRPs) that
typically detail their current generation mix, ongoing projects, and projections
out a few decades. Unfortunately, the last IRP published by TVA was in 2010.
Planning meetings for the latest IRP have been going on since the fall of 2013,
but concrete publications have yet to emerge. Back then, the highest price they
put on carbon (and I believe it is carbon this time around, not CO2) was
$30/tonne in 2014 under their scenario which was most optimistic about the
national economy (hint: that scenario was not accurate). If their accounting was
in straight carbon, that $30 would be worth even less relative to the $42/tonne
of CO2 due to the weight of those pesky oxygens.

I’m sending back my mailer with a 3 block monthly purchase (450 kWh or $12),
although I may do some math on my daily commute and purchase more to offset some
of that as well.
