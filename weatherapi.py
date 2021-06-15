import tkinter as tk
import requests
import time


def getweather(canvas):
    city = textfield.get()
    api ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cc69566d46bbf2f239bfe3ebe39d3fd6"
    json_data=requests.get(api).json()
    
    try:
        condition=json_data['weather'][0]['main']
        temp=int(json_data['main']['temp']-273.15)
        max_temp=int(json_data['main']['temp_min']-273.15)
        min_temp=int(json_data['main']['temp_max']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
        sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
        sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))
        final_info=condition+'/n'+str(temp)+"c"
        final_data='\n'+"Max temp"+str(max_temp)+"\n"+"Min Temp"+str(min_temp)+'\n'+'pressure'+str(pressure)+"\n"+"Humidity"+str(humidity)+"\n"+"Wind Speed"+str(wind)+"\n"+"sun rise"+"\n"+sunrise+'\n'+"sunset :"+sunset
        lebel1.config(text=final_info)
        lebel2.config(text=final_data)
    except:
        lebel1.config(text="Location not recognised")
        lebel2.config(text='')

    
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getweather)
lebel1 = tk.Label(canvas, font=t)
lebel1.pack()
lebel2 = tk.Label(canvas, font=f)
lebel2.pack()
canvas.mainloop()
