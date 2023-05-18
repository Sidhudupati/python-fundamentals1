import requests
city='Dubai'
url = 'http://api.weatherapi.com/v1/current.json?key=a198dff997c746128b3134735230205&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()
temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')
print("Today's weather in",city,"is",description,'and',temp,'degrees')
 