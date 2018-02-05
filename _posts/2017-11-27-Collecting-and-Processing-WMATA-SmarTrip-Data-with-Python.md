# Collecting and Processing WMATA SmarTrip Use History with Python

### Background

Note: [Everything’s on GitHub.](https://github.com/cwal37/scrapeWMATA)

[A recent post at Greater Greater Washington clued me in on the SmartTrip usage
functionality](https://ggwash.org/view/65503/whens-the-last-time-you-checked-your-metro-on-time-score)
on [the WMATA
website](https://smartrip.wmata.com/Account/AccountLogin.aspx?ReturnUrl=/). If
you’ve associated a SmartTrip card with an account, you can get recent on-time
statistics as well as a complete history of that card’s usage (since the data
portal launched in October, 2015). While that’s nice and all, it is a bit
annoying to get the detailed data. Specifically, you can only query 31 days of
data at a time. Before I realized that inconvenience I was already planning on
writing a script to pull my data just for funsies/practice. With that stumbling
block, the coding gets more fun and the end result is more useful. How do you
get to the stuff?

First click on your card

![](https://cdn-images-1.medium.com/max/800/1*pA_1Hkk3AuNY5kuqS6SLuQ.png)

Then click on Use History on the right

![](https://cdn-images-1.medium.com/max/800/1*nXFw8uKPODLw7JWwW96HMw.png)

Now you can simply enter up to 31-day date ranges and get whatever usage that
SmarTip card incurred.

As you click through the site, you might notice the URL changing in helpful
ways, ways that suggest you could just append pieces to it in order to get the
data you’re looking for. This might be the case, but you also still need to log
in, and I haven’t completely verified that functionality. Due to the need to
move around through web pages and submit information I decided to use a
selenium-based approach rather than kludging together an API based around
chopping up the URL. Selenium is a code package with bindings in several
languages that allows you to take control of an automated browser and do
websurf-y things. Not everything in and around selenium always works perfectly,
which can generally be traced somewhere back to the fact that the web itself is
a contradictory mess of disparate implementations.

### Spinning up Code

Thinking this over, there are two distinct functionalities I want. First, a way
to pull down all the data. Second, rolling up all acquired data into a single
file. Let’s start with the data collection.

To begin, we’ll import what we’ll be using in terms of packages.

    import time, datetime
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException

It’s basically just time related things and a few selenium parts. Right off the
bat, there’s a problem. Data goes back to October of 2015, but my card history
doesn’t go back that far. Also, I don’t just know all the 31 days back from now
for over two years. Can’t the code just take care of both issues for me? Yes.
Let’s start with the latter.

    datePairs = []
    dateStart = datetime.strptime('10/1/2015', '%m/%d/%Y')
    while dateStart <= datetime.now():
        print(dateStart)
        datePairs.append([dateStart.strftime('%m/%d/%Y'), (dateStart+timedelta(days=30)).strftime('%m/%d/%Y')])
        dateStart = dateStart + timedelta(days=31)

First, I’m creating an empty list. In my mind I already decided that this list
is going to be filled with tuples of every start and end date pair from October
2015 to whenever now is. This could have also been a list of lists, but tuples
are slightly faster (although that shouldn’t matter with the small list here),
and immutable. There’s no reason to change these dates once they’re
instantiated, so there’s no reason they can’t be immutable.

Next I’m creating the first day, October 1st, 2015. I’m also sticking with the
formatting I know the website uses from testing, denoted here as ‘%m/%d/%Y’,
[this is a helpful cheatsheet for Python’s strftime](http://strftime.org/). Each
tuple is comprised of the current dateStart, and that date + 30 days. Once the
current tuple is appended to the datePairs list, the dateStart has 31 days added
to it and the loop repeats. While the dateStart value is less than or equal to
the current date, this loop repeats.

Important note, the second from the last line is indented, Medium’s code blocks
just struggle with long lines

### On To The Web

    keyValues = open('keyValues.txt')
    keyValues = keyValues.read().split(',')

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : keyValues[0]}
    chromeOptions.add_experimental_option("prefs",prefs)

    baseURL = r'
    driver = webdriver.Chrome(keyValues[1], chrome_options = chromeOptions)

    driver.get(baseURL)

keyValues are my stored download directory, chromedriver.exe location, username
and password. You can just write those directly into your code, or have it pull
from a file as well. I’m pulling from a file since I have the rest of this code
as a public GitHub repo and obviously don’t want that information to be public.
That file is just a .txt file that looks like
“downloadDirectory,chromedriverLocation,username,password”.

Via the chromeOptions functionality of chromedriver I change the default
download directory for the automated webbrowser we’ll be opening. I want the
files in a specific place so that the aggregation code knows where to pick
everything up. I specify a baseURL as the login page, and create the driver
(using the selenium import “webdriver”) with the chromedriver location and that
download directory preference. Finally, I launch the driver, which should open a
browser window.

    userName = keyValues[2]
    passWord = keyValues[3]

    xpathUserName = '//*[
    ="ctl00_ctl00_MainContent_MainContent_txtUsername"]'
    xpathPW = '//*[
    ="ctl00_ctl00_MainContent_MainContent_txtPassword"]'
    xpathRange = '//*[
    ="ctl00_ctl00_MainContent_MainContent_rbByRange"]'
    xpathClickSend = '//*[
    ="right_wide"]/div/div/div/div[1]/p[3]/a'

    driver.find_element_by_xpath(xpathUserName).send_keys(userName)
    driver.find_element_by_xpath(xpathPW).send_keys(passWord)

    xpathSubmit = '//*[
    ="ctl00_ctl00_MainContent_MainContent_btnSubmit"]'
    driver.find_element_by_xpath(xpathSubmit).click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[
    ="left_wide"]/ul/li/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(xpathClickSend).send_keys(Keys.RETURN)
    time.sleep(1)

    driver.find_element_by_xpath(xpathRange).click()
    time.sleep(1)

