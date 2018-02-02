# Power Plant vs Home Furnace: What’s more Efficient?

*Note: I was certain I’d be able to finish writing on the plane and then publish
from the tarmac at DCA, but my seat was so cramped that I couldn’t use my laptop
and I finished this the following day.*

I’m sitting in the Indianapolis airport and I have a question. Is home heating
via natural gas more or less efficient than electric heating that is ultimately
powered by a modern combined cycle natural gas power plant. Typically I would
guess that the economy of scale offered by the power plant would favor the
electric option, but as a non-homeowner I don’t know enough about the efficiency
of modern residential heating options and had a suspicion that burning the gas
at home could also be quite efficient. Plus, if the discrepancy was large it
would really challenge the current status quo of power plants scrambling for
tiny amount of extremely expensive gas every time winter arrives in New England.
But really, I have no clue. With my limited pre-flight time frame, let’s dig in.

First, I have to find a data source. Fortunately, Energy Star maintains pretty
much everything I need. For this simple thought experiment I’m going to look at
the most efficient unit of each major heating type that’s able to fit through
some rule of thumb criteria. I’m going to use the [40Btu/sqft criteria for
colder climes found
here](http://homeguides.sfgate.com/many-btus-furnace-need-house-100318.html)
(since this is of particular importance in those places to begin with given the
demand for natural gas on both sides of the question and the physically limited
supply) and a theoretical 2000sqft house, which sounds “normal” to me (I suspect
a more thorough look would reveal something in the 1500sqft range as more
appropriate, but I’m trying to make this easy on myself). That house would
require a peak 80,000 Btu/hr output from its heating technology (Note: these
systems are probably oversized). Originally I wanted to look at air source heat
pumps, ground source heat pumps (GSHPs), and natural gas fired furnaces, but
there are no energy star air source heat pumps past a 57,000 capacity, so they
will have to wait until the next time I am trapped in an airport and my mind
begins to wander.

The basic numbers are below (stripped directly from my IPython notebook to save
time:

![](https://cdn-images-1.medium.com/max/800/1*nrewMCJ5-QNk8pX9F89LVg.png)

COP is the coefficient of performance for heating mode on the GSHP. It’s a pure
ratio, which suggests that for every 1 kWh, you are returned 3.9 kWh of heating
performance. Here’s my first set of calculations:

![](https://cdn-images-1.medium.com/max/800/1*528dICi6jWSCKWDSkuQXsQ.png)

Now we need some fuel costs and efficiencies The furnace owners needs 85395 Btus
straight up and some quite small amount of electricity, let’s say:

365 days, 100 with significant heating needs, 16 of hours in those days, so 1600
potential heating hours and 334/1600 = 0.20875, which we’ll round down to 200
Watts. Like I said, quick assumptions.[ Thankfully the BLS region which includes
Boston published some handy statistics
recently](https://www.bls.gov/regions/new-england/news-release/averageenergyprices_boston.htm)
making my data search much simpler. So, we have:

![](https://cdn-images-1.medium.com/max/800/1*nh70OGWHDbvZ23B5ZQ-qJg.png)

Now to look at the power plant efficiency of providing that electricity:

![](https://cdn-images-1.medium.com/max/800/1*PQkFEQGRU7XCgTPV_wZc2A.png)

So, you have a somewhat lower operating cost, and a dramatically more efficient
use of natural gas, what’s not to like? It all comes back to upfront costs at
the home level, and historical incidence at the regional planning level. At the
regional level, the natural gas transmission system in the northeastern united
states simply wasn’t designed with large power plant draw downs in mind. It’s
not a huge system, with almost complete control by local distribution companies,
who have large scheduling right carve outs often granted through grandfathering
when the current set of standards was put into place by FERC. Additionally, the
variability of the access and requirement for natural gas at a power plant used
to be a bit more variable, and still can be as those units are often at the
margin. This leads to a situation where power plants don’t want to pay for firm
capacity, even when it is available. This is perhaps a situation that could be
changed by significant top-down planning, or some changes to the market
structure, but it seems unlikely that either will be on the forefront any time
soon as the main friction over integration of public policy into the markets in
these states is currently related to renewable goals and carbon credits.

At the individual level, we have the sticker shock of GSHP units, which is
probably the largest barrier to adoption. I found [that Lennox furnace for a
$2,350 unit cost and a $3,700 unit installed
cost](http://www.pickhvac.com/gas-furnace/lennox/). Seems expensive, but not
terrible for an absolutely top-of-line in efficiency furnace. But what about the
GSHP? I couldn’t find the exact model price from[ the same
website](http://www.pickhvac.com/geothermal/waterfurnace/) as the gas furnace,
but they did have ranges for what appeared to be the previous model numbers.
Using a [few
](http://www.energyhomes.org/renewable-technology/geoinstallation.html)[other
](https://www.homeadvisor.com/cost/heating-and-cooling/install-a-geothermal-heating-or-cooling-system/)[sources](https://www.geoexchange.org/forum/threads/so-i-have-a-pair-of-waterfurnace-quotes.6061/)
it seems like the top end of the cost curve would be somewhere around $25,000,
and given the high-end status, size of the unit, and required installation costs
probably not less than $20,000 on the low end. Of course, since the GSHP unit
costs less to operate you would eventually recoup your costs, and to close out,
here are a few charts examining that:

![](https://cdn-images-1.medium.com/max/800/1*DLfpnNi1Rz0VYIkJmeZGcQ.png)

![](https://cdn-images-1.medium.com/max/1000/1*zVQ9i_l-XUGLt4ZHcWWWfQ.png)

It’s important to note that this is a harsh look at GSHPs. I’m comparing a very
expensive and large unit against its less efficient season, and I’m not doing
any discounting or discussion of financing options. Additionally, there used to
be a 30% federal tax credit (through 2016) for installation of energy star
certified systems. Exactly the type of example system we used. With that 30%
applied as a straight reduction to install costs, it looks quite a bit
different.

![](https://cdn-images-1.medium.com/max/1000/1*5wI4cfayFLN_BRY_7TcYzQ.png)

With all that in mind I hope this was at least a mildly interesting look into
the competing uses for natural gas in colder climes, and the lack of efficiency
resulting from a misalignment of rights to ship and flow gas when considered in
the context of the entire system of end users.
