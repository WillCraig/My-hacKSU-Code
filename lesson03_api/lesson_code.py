import requests
import json


KEY = ""



def get_weather(zip_code):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}'.format(zip_code, KEY) #
    
    response = requests.get(url)
    
    data = response.json()
    
    pretty_data = json.dumps(data, indent=4)
    
    city = data['name']
    
    print(city)
    
    
    
    
    tempK = data['main']['temp']
    
    tempF = 1.8 * (tempK - 273) + 32
    
    
    print(tempK)
    print(tempF)
    print(int(tempF)) # shortcut to getting no floating output, would rather use output formatting 
    
    
    print("\n\n\n\n") # separator
    
    
    print(f"The temperature in {city} is {tempF:.2f}") 

    
    
    # print(pretty_data)
    





if __name__ == '__main__':
    
    zip = 44262
    
    get_weather(zip)
    
    
    
    
    