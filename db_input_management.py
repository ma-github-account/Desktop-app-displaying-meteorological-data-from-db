
import pyodbc

server = "server"
database = "database"
username = "username"
password = "password"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

def select_all_records_from_Weather_Info_database():

	cursor.execute("SELECT * FROM Weather_Info")
	
	for row in cursor:
		print(row)

def insert_player_into_database(Date, Temperature, Wind_speed, Wind_direction, Relative_humidity, Total_precipitation, Pressure, Solar_radiation_intensity, Location, Day_or_night):

	count = cursor.execute("""
	INSERT INTO Weather_Info (Date, Temperature, Wind_speed, Wind_direction, Relative_humidity, Total_precipitation, Pressure, Solar_radiation_intensity, Location, Day_or_night) 
	VALUES (?,?,?,?,?,?,?,?,?,?)""",
	Date, Temperature, Wind_speed, Wind_direction, Relative_humidity, Total_precipitation, Pressure, Solar_radiation_intensity, Location, Day_or_night).rowcount

	cnxn.commit()

def select_last_10_temperature_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Temperature] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_wind_speed_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Wind_speed] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_Wind_direction_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Wind_direction] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_Relative_humidity_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Relative_humidity] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_Total_precipitation_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Total_precipitation] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_Pressure_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Pressure] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results

def select_last_10_Solar_radiation_intensity_records_for_given_location_and_day_or_night_time_status_from_Weather_Info_database(day_or_night,location):

	cursor.execute("SELECT TOP (10) [Solar_radiation_intensity] FROM [Test1].[dbo].[Weather_Info] WHERE [Day_or_night] = ? AND [Location] = ? ORDER BY [Date] asc", day_or_night, location)
	
	list_of_results = []

	for row in cursor:
		list_of_results.append(row[0])

	return list_of_results























