1 cosa:

trasformare i file in csv
* guardare come funziona libreria Pandas e come installarla/utilizzarla
- removing missing values and filtering rows or columns by some criteria
- Store the cleaned, transformed data back into a CSV, other file or database

_________________________________________________________________________________________________
https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
python -m pip install pyperclip
cd C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts
pip install pandas

 The script f2py.exe is installed in 'C:\Users\Juliana\AppData\Roaming\Python\Python37\Scripts'
 You should consider upgrading via the 'c:\program files (x86)\microsoft visual studio\shared\python37_64\python.exe -m pip install --upgrade pip' command.
https://data-flair.training/blogs/install-pandas-on-windows/

https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
import pandas as pd
_____________________________________________________________________________________________________

There are many ways to create a DataFrame from scratch, but a great option is to just use a simple dict.

Reading data from CSVs
With CSV files all you need is a single line to load in the data:

df = pd.read_csv('purchases.csv')

df_xlsx = pd.read_excel ('..\Dati_Originali_Prof\Tag 710333A 20 Sept.xlsx') 
mettere i tipo di file e dove lo trova

As noted in the docs for DataFrame.to_csv(), simply pass index=False as a 
keyword argument to not write row names.
df.to_csv('file_name.csv', index=False)

ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or p to install xlrd.
c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64>python.exe -m pip install xlrd

Successfully installed xlrd-1.2.0
WARNING: You are using pip version 20.1.1; however, version 20.2.3 is available.
You should consider upgrading via the 'c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe -m pip install --upgrade pip' command.
_____________________________________________________________________

df = pd.read_csv('Tag_710333A_20_Sept.csv')
print (df.head)

when I printed, there were some others data before the columns' titles
headers row = 23

## read headers 
df.columns

## read each column
df['Name']
would you like the top 5 names = df['Name'][0:5]
if you would like more than 3 or 3 in specific, no even in the ordem, you do, for example:
df[['Name','Type 1', 'HP']]

## read each row
if i would like everything in the row 2 of the data I'd use: (the tiles dont count)
df.iloc[1]
-- loop to get data in each row
for index, row in df.iterrows():
print(index, row) 
or print(index, row['name'])

to give me an specific location of one specific word, use:
df.loc[df['Type 1'] == "Fire"]
for example, and each row that contains Fire into the column Type 1, will show.
for two conditional with that:
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
only gives me the lines wich have grass and poison
"and" for pandas is "&"
"or" for pandas is "|"
this show either a line wich contains both values, or only one of them, example that contains poison, but no grass
I can also specifies conditionals like that:
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

Filter your data:
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
thats maintain your df with all the data, and you also have now a new_df with that filtered data.
to save that as a new file:
new_df.to_csv('filtered.csv')
even though I filtered my new data, the index of the old data remains, 
so if you wanna reset your index:
new_df = new_df.reset_index() and by defaut it saves your old index as a new column to the right of the reseted index
if you dont want that:
new_df = new_df.reset_index(drop=true)
and if you dont wanna to reset that to a new dataframe new_df =, you can:
new_df.reset_index(drop=True, inplace=True)

so resuming:
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.to_csv('filtered.csv')
new_df.reset_index(drop=True, inplace=True)


## read a specific location (R,C)
if i want a specific row and column location, I use:
df.iloc[2,1] for example, where 2 is the second line of the data (dont count the title) and 1 is the second column (counting 0 and 1)

https://www.youtube.com/watch?v=vmEHCJofslg

df.describe()

alfabetical order:
df.sort_values('Name')
alfabetical descending order:
df.sort_values('Name', ascending=False)

using two values:
df.sort_values(['Type 1', 'HP'])
it will give me in alfabetical order the type 1 and the hp in number will be the lower number first.
ascending and descending with 2 values, i use this:
ascending = false #will change both 
ascending =[1,0] #will maintain the first one as ascending, and the second one as descending.

create new column, named as Total, for example:
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']

create a new column Total, in a more succinct way:
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
: means all the line
4:10 means that I will skip the columns 0,1,2 and 3. Starting from 4 (count that) 
to 10 (dont counting that, stopping counting at the 9 column, wich I want include the value)
I do not count column 10
.sum is the sum of the values of all that columns
axis=1 means if you are adding horizontaly (1) or verticaly (0)

