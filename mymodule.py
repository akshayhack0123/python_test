# ===========
# mymodule.py
# ===========

from urllib.request import urlopen
import json

def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3f63ccf4a308a813a06606c1bc526a16")
    result = sock.read()                            
    sock.close()                                        
    weather = json.loads(result)
    return weather["main"]["temp"] -273.15

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/" + postal_code)
    result = sock.read()                            
    sock.close()                                        
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])

if __name__ == "__main__":
    degrees = get_weather("OSLO")
    print("Weather in Oslo is %.2f degrees Celsius" % degrees)

    location = postal_lookup("B323PP")
    print("Latitude %.2f and langitude is %.2f" % location)
