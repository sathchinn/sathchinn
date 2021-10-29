from tkinter import*
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_farenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather']['icon']
        weather = json['weather']['main']
        final = {city, country, temp_celcius, temp_farenheit, icon, weather}
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        image['bitmap'] = 'weather icons/{}.png'
        temp_lbl['text'] = '{:.2f}°C {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]

    else:
        messagebox.showerror('Error', 'Cannot find City {}'.format(city))


app = Tk()
app.title('Weather app')
app.geometry('700x450')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search Weather', width=15, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()
