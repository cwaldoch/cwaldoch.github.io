![](https://cdn-images-1.medium.com/max/800/1*6ozbVUi4gFqnJeL3EAPCXQ.jpeg)

# Generalized Python Graphing for EIA-860

With the delayed, but [impending release of 2013 electric generator data from
the EIA](http://www.eia.gov/electricity/data/eia860/), I thought this would be a
good moment to whip up some form 860 specific graphing code. [It’s been a while
since I looked at the 860 data for
fun](http://btus.us/the-state-of-our-energy-storage/), and back then I barely
had a grasp on Matlab, let alone Python. While still a relative novice, I can at
least cobble together enough working lines of code to generate better looking
graphs more quickly. Again, I’m not a code guru, I just enjoy making graphs and
looking at data outside the confines of Excel. This is more intended for people
seeking help to get started, curious about EIA data, or bored and enjoy
nitpicking some relatively novice code. I started writing this before the 2013
data was released, so I’ll be referencing the 2012 numbers. [I created a Github
repo to store the excel data and scripts as well if you want to grab the
code.](https://github.com/cwal37/EIA_860)

First, the easiest way to follow along a bit or just do this better is either
[Python (x,y)](https://code.google.com/p/pythonxy/) or
[WinPython](http://winpython.sourceforge.net/). Both of those are Python
packages put together for scientific computing. They come with most of the
well-known libraries, and Spyder, an IDE which is similar to Matlab in some ways
and might help ease the transition if you’re coming from there. I like Spyder
because it has a nice variable explorer window which saves me a fair amount of
time when I’m troubleshooting data types. To me, the major difference between
those two packages is that WinPython doesn't require a full installation, you
can even run it from a flash drive (although the speed may leave something to be
desired). Either way, both of those will be able to get you up and graphing in
no time. I’m not offering much of an installation guide here, because their
resources are far better than anything I’d come up with.

The truly crucial libraries I’m working with are pandas and matplotlib. I think
of pandas as my datatype savior. Before I started messing around with it last
year my graphing code was often a mess of conflicting datatypes, and I wasted a
lot of time on diagnosis. With pandas I just pull any csv/txt/xls/xlsx file in
as a dataframe and go from there. You can still run into datatype issues, but I
find everything to be much more clear with pandas. [Matplotlib is a plotting
library](http://matplotlib.org/) with an extreme amount of possible
customization depending on how deep you’re willing to dive. N[umpy is basically
the workhorse for scientific operations and allows direct integration of Fortran
and C++](http://www.numpy.org/), and we’re using os to create an output
directory. We might not use numpy, but I import it reflexively in case I need to
test something along the way.

    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    import os

At this point, I've already grabbed the 2012 860 data and unzipped the
spreadsheets to my desired folder. From here I decide I want to look at the
operating generators, so I grab that workbook and sheet.

    base_data = pd.read_excel(r'./GeneratorY2012.xlsx', 'Operable', skiprows=1)

At this point there are a couple things to notice. First, I have the data and
script in the same directory. That’s the r before the file name, if you have it
elsewhere, just put the entire directory inside the apostrophe. You can have
them anywhere on your computer, but I prefer to silo off each project I do in
its own directory or my structure gets messy and confused. In my case, the full
directory would be ‘Z:\Projects\Data\EIA_860\GeneratorY2012.xlsx’. At this point
observant Windows users might notice that in the typical directory structure we
see there’s a \, but in my code the filename is preceded with /. Don’t forget to
make that correction, the backslash is a Windows-specific quirk. Also, I’m
skipping the first row. If you open up the spreadsheet you’ll see that the first
row isn’t data, and is junk. In the past I would have deleted that row and
re-saved it, but this is the glorious code-novice future, so just skip the row.
Finally, save yourself some time and save the .xlsx as a 97–03 .xls, which will
run far, far faster. Don’t forget to change the filename to match your new
filetype.

So you’ve got the data in Python, that’s cool, but what’s actually in the
spreadsheet? You could open it up in Excel and take a look at the column
headers, but I’m trying to avoid Excel here, so let’s print a list of the column
headers.

    print list(base_data.columns.values)

This is going to return a whole mess of words in the console, but it should give
you an idea of what’s available. The 5th column is State. Often when dealing
with the United States a distinction is made between the contiguous US and
Alaska/Hawaii. This is particularly pertinent when talking about generation
infrastructure as those states are not part of the same grid as the lower 48
(Hawaii’s islands are themselves each a stranded market, which is kind of
crazy). Going from that, let’s turn an eye towards the lower 48 and further
ostracize Alaska and Hawaii. First I’m going to create a new dataframe, a
working copy of the base_data.

    working = base_data

Then, I’ll exclude Alaska and Hawaii from the the dataframe.

    working = working[working.State != 'AK']
    working = working[working.State != 'HI']

OK, so the code didn’t crash, and it probably worked, right? But what if you
wanted to check, just to be completely sure? No problem, here’s a slightly
circuitous path, but it will introduce you to a few more concepts. We’re going
to get a list of the states from the state column, reduce it to unique values
only, then sort it in alphabetical order so that a quick glance can confirm or
deny the presence of Alaska and Hawaii once it’s been printed.

    print sorted(set(list(working['State'])))

While the list, set, sort, and print are condensed into one nested line, you
could split them out individually as well, although it’s going to take more time
and provide more potential points for error.

    states = working['State']
    states_list = list(states)
    states_set = set(states_list)
    states_sorted = sorted(states_set)
    print states_sorted

From here, we can jump into the data and calculating/graphing. I’m going to use
the prime movers to start out. Roughly put, prime movers designate the type of
technology a generator is. The full list is as follows:

![](https://cdn-images-1.medium.com/max/800/1*Wulk6sR_S8lqcyeHEP4bfA.png)

A simple first pass is the collection of nameplate capacities for each prime
mover. To do this, we’ll turn to the groupby function of pandas. Groupby allows
you to split and combine dataframes based on values in the original.

    prime_movers = working.groupby('Prime Mover')
    capacities = prime_movers.sum()
    print capacities['Nameplate Capacity (MW)']

From here, we can start graphing. First, we’ll make a hideous bar chart with a
lengthy line of code.

    plt.bar(range(len(capacities['Nameplate Capacity (MW)'])), capacities['Nameplate Capacity (MW)'])

    plt.savefig('ugly bar.png')

This generates a hideous, non-informative bar chart, then saves it to your
working directory as a .png. The graph is below:

![](https://cdn-images-1.medium.com/max/800/1*v7fppj6br1UnJbuYNS4zeQ.png)

Ok, so there are a few things to be done to the graph, but first, I want to
shorten the plotting line. This is more of a personal preference on my part, but
I don’t like calling into the dataframe while graphing. Rather, I like to
declare what I’ll be graphing beforehand because it feels better
organizationally in my mind.

    pm_caps = capacities['Nameplate Capacity (MW)']

    plt.bar(range(len(pm_caps)), pm_caps)

Some people might be wondering about that range(len(pm_caps)) thing. Due to the
way matplotlib generates a bar chart, you need to feed it the actual values
along with a length for the chart. The easiest way to auto-size it is to get the
range of the length of the data you’re graphing.

Now we’re going to add information to the graph.

    pm_list = sorted(set(list(working['Prime Mover'])))

    plt.bar(range(len(pm_caps)), pm_caps)
    plt.xlabel('Prime Mover')
    plt.ylabel('MW')
    plt.title('Sum of Capacities by Prime Movers for 2012 (MW)')
    plt.xticks(range(len(pm_list)), pm_list, rotation = 60)

    plt.savefig('informative ugly bar.png')

![](https://cdn-images-1.medium.com/max/800/1*2b4rIWDP1VOsQuWU2IyasA.png)

So now I’ve got some labels, a title, and labeled tick marks, but it’s still not
a looker. Part of that is the large numbers on the y-axis. It would be pretty
easy to convert those MWs into GWs, but I’ll leave it up to you to figure out.
Additionally, this data just doesn’t look that great in this format; there’s an
incredible spread. Flywheels are barely above 20 MW, while steam turbines are
edging 570,000 MW. Often you might take the log of everything to get the data on
a manageable scale, but is there even value in comparing steam turbines and
hydropower to flywheels or batteries? In this case, the answer is probably not.
These technologies not only have vastly different levels of deployment, but they
fill different roles in our energy infrastructure as well.

That bar chart is also static. Perhaps a better way to show the different prime
movers is in their deployment over time. We want the column ‘Operating Year’,
but let’s focus in even further and restrict it to the past 20 years (1993–2012
since this data only goes through 2012). We can also bring Alaska and Hawaii
back in (although if you were curious and re-made the above bar chart with them
in you would have seen that the change was basically imperceptible). Finally,
we’ll only look at renewables. Since we’re looking at the last 20 years, that’s
where the most change is going to show up. First, we’ll separate out the data
for different prime mover groups. One way to do this is successive filtering of
each Prime Mover

    renewables = working[working['PrimeMover'] != 'ST']
    renewables = renewables[renewables['Prime Mover'] != 'BA']

And so on, down the line of all the non-renewable prime movers. A different way
to tackle this is generating lists of different groups beforehand.

    renewables = ['HA', 'HB', 'HK', 'PV', 'WT', 'WS', 'FC']
    traditional = ['ST', 'GT', 'IC', 'CA', 'CT', 'CS', 'CC', 'HY','BT']
    storage = ['BA', 'CE', 'CE', 'FW', 'ES', 'CP', 'PS']

Set up a renewables dataframe

    renew_data = working

Then loop through the traditional generation technologies and pull them out of
the data:

    for tech in traditional:
        renew_data = renew_data[renew_data['Prime Mover'] != tech]

Storage is still in there, but I bet you can figure out how to pull those out as
well. My grouping itself might also seem a bit suspect at first glance. I
separated the different hydropower technologies based on the way they are
treated in national green energy programs. Generally hydrokinetic and wave-based
technologies have full approval, while traditional hydropower operations face a
bevy of restrictions. That’s also why it’s traditional, and not fossil fuels.
Even if I did want to create a fossil fuels filter, geothermal and nuclear steam
plants would fall into the group if you’re using prime movers. There are other
ways in the data to identify different types of plants (such as fuel type), but
we’ll stick with prime movers for now. The goal is for this code to be easily
modified to accommodate for different filtering ideas later on.

So now the code gets a little more complicated, as a couple loops are thrown in:

    capacities = pd.DataFrame(columns = renewables)
    year = 1992
    years = range(1992, 2013
    i = 0

    for year in range (1992, 2013):
        current_year = renew_data['Operating Year'] == year]
        
        for tech in renewables:        
            cap_add = current_year[current_year['Prime Mover'] == tech]
            capacity = cap_add['Nameplate Capacity (MW)'].sum()
            capacities.loc[i, tech] = capacity

        year = year + 1
        i = i + 1

Breaking it down in order, I’m:

1.  Creating an empty dataframe whose headers are the renewable energy prime movers.
1.  Defining my starting year.
1.  Defining my range of years.
1.  Setting up i for the loop.
1.  Initialize the main loop to go through the years.
1.  Restrict the data to the year I want.
1.  Initialize an inner loop to calculate the capacities for each technology.
1.  Restrict the data to a single technology.
1.  Sum the capacity added for that technology in that year.
1.  Place that calculated value into the formerly empty dataframe.
1.  Step back out and add 1 to the year to move forward, and add 1 to i, so that the
next set of annual capacities is written into the next row of the dataframe.

If you print the new dataframe, you might think something’s broken. HA, HB, HK,
and WS all show goose eggs for the entire 20 year period. Nothing’s actually
wrong, it’s just that no generators for any of those technologies reached the
size threshold fore reporting over that 20 year span. More specifically,
offshore wind has been delayed by permitting/NIMBY-ism, and the new hydro
technologies are still being developed. Until recently, most in-the-field
set-ups were pilot demonstrations. Before we get to some graphs, let’s get rid
of those technologies:

    capacities = capacities.drop(['HA', 'HB', 'HK', 'WS'], 1)

At this point, we can make some graphs. This first chunk of code will loop
through the 3 remaining technologies, plotting, labeling, and saving individual
graphs.

    x = range (0, 21)
    years = list(years)
    for tech in renew_tech:
        plt.plot(x, capacities[tech], linewidth = 2)
        plt.title(tech + ': 20 Years of Capacity Additions')
        plt.xticks(x, years, rotation = 60)
        plt.ylabel('MW')
        plt.xlabel('Year')    
            
        plt.savefig(tech + '.png', bbox_inches = 'tight')
        plt.close()

These graphs look like this:

![](https://cdn-images-1.medium.com/max/800/1*nUq1_BAANy48zX67_tXpYw.png)

That’s fine and all, but why not condense everything into a single graph?

    for tech in renew_tech:
    plt.plot(x, capacities[tech], linewidth = 2, label = tech)
        plt.title('20 Years of Renewable Capacity Additions')
        plt.xticks(x, years, rotation = 60)
        plt.ylabel('MW')
        plt.xlabel('Year')
    plt.legend(loc = 2)        
    plt.savefig('20 Years of Renewable Capacity Additions.png', bbox_inches = 'tight')
    plt.close()

The only major change is moving the save and close commands outside of the loop.
Essentially, matplotlib is drawing a new line and resizing the graph as required
with each successive loop. I also added a legend, which relies on the new label
argument in the plot command.

![](https://cdn-images-1.medium.com/max/800/1*Y3eW5V8PQOSpQ2A1gUeX2g.png)

We can also dial it back to generate the same graph for traditional generation.
Just change a few variable names and you’re done:

![](https://cdn-images-1.medium.com/max/800/1*GqdU6LYv3NR5b8SVvDayAw.png)

If you’re going to be doing a bunch of graphing, it would be even easier to
throw the whole thing in a loop, and just choose your groups on the outside. One
way to do this would be to append a few columns to the initial dataframe with ID
numbers based on whatever grouping scheme you want.

This was really just scratching the surface of how you can peer into and graph a
federal dataset without ever opening Excel. There‘s a boatload of powerful
scientific and graphing Python functionality out there, and if you’re just
starting out, I hope this adequately demonstrates some basics. Next time I’ll
dig back into an energy topic and focus less on the coding side of things. Now
that the 2013 data is out, it’s time to analyze some trends.

Again, like I said at the top, [all of this is avialable on GitHub if you are so
inclined](https://github.com/cwaldoch/EIA_860).

