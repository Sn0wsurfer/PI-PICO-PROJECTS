import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import urequests as requests
#import decimal
import ujson as json

# network.hostname("****")
ssid = '****'
password = '****'
Hname = "****"

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

def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request =='/lightoff?':
            pico_led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp    
        html = webpage(temperature, state)
        client.send(html)        
        client.close()
        
def openweather():
#     data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=wellington,nz&appid=7d635aea345b49cbecc4d2158bebe7b2").json()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-41.328&lon=174.805&appid=7d635aea345b49cbecc4d2158bebe7b2").json()
    json_str = json.dumps(data)
    resp = json.loads(json_str)
    data2 = data.get("wind")
    json_str2 = json.dumps(data2)
    resp = json.loads(json_str2)
    WindSpeed = float
    WindSpeed = (resp["speed"])
    Windno = int(round(WindSpeed)*3.6)
    
    data3 = data.get("main")
    json_str3 = json.dumps(data3)
    resp = json.loads(json_str3)
    temptx = float
    temptx = (resp["temp"])
    temp = int(round(temptx -273.15))
    # Lightno = 90
    #test print varible if required
    Stemp = "Temperature " + str(temp)
    SWindno = "wind Speed " + str(Windno)
    print (Stemp)
    print (SWindno)
       
try:
    ip = connect()
    connection = open_socket(ip)
    openweather()
    serve(connection)

    
except KeyboardInterrupt:
    machine.reset()
    

