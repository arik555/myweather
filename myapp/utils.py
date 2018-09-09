from weather import Weather, Unit


def get_arranged_data(myList):
	temp_forecast_dates = []
	temp_forecast_texts = []
	temp_forecast_high_data1 = []
	temp_forecast_low_data2 = []
	if len(myList) == 0:
		return 'None'
	# print(myList[1])
	address = myList[0]['city']+', '+myList[0]['region']+', '+myList[0]['country']+'.'
	atmosphere = '<b>Sunrise:</b> '+myList[2]['sunrise']+'<br><b>Sunset:</b> '+myList[2]['sunset']
	curr_weather_code = myList[1]
	wind_direction = myList[4]
	wind_speed = myList[3]['speed']
	forecast_data = myList[5]
	for each in forecast_data:
		temp_forecast_dates.append(each['date']+' - '+each['day'])
		temp_forecast_texts.append(each['text'])
		temp_forecast_high_data1.append(each['high'])
		temp_forecast_low_data2.append(each['low'])
	mini_temp = min(temp_forecast_low_data2)
	maxi_temp = max(temp_forecast_high_data1)
	dt = {'address': address, 'atmosphere': atmosphere, 'curr_weather_code': curr_weather_code['code'],
	'curr_weather_temp': curr_weather_code['temp'], 'curr_weather_text': curr_weather_code['text'], 'wind_direction': wind_direction, 
	'wind_speed': wind_speed, 'flag': '1', 
	'temp_forecast_dates': temp_forecast_dates, 
	'temp_forecast_texts': temp_forecast_texts, 'zip': zip(temp_forecast_dates, temp_forecast_high_data1, temp_forecast_low_data2, temp_forecast_texts), 
	'temp_forecast_high_data1': temp_forecast_high_data1, 
	'temp_forecast_low_data2': temp_forecast_low_data2, 'mini_temp': int(mini_temp)-5,
	'maxi_temp': int(maxi_temp)+5, }
	# print(dt)
	return dt


def get_proper_direction(n):
	directions = [('N', 0, 11.25), ('NNE', 11.25, 33.75), 
	('NE', 33.75, 56.25), ('ENE', 56.25, 78.75), ('E', 78.75, 101.25),
	('ESE', 101.25, 123.75), ('SE', 123.75, 146.25), ('SSE', 146.25, 168.75),
	('S', 168.75, 191.25), ('SSW', 191.25, 213.75), ('SW', 213.75, 236.25),
	('WSW', 236.25, 258.75), ('W', 258.75, 281.25), ('WNW', 281.25, 303.75),
	('NW', 303.75, 326.25), ('NNW', 326.25, 348.75)]
	direc = [direction for direction in directions if direction[1] <= n <= direction[2]][0][0]
	return direc


def get_weather_data(city_name):
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(city_name)
	try:
		dt = location._weather_data
		forecast_data = dt['item']['forecast']
		sun_rise_set = dt['astronomy']
		curr_temp_cond = location.condition._condition_data
		wind_data = location.wind._wind_data
		place = {'city': location.location.city, 'region': location.location.region, 'country': location.location.country}
		direction = get_proper_direction(float(wind_data['direction']))
	except:
		return 0
	else:		
		return (place, curr_temp_cond, sun_rise_set,
			wind_data, direction, forecast_data)

'''
({'city': 'Kolkata', 'region': ' WB', 'country': 'India'}, 
{'code': '29', 'date': 'Fri, 07 Sep 2018 07:30 PM IST', 'temp': '27', 'text': 'Partly Cloudy'}, 
{'sunrise': '5:21 am', 'sunset': '5:47 pm'}, 
{'chill': '81', 'direction': '135', 'speed': '17.70'}, 
'SE',
[{'code': '4', 'date': '07 Sep 2018', 'day': 'Fri', 'high': '29', 'low': '25', 'text': 'Thunderstorms'}, {'code': '4', 'date': '08 Sep 2018', 'day': 'Sat', 'high': '31', 'low': '25', 'text': 'Thunderstorms'}, {'code': '4', 'date': '09 Sep 2018', 'day': 'Sun', 'high': '31', 'low': '25', 'text': 'Thunderstorms'}, {'code': '4', 'date': '10 Sep 2018', 'day': 'Mon', 'high': '31', 'low': '26', 'text': 'Thunderstorms'}, {'code': '4', 'date': '11 Sep 2018', 'day': 'Tue', 'high': '32', 'low': '26', 'text': 'Thunderstorms'}, {'code': '26', 'date': '12 Sep 2018', 'day': 'Wed', 'high': '32', 'low': '26', 'text': 'Cloudy'}, {'code': '28', 'date': '13 Sep 2018', 'day': 'Thu', 'high': '32', 'low': '26', 'text': 'Mostly Cloudy'}, {'code': '4', 'date': '14 Sep 2018', 'day': 'Fri', 'high': '31', 'low': '26', 'text': 'Thunderstorms'}, {'code': '4', 'date': '15 Sep 2018', 'day': 'Sat', 'high': '31', 'low': '25', 'text': 'Thunderstorms'},
-----------
{'code': '4', 'date': '16 Sep 2018', 'day': 'Sun', 'high': '30', 'low': '26', 'text': 'Thunderstorms'}])
'''