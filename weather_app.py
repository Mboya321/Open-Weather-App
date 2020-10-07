import tkinter as tk
import requests
from tkinter import font

root = tk.Tk()
canvas = tk.Canvas(root, height= 500, width=600)
canvas.pack()

#the keys below was based on my acc
#go visit openweathermap.org to get ur own key

#key=a3c049293a6abc2955af2f513cb32cca
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_ans = 'The weather of ' + name + ' is ' + desc + ' and the temp is ' + str(temp) + ' degree celsius'
        return final_ans
    except:
        error_msg = 'There was a problem when retrieving the data '
        return error_msg


def get_weather(city):
    weather_key = 'a3c049293a6abc2955af2f513cb32cca'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


#setting the background image
background_image = tk.PhotoImage(file='weather_image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#0c124c', bd=5)
frame.place(relx =0.5, rely=0.1,relwidth=0.75, relheight=0.1, anchor= 'n')

entry = tk.Entry(frame, font= 40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text= 'Get weather',  fg= 'black',
                   command= lambda: get_weather(entry.get()))
button.place(relx= 0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#0c124c', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth= 1, relheight=1)

root.mainloop()