to put that new column Total, now in the last column to the 5th column(counting from 0), I grab specifics columns:
df[['Total', 'HP', 'Defense']] in wherever order I want,
so if I want to reorder my columns, and save it afterwards:
df = df[['Total', 'HP', 'Defense']] #in wherever order I choose
if annoys you retype always the order of the columns, you can use:
cols = list(df.columns.values)
so the results of puting that last column in place is:
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

to eliminate a column Total, for example, use drop:
df = df.drop(columns=['Total'])

string contains:
if in my data a have some names writing like this example "CharizardMega", "BeedrillMega" etc.
and I want to eliminate that Mega in those names, I can not use == signal, because contain is not = to something
remember the contains function, inside the string, so:
df.loc[df['Name'].str.contains('Mega')]
that shows me all the lines that Mega is in it.
the invert of this, use the "!" means not, 
but "!" in pandas is "~"
df.loc[~df['Name'].str.contains('Mega')]

Using this I can use another function,
let's say I want to know in the column Type 1, wich lines contains the word Fire or Grass
to do this I need to import "regular expressions"
super powerful in filtering data
import re
df.loc[df['Type 1'].str.contains('fire|grass', regex=True)]
if it doenst work, make sure the words fire and grass in the file were written in uppercase, if so:
df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
another way to writ in lowercase and it be read is:
df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
this will be ignoring case

another function with contains:
... continue the video



____________________________________________________________________________
https://www.kite.com/python/answers/how-to-convert-a-pandas-dataframe-row-to-column-headers-in-python
Assign row as column headers
example:
header_row = 23
df.columns = df.iloc[header_row]

https://chrisalbon.com/python/data_wrangling/pandas_rename_column_headers/
# Create a new variable called 'header' from the first row of the dataset:
header = df.iloc[0]
# Replace the dataframe with a new one which does not contain the first row
df = df[1:]
# Rename the dataframe's column values with the header variable
df.rename(columns = header)

my header_row in the prof's file, is writen as 23, but dont counting the header and the first data line as 0,
my header was realy number 21

header_row = df.iloc[21]
to continuous reading after that:
df = df[22:]
to inpu that 21 line as my header:
df.columns = header_row
df.reset_index(drop=True, inplace=True)
but the line had a name from the old line file, named as 21
to change that:
header_row.name = ''


_____________________________________________15/10/2020
-open prompt dei comandi (cmd)
-cd C:\Users\Juliana\Desktop\inicio_tcc\Materiale_Tirocinio_Prof_Luschi\Scripts
- py script1.py

____________________________________________________________________________
download numpy:
open prompt dei comandi (cmd)
cd
c:\program files (x86)\microsoft visual studio\shared\python37_64\py -m pip install

Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: numpy in c:\users\juliana\appdata\roaming\python\python37\site-packages (1.19.2)
WARNING: You are using pip version 20.1.1; however, version 20.2.3 is available.
You should consider upgrading via the 'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe -m pip install --upgrade pip' command.
_________________________________________________________________________________________________
pandas to loop through DataFrames and keep only specified column headings
https://stackoverflow.com/questions/37865007/pandas-to-loop-through-dataframes-and-keep-only-specified-column-headings-error

delete columns based in a conditional
https://stackoverflow.com/questions/13851535/delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression-involving

https://stackoverflow.com/questions/15703283/pandas-drop-a-range-of-rows-from-df
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
https://www.marsja.se/how-to-get-the-column-names-from-a-pandas-dataframe-print-and-list/
______________________________________________________________--

-imparare creare colonne
imparare a convertire coordinate geografiche in python, from 4326 to 3857

install pyproj:
C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64>py -m pip install pyproj
https://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/
# Define some common projections using EPSG codes 
wgs84=pyproj.CRS("EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth 
OR:
# Define a projection with Proj4 notation, in this case an Icelandic grid 
isn2004=pyproj.CRS("+proj=lcc +lat_1=64.25 +lat_2=65.75 +lat_0=65 +lon_0=-19 +x_0=1700000 +y_0=300000 +no_defs +a=6378137 +rf=298.257222101 +to_meter=1") 
_________________________________________________________________________________________________

https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
Don't drop, just take the rows where EPS is not NA:
df = df[df['EPS'].notna()]
Drop the rows that are NaN:
df.drop(df[~df['GPS Latitude'].notna()].index, inplace=True) # drop the rows that are null (NaN) from dataframe

Convert Select Columns in Pandas Dataframe to Numpy Array
https://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array
s_array = df[["A", "B", "C"]].to_numpy()
s_array


____________________________________________________________
https://stackoverflow.com/questions/44446862/calculate-distance-between-latitude-and-longitude-in-dataframe
I'd recommend you use pyproj instead of geopy. geopy relies on online services whereas pyproj is local (meaning it will be faster and won't rely on an internet connection) and more transparent about its methods (see here for instance), which are based on the Proj4 codebase that underlies essentially all open-source GIS software and, probably, many of the web services you'd use.

