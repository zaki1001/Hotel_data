# Thomas_Hotel_data


**Requirements**

The scripts would work on both Python 3.x and 2.x

You need to install the following repositories:

Pip install numpy

Pip install pandas

Pip install inflect

Pip install datetime

Pip install regex

# Instructions

**Download everything in a folder on you computer, then put the booking report file in that  folder.**

First run the **hotelbig.py** script to generate the hotel\_big\_data.csv empty csv

Just put the booking report in the folder in which you keep all the scripts, then run the **hotelbig.py** script and this will create a new empty hotelbigdata csv which will be used by the later scripts.

Next run the **hotel\_big\_data.py** script which will update/populate the hotel big data.csv

Then run the **lowhighthomas.py** script. This is where you start entering the weeks for low season and high season.

It will ask you the following question:

**Please Begin Entering The Low Season WeekNumber...Hit Y to Continue or N to start entering High Season WeekNumber**

You enter Y to give the weeks for lowseason and hit enter

It will keep asking you for low season weeks, I you want to stop entering low season at any point just enter N to start giving weeks for High Season

Which will then ask the following question:

**Please Begin Entering The High Season WeekNumber...Hit Y to Continue  N to end**

Now give the weeks for High Season and when you are done enter N to generate the HighSeason.csv and LowSeason.csv

Finally run the **removedates\_median.py**

This script is used to remove any dates from the system and/or its attributes

It will first ask you this:

**Which season you want to remove dates from? Enter No to stop.**

Here enter the Season from which  you want the dates to removed for ex:High

Or enter No to not remove any dates and directly calculate the 3/4 median

If you entered HIgh or low then it will ask:

**Which Arrival Status you want to remove it from**

Here you enter the Arrival Status you want to remove, which are : same,one,two,three,four,five,six,seve,one week,two week and remaining .

It uses Regular Expression so dont mind the short form or wrong spellings(Its better to use the phrases i used above)

Then its asks for date to be removed:

**Which Dates data you want removed?mm/dd/yyyy**

Note the format of the date.

When you are done removing dates just enter No when its asks this:

**Which season you want to remove dates from? Enter No to stop.**

Finally it will calculate the 3/4 median and the results will be in the csv file:

LowSeasonMedian.csv and HighSeasonMedian.csv
