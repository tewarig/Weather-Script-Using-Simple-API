
import requests, json 

api_key = "1361a757d4f77283d55528049474e9b6"

main_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter Your City : ")

url = main_url + "appid=" + api_key + "&q=" + city #It adds up city and api to form Complete Url

raw = requests.get(url)

report = raw.json()

print(report)

