import urequests as requests
import ujson
import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

# network.hostname("Jungle_S_LED")
ssid = 'PreAnthropocene'
password = 'Arr1p1sTrutt@'
Hname = "Jungle_S_LED"

#https://api.openweathermap.org/data/2.5/weather?lat=-41.328&lon=174.805&appid=
def get_weather_data():
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=-41.328&lon=174.805&appid='

    try:
        response = requests.get(weather_url)
        if response.status_code == 200:
        # Parse the JSON response
            weather_data = ujson.loads(response.text)
            
            # Extract wind speed and temperature
            wind_speed = weather_data.get("wind", {}).get("speed")
            temperature = weather_data.get("main", {}).get("temp")
            windno = int(round(wind_speed)*3.6)
            temp = int(round(temperature -273.15))
            
            print(f"Wind Speed: {windno}kph")
            print(f"Temperature: {temp}°C")
        
        else:
            print("Failed to fetch weather data")
            
    except Exception as e:
        print('Error:', e)
        
        
def connect():
    #Connect to WLAN
    wlan = network.hostname(Hname)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return(connection)

try:
    ip = connect()
    connection = open_socket(ip)
    get_weather_data()


    
except KeyboardInterrupt:
    machine.reset()

