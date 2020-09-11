from plyer import notification
import requests
import time

# Creating notification
def notifyMe(title,message):
    notification.notify(
        title=title,
        message = message,
        app_icon = 'corona.ico',
        timeout= 6
    )
# Fetching data from web
def getData(url):
    r = requests.get(url)
    return r.json()

if __name__ == '__main__':
    while(True):
        myData = getData('https://api.covidindiatracker.com/state_data.json')
        for item in myData[4:5]:
            print(item)
            notifyMe(item['state'],f"Active Cases : {item['active']}\nConfirmed Cases : {item['confirmed']}\nRecovered Cases : {item['recovered']}\nDeath : {item['deaths']}")
        time.sleep(1800)




