import time
import board
import neopixel
import json
import sys
import requests
import decimal
from math import radians, cos, sin, asin, sqrt

Loopv = 0
EQid2 = "New"
# print(EQid2)

while Loopv <= 8000:
    if Loopv % 30 == 0:
            #     data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=wellington,nz&appid=7d635aea345b49cbecc4d2158bebe7b2").json()
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-41.328&lon=174.805&appid=7d635aea345b49cbecc4d2158bebe7b2").json()
        json_str = json.dumps(data)
        resp = json.loads(json_str)
        data2 = data.get("wind")
        json_str2 = json.dumps(data2)
        resp = json.loads(json_str2)
        WindSpeed = decimal.Decimal
        WindSpeed = (resp["speed"])
        Windno = int(round(WindSpeed)*3.6)
        
        data3 = data.get("main")
        json_str3 = json.dumps(data3)
        resp = json.loads(json_str3)
        temptx = decimal.Decimal
        temptx = (resp["temp"])
        temp = int(round(temptx -273.15))
        # Lightno = 90
        #test print varible if required
        Stemp = "Temperature " + str(temp)
        SWindno = "wind Speed " + str(Windno)
        print (Stemp)
        print (SWindno)

        pixels = neopixel.NeoPixel(board.D18, 202, brightness=0.1)
        pixels.fill((0, 255, 0))
        for i in range(Windno + 101):
            pixels[i] = (51, 178, 255)
        
        for i in range(101):
            pixels[i] = (0, 255, 0)
        
        for i in range(temp * 2):
            pixels[i] = (51, 178, 255)    
            
        pixels[0] = (0, 0, 0)
#        pixels[10] = (255, 0, 0)
        pixels[20] = (255, 0, 0)
#        pixels[30] = (255, 0, 0)
        pixels[40] = (255, 0, 0)
#        pixels[50] = (255, 0, 0)
        pixels[60] = (255, 0, 0)
#        pixels[70] = (255, 0, 0)
        pixels[80] = (255, 0, 0)
#        pixels[90] = (255, 0, 0)
        pixels[100] = (255, 0, 0)
        pixels[101] = (0, 0, 0)
        pixels[110] = (255, 0, 0)
        pixels[120] = (255, 0, 0)
        pixels[130] = (255, 0, 0)
        pixels[140] = (255, 0, 0)
        pixels[150] = (255, 0, 0)
        pixels[160] = (255, 0, 0)
        pixels[170] = (255, 0, 0)
        pixels[180] = (255, 0, 0)
        pixels[190] = (255, 0, 0)
        pixels[200] = (255, 0, 0)
        
    EQdata = requests.get("https://api.geonet.org.nz/quake?MMI=1").json()


    json_str = json.dumps(EQdata)
    resp = json.loads(json_str)
    EQdata2 = EQdata.get("features")

    json_str = json.dumps(EQdata2)
    resp = json.loads(json_str)
    EQdata3 = (resp[0])

    json_str = json.dumps(EQdata3)
    resp = json.loads(json_str)
    EQdata4 = EQdata3.get("properties")
    EqLoc = EQdata3.get("geometry")

    json_str = json.dumps(EQdata4)
    resp = json.loads(json_str)
    Mag = EQdata4.get("magnitude")
    EQid = EQdata4.get("publicID")

    json_str = json.dumps(EqLoc)
    resp = json.loads(json_str)
    EqLoc2 = EqLoc.get("coordinates")

    json_str = json.dumps(EqLoc2)
    resp = json.loads(json_str)
    lon2 = (resp[0])
    lat2 = (resp[1])

    Mag2 = float(round(Mag,2))
    Lightno = int(Mag2*10)

    lon1 = 174.831151
    lat1 = -41.322746

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    DistTemp = int(round(c * r))
    
    # DistTemp = 1449
    # error handling, IF distance greater than 1000km then greater available lights therefore limit to 1000
    # print(DistTemp)
   
    if DistTemp > 1000:
        Dist = 1000
    else: Dist = DistTemp
    
    SMag = "Magnitude " + str(Mag2)
    SEQid = "I.D. " + str(EQid)
    SDist = "Distance " + str(DistTemp)

    print(SMag)
    print(SEQid)
    print(SDist)
    
