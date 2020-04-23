import requests, json 

api_key = "1361a757d4f77283d55528049474e9b6"

main_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter Your City : ")

url = main_url + "appid=" + api_key + "&q=" + city #It adds up city and api to form Complete Url

raw = requests.get(url)

report = raw.json()

temp=report["main"]["temp"]
tempfeels=report["main"]["feels_like"]
humidity=report["main"]["humidity"]
temp = temp - 273.15
tempfeels = tempfeels - 273.15
timezone= report["timezone"]
hrs=timezone//3600
min=(timezone - hrs*3600)//60
print("Tempreture            ",temp)
print("Tempreture Feels Like ",round(tempfeels,2))
print("Humidity              ",humidity)
print("Time Zone             ",hrs,min," GMT ")
