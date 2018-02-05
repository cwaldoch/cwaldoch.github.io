# Breaking down FERC docket metadata with Python

### The DOE’s Resiliency NOPR

A few weeks ago the Department of Energy [suddenly dropped a NOPR on the
world](https://www.federalregister.gov/documents/2017/10/10/2017-21396/grid-resiliency-pricing-rule).
This notice of proposed rulemaking (NOPR is much easier to say, although it’s
more like a maybe-er) has possibly very large implications for the deregulated
energy markets as they currently exist. Rather than addressing the specifics of
this rule and its potential implications (which I am also interested in, but
have a professional entanglement in that the company I currently work for is
intimately involved in the markets and did in fact file comments, which can be
[found at this page](https://www.potomaceconomics.com/document-library/)), I’m
going to show off a quick and dirty way to assess the general character of the
comments using Python.

Also, the code and other things presented here can be found [on
github.](https://github.com/cwaldoch/DOE_Resiliency_NOPR)

### Webscraping

Typically you have to get a bit dirty when pulling straight text from a webpage.
Figuring out what you want, and where to pull it from is often assisted by a
package like beautifulsoup, which is excellent at parsing the mess (or soup) of
HTML into something more manageable. When you’re feeling friskier or need some
interaction with a webpage you can turn to selenium or mechanize to power
through forms (which I actually did for the FERC eLibrary at a past job to pull
down every hydropower permit they had on file). In this case, we can be **very
**lazy.

1.  Navigate to:
[https://elibrary.ferc.gov/idmws/docket_search.asp](https://elibrary.ferc.gov/idmws/docket_search.asp)
This page might currently be broken via direct link, so you can also go here and
then click on “Docket Search”: https://www.ferc.gov/docs-filing/elibrary.asp
1.  Type in “RM18–1" for the docket and hit submit
1.  Once loaded, right click on the page and choose “View Source”
1.  On that page hit ctrl+a then ctrl+c
1.  Open a notepad window and hit ctrl+v
1.  Makesure that the filetype in the drop down below the filename is set to All
Files (*.*)
1.  Save the file with anything for a name, but for convenience “filings.html” will
work, the “.html” part is important
1.  Congratulations, you have webscraped!

Now that we’ve lost the throngs of DC staffers who opened a new tab to add
“Webscraping” to their LinkedIn profiles let’s get down to the more interesting
and useful part.

### Python

First, get Python! Now, there are a lot of ways to do this, but for our use
there are two pretty much equally easy paths, although one takes longer than the
other. If you’re really unsure about this whole Python thing and commitment to
actually installing something is just not your bag, then WinPython is for you.
Download the appropriate version for you from [this
page](http://winpython.github.io/) (if you’re uncertain, go for the highest
version number and 64-bit). WinPython keeps to itself, and will simply place a
folder full of Python goodness wherever you direct it. It doesn’t take over
other installations you might have, but it also won’t be defaulted to for
anything either. If you want a slightly more involved actual installation (or
you’re on a Mac, which the “Win” might have given away), then I would turn to
Anaconda, [found here](https://www.anaconda.com/download/). Anaconda and
WinPython include mostly the same interfaces you might code with and many of the
same packages, but Anaconda installs and registers itself to your actual
computer. It also is backed by a larger organization with broader goals, which
you can read about on their site. Again, go for the Python 3 download.

Either way, once you’ve acquired one of these Python installations you should
see something called “Spyder” either in your installed programs or as an icon in
the WinPython folder. Spyder is where we’ll be writing and viewing the Python
code. I like Spyder because it was modeled around the kind of interface you see
in Matlab, which means conveniences such as variable viewing. A lot of python
data/science “messin’ around” development also happens in Jupyter notebooks
these days, but for now we’ll stick with Spyder.

First things first, hit the save button and navigate to wherever you places the
“filings.html” file. This will make sure you have data and code in the same
place and keep us from any problems around filepaths. You can name the file
whatever you like, but something whose purpose you’ll remember when staring at a
file directory later is typically good practice.

### Coding in Python

So, finally, let’s write some code, starting with the key package, pandas!

    import pandas as pd

Import functions begin any python script that is using more than the very basic
nuts and bolts in Python. In this case, we’ll be using the uber popular pandas
library. This command tells your current script to grab all of the pandas code
to be used, and to use the pseudonym “pd” to refer to pandas and call it’s
functions. Instead of writing out pandas.read_csv, you can use pd.read_csv,
saving some characters.

The next line of code uses some of that built-in pandas functionality to save us
from having to do a lot of messy HTML parsing.

    dfList = pd.read_html('filings.html')

This reads the HTML file we saved earlier (via manual webscraping), and returns
a list of all the tables embedded in that page as DataFrames. DataFrames are a
type of data structure used in pandas that you can think of as an Excel sheet in
code form. It returns a list, because in this page there were multiple tables,
so it puts them all into a generic Python data structure called a list. Lists
are exactly what they sound like, a list of things. In this case, I already know
that there are 4 tables in the HTML (and therefore 4 DataFrames), but if you
wanted to check for yourself, you could write:

    len(dfList)

To access items inside something else in Python you can often use indexing.
Indexing is generically simple with the possibility of being extremely
complicated. In this case, you simply append a number in brackets to the end of
an object, to return what was in that space in the larger data structure, in
this case the dfList. At this point, it’s important to mention that code starts
counting at 0, so while the len command above returned 4, the indices, or
locations of the objects in the list are:

    dfList[0]
    dfList[1]
    dfList[2]
    dfList[3]

You can mess around with the other objects if you want, but let’s move on right
to the table we want, #4. Each item in that list is an HTML table that has been
converted into a DataFrame, the pandas Excel sheet-like data object. To get the
one we want is simple:

    dfComments = dfList[3]

Now you have a DataFrame of all the information on the filings, but it’s not
sorted very usefully at all. In fact, I think it’s kind of a junky format with a
large number of “nan” values (which stands originally for “not a number”, but
has morphed into a bit of a catch-all in certain areas for values that just
aren’t). To convert it to something more palatable I looked at what was common
to each participant’s set of information and wrote a dirty little loop to
maintain the order, strip the non-existent values, and spit out something that
fits with what I had in mind for analysis:

    results = []
    for x, row in dfComments.iterrows():
       i = 0
       if row[0] == ‘Filed By:’:
           filer = row[1]
       if row[0] == ‘Filed Date:’:
           date = row[1] 
       if row[0] == ‘Accession No:’:
           accNo = row[1]
       if row[0] == ‘Description:’:
           desc = row[1]
           i = 1
       if i == 1:
           results.append([filer, date, accNo, desc]) 
           print(filer)

First, I’m creating an empty list named “results”, then I’m looping through the
dfComments DataFrame, one row at a time. From examining the data through some
exploratory queries (or just looking at it in Spyder’s variable viewer) I saw a
pattern in it structure to exploit. Each row starts with the name of what I
eventually want to be a column in my final DataFrame. and the second column’s
value is, well, the value (such as filing date or filer name). This code strips
out those values, and layers them on top of each other in individual lists, that
keep getting appended to “results”, which becomes a list of lists.

Each if statement checks to see if the first row value is a type I want, and if
it is takes the second value and makes it a variable to be appended to a results
list. Whenever i is equal to 1 a list of values is appended to the results. In
this case I can just do that because the style is standardized so that each list
of information on a filing ends with “Description”, you might not always be so
lucky, but time around it let me roll with a simple, inefficient structure. From
here, back outside of the loop, you can use another pandas function to construct
an entirely new DataFrame:

    dfFormatted = pd.DataFrame(results, columns = [‘Filer’, ‘Date’, ‘Accession No.’, ‘Description’])

This relies on the structure we built up inside of the loop. Imagine each list
of values being stacked on top of the previous list, like the floors of a
skyscraper. Now, we’re dividing the skyscraper at pre-determined intervals into
columns. Now, we have something that looks a lot easier to work with, much
closer to the traditional Excel Worksheet you might be familiar with. At this
point, you might want to save your work so that you don’t have to process the
HTML and resulting messy DataFrame again.

    dfFormatted.to_csv(’formatted_results.csv’)
    dfFormatted = pd.read_csv(’formatted_results.csv’)

This does exactly what it looks like. The first line saves the dataframe as a
csv file, the second line reopens the saved file back up as a dataframe. There
are a number of “to” and “Read” commands in pandas (like excel or sas7bdat), so
I recommend reading the documentation to find what works best for you.
Personally, I prefer the speed and no-nonsense attitude of csv files, they’re
basically 90s Sonic the Hedgehog in excel-accessible data structure form.

Moving on, let’s take a look at our newly styled data.

    uFilers = list(set(dfFormatted[‘Filer’]))
    uLFilers = [str.lower(x) for x in uFilers]

Both of these lines use built-in Python functionality. The first gets a list of
the set of the values in the “Filer” column of our dfFormatted DataFrame. A set
in Python is an ephemeral result that gets the unique values out of some other
list of data. It’s wrapped in list in order to return a workable object for the
next line. The second lined is a loop that uses the built-in “lower” function of
the str package in Python to convert all the letters in all the filer’s names to
lowercase. Unlike above, this loop isn’t nested over multiple lines of codes,
but uses a neat feature of Python called a list comprehension. List
comprehensions allow you to execute loop-like tasks on all the objects with a
list in a single line of code. Now for the reason we even bothered:

    nukeFilers = []
    for filingName in uLFilers:
       if ‘nuclear’ in filingName or 'uranium' in filingName::
           nukeFilers.append(filingName)

Like above we’re using a for loop and initializing a list pre-loop to store
results. This loop goes through each filing name in the list of unique
lowercased filing names and searches for the strings “nuclear” and “uranium”. If
either of those words is in the filer’s name, they’re appended to the nukeFilers
list. The reason we lowercased all of the filer names is because case counts in
Python, and we needed to standardize all of the letters to make the search for
specific strings easier. In this case, you get 14 entires in the nukeFilers list
(individual entries are comma separated and surrounded by ‘ in lists):

    [‘entergy services, inc. entergy services, inc. entergy arkansas, inc. entergy arkansas, inc. entergy louisiana, llc entergy louisiana, llc entergy mississippi, inc. entergy mississippi, inc. entergy new orleans, inc. entergy new orleans, inc. entergy texas, inc. entergy texas, inc. entergy nuclear power marketing, llc entergy nuclear power marketing, llc’,
     ‘nuclear energy institute’,
     ‘american nuclear society’,
     ‘uranium producers of america’,
     ‘american nuclear society american nuclear society’,
     ‘u.s. nuclear infrastructure council’,
     ‘nuclear matters’,
     ‘nuclear information & resource service’,
     ‘nuclear information and resource service’,
     ‘uranium energy corp’,
     “toledo coalition for safe energy don’t waste michigan beyond nuclear citizens for alternatives to chemical contamination”,
     ‘nuclear energy information service’,
     ‘u.s. women in nuclear’,
     ‘north american young generation in nuclear’]

Some of these groups are pro-nuclear, at least 1 is anti-nuclear, and Entergy
was only captured here via luck (although they do own nuclear generation
stations). So, to some extent, this shows the limits of a simple text scrape.
Without additional domain-specific knowledge you just get a list of phrases that
contained the words nuclear or uranium. Heck, you might have not even considered
the potential stake of uranium-based businesses if you were only thinking at the
broad power plant technology level. Despite that, I hope this was a useful look
into how you can break things down. More advanced techniques would use [nltk
](http://www.nltk.org/)and dictionaries of common words and punctuation. You
could also start with a list of companies and parse if they’re present.

### One More Thing

As a little bonus, here’s two graphs of filings by day. [Code for these, and
everything else can be found on
GitHub.](https://github.com/cwaldoch/DOE_Resiliency_NOPR)

![](https://cdn-images-1.medium.com/max/800/1*wqbQcIIk3k-dszvN7ninRA.png)

![](https://cdn-images-1.medium.com/max/800/1*0G2z1r2ZqzlCuLQFvPpNvw.png)


