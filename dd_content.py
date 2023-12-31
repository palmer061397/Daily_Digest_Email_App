# Used for get_random_quote function
import csv
import random
from urllib import request
import json
import datetime


# Get Random Quote
def get_random_quote(quotes_file='my_quotes.py'):
	try: # load motivational quotes from csv file 
	    with open(quotes_file) as csvfile:
	                     quotes = [{'author': line[0],
                      'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]
	except Exception as e:
	    print(e)
	return random.choice(quotes)
     	


# Get Weather Forcast
def get_weather_forecast(coords={'lat': 33.7557, 'lon': -96.5637}): # default location at Cape Canaveral, FL
    try: # retrieve forecast for specified coordinates
        api_key = 'YOUR_API_KEY' # replace with your own OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        data = json.load(request.urlopen(url))

        forecast = {'city': data['city']['name'], # city name
                    'country': data['city']['country'], # country name
                    'periods': list()} # list to hold forecast data for future periods

        for period in data['list'][0:9]: # populate list with next 9 forecast periods 
        	forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
        
        return forecast

    except Exception as e:
        print(e)

#Get Wiki Article
def get_wikipedia_article():
    try: # Retieve random wiki article
        data = json.load(request.urlopen("https://en.wikipedia.org/api/rest_v1/page/random/summary"))
        return {'title': data['title'], 'extract': data['extract'], 'url': data['content_urls']['desktop']['page']}
        
    except Exception as e:
    	print(e)
    

if __name__ == '__main__':
    #Get random quote
    quote = get_random_quote()
    print(f"Your quote for the day! \n{quote}")
    
    #Get weather
    print(get_weather_forecast())
    
    #Get wiki article summary
    article = get_wikipedia_article()
    if article:
          print(f"\n{article['title']}\n{article['url']}\n{article['extract']}")