This code gets the username and password from the keyValues, stores ta number of
relevant xpath values, and then logs into the website with the user credentials
and clicks “submit”. xpaths can be used to navigate throughl XML documents.
Personally, I find them easier to use and more reliable than CSS selectors,
although I feel like I’ve seen a rise in recommendations for the latter over the
last several years. These xpaths are chrome-specific, and would probably come
out differently were you to inspect using a different browser. To find these in
chrome, hit F12 on a page then click on the arrow-in-a-square button in the
upper left of that panel.

Click on anything in the page and it will highlight it in the HTML. From there,
right click -> Copy -> Copy Xpath. The next few lines of code click through the
rest of the remaining pages until we arrive in the location where the data
lives, that bit will require a loop. I have a second’s sleep after each button
press because webbrowsing can be weird and slow. In this case, it’s not really
an issue, but I like to give the website/browser a bit of time to fully load in
order to make sure every element is available to be found and manipulated. You
might also notice that one xpath methods uses send_keys(Keys.RETURN), while the
others just .click(). The click method didn’t work for anything that I used
RETURN on. This is one of those vagaries of the web situations I should probably
more intimately understand, but don’t find to be particularly important or
interesting in this case.

    xpathBack = '//*[
    ="ctl00_ctl00_MainContent_MainContent_btnBack"]'
    xpathstartDate = '//*[
    ="ctl00_ctl00_MainContent_MainContent_txtStartDate"]'
    xpathEndDate = '//*[
    ="ctl00_ctl00_MainContent_MainContent_txtEndDate"]'
    xpathExport = '//*[
    ="ctl00_ctl00_MainContent_MainContent_lnkExport"]'

    i = 0
    for datePair in datePairs:
        if i > 0:
            driver.find_element_by_xpath(xpathBack).send_keys(Keys.RETURN)

    driver.find_element_by_xpath(xpathstartDate).clear()
        driver.find_element_by_xpath(xpathstartDate).send_keys(datePair[0])
        
        driver.find_element_by_xpath(xpathEndDate).clear()
        driver.find_element_by_xpath(xpathEndDate).send_keys(datePair[1])
        
        time.sleep(1)
        # '//*[
    ="ctl00_ctl00_MainContent_MainContent_btnSubmit"]'
        driver.find_element_by_xpath(xpathSubmit).send_keys(Keys.RETURN)

    time.sleep(1)
        try:
            driver.find_element_by_xpath(xpathExport).send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass
        i = 1

    time.sleep(1)
    driver.find_element_by_xpath('//*[
    ="aspnetForm"]/a').send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()

The rest of the code is really just an extension of the above, but with a back
button and looping over all of the datepairs. Here, we’re using send_keys to
send the datePair values as test to the submission form. At the end of the loop
the browser logs out of the website and the webdriver session is killed.

### Data Aggregation

At this point you should have a bunch of loosie csv files wherever you told
chromedriver to deposit them (or in you’re default download directory, in which
case you’ll need to move them, those experimental prefs can be iffy sometimes).

    import pandas as pd
    from os import walk

Here we’re importing pandas, the python data handling superhero, as well as
walk, from os, so we can take a stroll around our local directories.

    fileDirectory = downloadDirectory

    def file_walk(directory):
        file_name_list = []
        for (dirpath, dirnames, filenames) in walk(directory):
            file_name_list.extend(filenames)
            break
        return(file_name_list)
        
    useFiles = file_walk(fileDirectory)

First we’re defining the fileDirectory as whatever your downloadDirectory was,
so replace that with the location of your 31-day files. Next we’re creating a
tiny function to walk through the files and get all the file names from that
directory. This function returns a list of all the filenames in teh directory,
so make sure there aren’t any unwanted files in there. The function is called on
the final line.

    for file in useFiles:
        
        df = pd.read_csv(fileDirectory + '\\' + file)
        if file == useFiles[0]:
            dfResults = df
        else:
            dfTwo = [dfResults, df]
            dfResults = pd.concat(dfTwo, ignore_index = True)
    dfResults.to_csv('results.csv')

The end of this script simply iterates through the filenames in the list, reads
each one in as a pandas DataFrame, and then appends it to the last one. The
first file gets named dfResults, and all the rest get appended to that via the
pd.concat function. Finally, these results are saved to whatever the location of
the script as “results.csv”, you can add a directory in front of the file name
to save it wherever you want.

If you open it in Excel, it should look pretty friendly.

![](https://cdn-images-1.medium.com/max/800/1*NPRNRXJO-YlcbNy5v5ubXA.png)

There are a bunch of fun analyses and visualizations you could make from here,
but I’ll save that for a future post.

