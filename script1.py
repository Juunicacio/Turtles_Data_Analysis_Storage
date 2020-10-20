import pandas as pd
import numpy as np
import pyproj as pj
import datetime as dt

def calculateDistance(geodRef, lat1, lon1, lat2, lon2):
	v1,v2,dist = geodRef.inv(lat1,lon1,lat2,lon2) #Take the second row and the first row on the count. it shoul give 3 values, but I only need the dist.
	return dist #Put the dist inside the distances variable once empty.
	
def convertUnixTimeFromString(timeString):
	return dt.datetime.strptime(timeString, '%Y.%m.%d %H:%M:%S').timestamp() #[i] is the position in an array

def calculateSpeed(d, t1, t2):
	speed = d / (t2 - t1)
	return speed


def main():
	#using excel_original file
	df_xlsx = pd.read_excel('..\Dati_Originali_Prof\Tag 710333A 20 Sept.xlsx')
	df_xlsx.to_csv('Tag_710333A_20_Sept.csv', index=False)

	#use csv_original file
	df = pd.read_csv('Tag_710333A_20_Sept.csv', index_col=False)
	
	#Remove/Change Header --------------------------------------
	#set the line 23 as the header, but counting from 0 on df it's line 21:
	header_row = df.iloc[21] #take row 21
	header_row.name = '' # cancel the index columns to none
	df = df[22:] #filter the satellite informations on the firstlines
	df.drop(df.index[0:21]) #cancel those informations
	df.columns = list(header_row) #set the new header
	df.reset_index(drop=True, inplace=True) #reset index
	#-----------------------------------------------------------
	
	df.to_csv('Dataframe_Overall_Tag_333A_Data.csv', index=False)
	
	#Remove not GPS columns ------------------------------------
	#conditional to control the data:
	GPS_keep_col = list(['Acquisition Time', 'Acquisition Start Time', 'GPS Fix Time', 'GPS Fix Attempt', 'GPS Latitude', 'GPS Longitude'])

	for c in df.columns: 
		if c not in GPS_keep_col: 
			df.drop(c, inplace=True, axis=1)
		else:
			GPS_keep_col.remove(c)
			
	if GPS_keep_col:
		print("Data missing!")
	#-----------------------------------------------------------
	
	#Prepare Geod Object for Calculations ----------------------
	#Geod is used as objec to calculate distances between points expressed in lat/lon (in degree)
	wgs84_geod = pj.Geod(ellps='WGS84') #Distance will be measured on this ellipsoid - more accurate than a spherical method	
	#-----------------------------------------------------------
	
	#Start business --------------------------------------------
	# drop the rows that are null (NaN) from dataframe in the GPS Latitude / GPS Longitude columns
	df.drop(df[~df['GPS Latitude'].notna()].index, inplace=True) 

	#create an array with all the elements that are inside that column #Convert the DataFrame to a NumPy array.
	latitudes = df[['GPS Latitude']].to_numpy() 
	longitudes = df[['GPS Longitude']].to_numpy()
	
	#create an array with all the elements that are inside that column #the elements in that column are in str format. later on I'll need to change it.
	acquisitionTimes = df[['Acquisition Time']].to_numpy() 
	#-----------------------------------------------------------
	
	#Speeds holds
	speeds = [] #empty list
	indicesTimeToRemove = [] #empty list
	i=0
	while i < (len(latitudes)-1):
		foundS = False
		next = i+1
		S = 100
		#while----
		while (S > 1.111) and (next < len(latitudes)):
			D = calculateDistance(wgs84_geod,latitudes[i],longitudes[i],latitudes[next],longitudes[next])
			t1 = convertUnixTimeFromString(acquisitionTimes[i,0])
			t2 = convertUnixTimeFromString(acquisitionTimes[next,0])
			S = calculateSpeed(D,t1,t2)
#			print('D:'+str(D))
#			print('t1:' + acquisitionTimes[i,0] + ' | t2:'+acquisitionTimes[next,0])
#			print('SPEED:' + str(S))
			if(S > 1.111):
				indicesTimeToRemove.append(acquisitionTimes[next,0])
				print('-----------------------')
				print('Point to remove - INDEX '+ str(next))
				print('TIME: '+ acquisitionTimes[next,0])
				print('SPEED: '+ str(S))
			else:
				foundS = True
			next+=1
		#---------
		if(foundS):
			speeds.append(S)
		i=next-1
	speeds.append(0)
		
	df.drop(df[df['Acquisition Time'].isin(indicesTimeToRemove)].index, inplace=True) 
	df['Average Speed m/s'] = speeds
	df['Average Speed m/s'] = df['Average Speed m/s'].str[0] #remove the brackets of the values in the column
	
	df.to_csv('Filtered_points_by_speed_Tag_333A_Sept.csv', index=False)
	#print(speeds)
	#print(indicesToRemove)
	
if __name__== "__main__":
	main()




####

#df.dropline(indice)

#df['VELOCITà'] = speeds