#     Distno = decimal.Decimal
#     Distno = int(round(Dist))
#     print(Dist)
    
    pixels = neopixel.NeoPixel(board.D18, 202, brightness=0.1)
    
    if (EQid != EQid2):
    
        pixels.fill((255, 0, 0))
        for i in range(int(Dist/10)+101):
            pixels[i] = (0, 255, 0)
            
        for i in range(101):
            pixels[i] = (0, 255, 0)    
                
        for i in range(Lightno):
            pixels[i] = (255, 0, 0)

        time.sleep(0.1)

        pixels[0] = (0, 0, 0)
        pixels[10] = (20, 20, 20)
        pixels[20] = (20, 20, 20)
        pixels[30] = (20, 20, 20)
        pixels[40] = (20, 20, 20)
        pixels[50] = (20, 20, 20)
        pixels[60] = (20, 20, 20)
        pixels[70] = (20, 20, 20)
        pixels[80] = (20, 20, 20)
        pixels[90] = (20, 20, 20)
        pixels[100] = (20, 20, 20)
        pixels[101] = (0, 0, 0)
        pixels[110] = (20, 20, 20)
        pixels[120] = (20, 20, 20)
        pixels[130] = (20, 20, 20)
        pixels[140] = (20, 20, 20)
        pixels[150] = (20, 20, 20)
        pixels[160] = (20, 20, 20)
        pixels[170] = (20, 20, 20)
        pixels[180] = (20, 20, 20)
        pixels[190] = (20, 20, 20)
        pixels[200] = (20, 20, 20)

        time.sleep(10)

        pixels.fill((0, 255, 0))

        pixels[0] = (0, 0, 0)
        pixels[10] = (20, 20, 20)
        pixels[20] = (20, 20, 20)
        pixels[30] = (20, 20, 20)
        pixels[40] = (20, 20, 20)
        pixels[50] = (20, 20, 20)
        pixels[60] = (20, 20, 20)
        pixels[70] = (20, 20, 20)
        pixels[80] = (20, 20, 20)
        pixels[90] = (20, 20, 20)
        pixels[100] = (20, 20, 20)
        pixels[101] = (0, 0, 0)
        pixels[110] = (20, 20, 20)
        pixels[120] = (20, 20, 20)
        pixels[130] = (20, 20, 20)
        pixels[140] = (20, 20, 20)
        pixels[150] = (20, 20, 20)
        pixels[160] = (20, 20, 20)
        pixels[170] = (20, 20, 20)
        pixels[180] = (20, 20, 20)
        pixels[190] = (20, 20, 20)
        pixels[200] = (20, 20, 20)

        time.sleep(1)

        pixels.fill((255, 0, 0))
        for i in range(int(Dist/10)+101):
            pixels[i] = (0, 255, 0)
        
        for i in range(101):
            pixels[i] = (0, 255, 0)
        
        for i in range(Lightno):
            pixels[i] = (255, 0, 0)

        pixels[0] = (0, 0, 0)
        pixels[10] = (20, 20, 20)
        pixels[20] = (20, 20, 20)
        pixels[30] = (20, 20, 20)
        pixels[40] = (20, 20, 20)
        pixels[50] = (20, 20, 20)
        pixels[60] = (20, 20, 20)
        pixels[70] = (20, 20, 20)
        pixels[80] = (20, 20, 20)
        pixels[90] = (20, 20, 20)
        pixels[100] = (20, 20, 20)
        pixels[101] = (0, 0, 0)
        pixels[110] = (20, 20, 20)
        pixels[120] = (20, 20, 20)
        pixels[130] = (20, 20, 20)
        pixels[140] = (20, 20, 20)
        pixels[150] = (20, 20, 20)
        pixels[160] = (20, 20, 20)
        pixels[170] = (20, 20, 20)
        pixels[180] = (20, 20, 20)
        pixels[190] = (20, 20, 20)
        pixels[200] = (20, 20, 20)
        EQid2 = EQid
        print(EQid2)
        
        time.sleep(10)
        
        pixels = neopixel.NeoPixel(board.D18, 202, brightness=0.1)
        pixels.fill((0, 255, 0))
        for i in range(Windno + 101):
            pixels[i] = (51, 178, 255)
        
        for i in range(101):
            pixels[i] = (0, 255, 0)
        
        for i in range(temp * 2):
            pixels[i] = (51, 178, 255)    
            
        pixels[0] = (0, 0, 0)
#        pixels[10] = (255, 0, 0)
        pixels[20] = (255, 0, 0)
#        pixels[30] = (255, 0, 0)
        pixels[40] = (255, 0, 0)
#        pixels[50] = (255, 0, 0)
        pixels[60] = (255, 0, 0)
#        pixels[70] = (255, 0, 0)
        pixels[80] = (255, 0, 0)
#        pixels[90] = (255, 0, 0)
        pixels[100] = (255, 0, 0)
        pixels[101] = (0, 0, 0)
        pixels[110] = (255, 0, 0)
        pixels[120] = (255, 0, 0)
        pixels[130] = (255, 0, 0)
        pixels[140] = (255, 0, 0)
        pixels[150] = (255, 0, 0)
        pixels[160] = (255, 0, 0)
        pixels[170] = (255, 0, 0)
        pixels[180] = (255, 0, 0)
        pixels[190] = (255, 0, 0)
        pixels[200] = (255, 0, 0)
        
    Loopv += 1
    print ("loop ")
    print (Loopv)
    time.sleep(10)