#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pyproj import Geod

###### question. why this coordinates in degree?
wgs84_geod = Geod(ellps='WGS84') #Distance will be measured on this ellipsoid - more accurate than a spherical method

#Get distance between pairs of lat-lon points
def Distance(lat1,lon1,lat2,lon2):
  az12,az21,dist = wgs84_geod.inv(lon1,lat1,lon2,lat2) #Yes, this order is correct
  return dist

#Create test data
lat1 = np.random.uniform(-90,90,100)
lon1 = np.random.uniform(-180,180,100)
lat2 = np.random.uniform(-90,90,100)
lon2 = np.random.uniform(-180,180,100)

#Package as a dataframe
df = pd.DataFrame({'lat1':lat1,'lon1':lon1,'lat2':lat2,'lon2':lon2})

#Add/update a column to the data frame with the distances (in metres)
df['dist'] = Distance(df['lat1'].tolist(),df['lon1'].tolist(),df['lat2'].tolist(),df['lon2'].tolist())
PyProj has some documentation here.


____________________________________________________________________________
calculate velocity between two points, first put the time in string

https://gis.stackexchange.com/questions/333928/calculate-velocity-and-errors-from-distance-between-gps-points

calculate datetime in seconds:
https://stackoverflow.com/questions/19801727/convert-datetime-to-unix-timestamp-and-convert-it-back-in-python
https://docs.python.org/3.3/library/datetime.html#datetime.datetime.timestamp


Converting Strings to Dates as datetime Objects
https://stackabuse.com/converting-strings-to-datetime-in-python/
date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f') #change the '-' to '.'
# Datetime 
acquisition_times = df[['Acquisition Time']].to_numpy()
date_time_str = '2020.07.09 23:00:09'
date_time_obj = dt.datetime.strptime(date_time_str, '%Y.%m.%d %H:%M:%S')
print(date_time_obj)

#datetime = dt()

_________________________________________________________________________________________________
with the distance, calculate the speed, using the time 

#calculate the velocity
#v= d/t
#v = Length/ Second2 - second1

speeds =np.empty([len(unixDates)], dtype=np.float)

i = 0
while i < len(unixDates)-1:
	speeds[i] = (distances[i] / (unixDates[i+1] - unixDates[i]))
	i += 1

df['Average Speed'] = speeds
df.to_csv('GPS_Data_333A_Sept_Speeds.csv', index=False)
print(df)
_________________________________________________________________________________________________
now, the maximum speed is 4km/h, converting in m/s is 1,1111
so, when the turtle reach the speed > than 1,1111m/s is because the next point is out 
so, we need to make a expression that eliminate the next point of a exceeded speed.

+/-
df
speeds
indicesToRemove = LISTA
while i < len(acquisitionTime)
    next = i+1
    S = 100
    while (S > 1.1) and (next < len(acquiostionTime) - 1) 
        D = CalcolaDistanza(i,next)
        S = CalcolaVelocità(D,i,netx)
        if(S > 1.1)
            indicesToRemove.append(next)
        next+=1
    speeds=S

for indice in indicesToRemove
    df.dropline(indice)

df['VELOCITà'] = speedsdf
speeds
indicesToRemove = LISTA
while i < len(acquisitionTime)
    next = i+1
    S = 100
    while (S > 1.1) and (next < len(acquiostionTime) - 1) 
        D = CalcolaDistanza(i,next)
        S = CalcolaVelocità(D,i,netx)
        if(S > 1.1)
            indicesToRemove.append(next)
        next+=1
    speeds=S

for indice in indicesToRemove
    df.dropline(indice)

df['VELOCITà'] = speeds




