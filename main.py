import requests, json 

api_key = "1361a757d4f77283d55528049474e9b6"

main_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter Your City : ")

url = main_url + "appid=" + api_key + "&q=" + city #It adds up city and api to form Complete Url

raw = requests.get(url)

report = raw.json()
if report["cod"]==200:
    temp=report["main"]["temp"]
    tempfeels=report["main"]["feels_like"]
    humidity=report["main"]["humidity"]
    temp = temp - 273.15
    tempfeels = tempfeels - 273.15
    timezone= report["timezone"]
    if timezone < 0:
        hrs = timezone // 3600
        min = -(timezone - hrs * 3600) // 60
    else:
        hrs=timezone//3600
        min=(timezone - hrs*3600)//60
    tempf= temp * 9/5 + 32
    tempfeelsf= tempfeels * 9/5 + 32
    print("Tempreture       ",round(temp,2)," °C  or ",round(tempf,2)," °F")
    print("Tempreture Feels ",round(tempfeels,2)," °C  or ",round(tempfeelsf,2)," °F")
    if tempfeels > 38:
        print(" Tempreture May Cause Your Beautiful Skin Burn, Avoid Going Outside without Cover and Sunglasses ")
    print("Humidity         ",humidity," % ")
    if humidity > 85:
        print("Its Likely to Rain Better take Umbrella with You")
    print("Time Zone ",hrs,"Hour",min,"Mins GMT ")
else:
    print("City Not Found In Database")
