from tkinter import *
from PIL import Image, ImageTk  
from tkinter import ttk
import requests


from datetime import datetime

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=your__api"
    data = requests.get(url).json()

    if data["cod"] != "200":
        w_label1.config(text="N/A")
        wb_label1.config(text="Invalid City")
        temp_label1.config(text="N/A")
        pr_label1.config(text="N/A")
        maxtemp_label1.config(text="N/A")
        mintemp_label1.config(text="N/A")
        return

    # Get current weather (first entry in list)
    current = data["list"][0]
    w_label1.config(text=current["weather"][0]["main"])
    wb_label1.config(text=current["weather"][0]["description"])
    temp_label1.config(text=str(int(current["main"]["temp"] - 273.15)))
    pr_label1.config(text=current["main"]["pressure"])

    # Get today's min and max temp from all 3-hourly forecasts
    today = datetime.now().date()
    temps_today = [item["main"]["temp"] for item in data["list"]
                   if datetime.fromtimestamp(item["dt"]).date() == today]

    if temps_today:
        min_temp = min(temps_today)
        max_temp = max(temps_today)
        maxtemp_label1.config(text=str(int(max_temp - 273.15)))
        mintemp_label1.config(text=str(int(min_temp - 273.15)))
    else:
        maxtemp_label1.config(text="N/A")
        mintemp_label1.config(text="N/A")

    

win = Tk()
win.title(" Saurav's Weather App")
win.config(bg="#639DD5")
win.geometry("500x660")

# Set cloud icon from PNG
cloud_icon = PhotoImage(file="clouds.png")  # PNG file
win.iconphoto(False, cloud_icon)

# Heading label
name_label = Label(win, text=" Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = [
    "Achham", "Arghakhanchi", "Baglung", "Bhaktapur", "Bara", "Bardiya", "Bhotejhora", "Bhojpur", "Chakechaur", "Chaurpati", "Chitwan", "Dadeldhura", "Dailekh", "Dang", "Dhading", "Darchula", "Dhankuta", "Dholpa", "Dolakha", "Gorkha", "Gulmi", "Hetauda", "Humla", "Jajarkot", "Jarnath", "Jhapa", "Kalikot", "Kanchanpur", "Kapilvastu", "Kaski", "Kathmandu", "Khatmandu", "Kailali", "Lalitpur", "Lamjung", "Lumbini", "Mahottari", "Makwanpur", "Manang", "Manthar", "Mugu", "Mustang", "Myagdi", "Naya", "Nawalparasi", "Nuwakot", "Okhaldhunga", "Palpa", "Panchthar", "Parbat", "Phaikapur", "Pyuthan", "Rampur", "Ramechhap", "Rapti", "Rasuwa", "Rolpa", "Rukum", "Rampur", "Salyan", "Sankhuwasabha", "Saptari", "Saruhari", "Sindhuli", "Sindupalchowk", "Siraha", "Syangja", "Tanahun", "Taplejung", "Terahi", "Udayapur", "Sunsari", "Bhadrapur", "Jharkot", "Baidik", "Guna"
]
com = ttk.Combobox(win, text="Weather App",values=list_name, font=("Times New Roman", 20, "bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)


w_label = Label(win, text=" Weather Climate", font=("Times New Roman", 15))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Times New Roman", 15))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text=" Weather Description", font=("Times New Roman", 15))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Times New Roman", 15))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text=" Temperature", font=("Times New Roman", 15))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 15))
temp_label1.place(x=250, y=400, height=50, width=210)


pr_label = Label(win, text=" Pressure", font=("Times New Roman", 15))
pr_label.place(x=25, y=470, height=50, width=210)

pr_label1 = Label(win, text="", font=("Times New Roman", 15))
pr_label1.place(x=250, y=470, height=50, width=210)


maxtemp_label = Label(win, text=" Max Temperature", font=("Times New Roman", 15))
maxtemp_label.place(x=25, y=540, height=50, width=210)

maxtemp_label1 = Label(win, text="", font=("Times New Roman", 15))
maxtemp_label1.place(x=250, y=540, height=50, width=210)

mintemp_label = Label(win, text=" Min Temperature", font=("Times New Roman", 15))
mintemp_label.place(x=25, y=610, height=50, width=210)

mintemp_label1 = Label(win, text="", font=("Times New Roman", 15))
mintemp_label1.place(x=250, y=610, height=50, width=210)




done = Button(win, text="Search", font=("Times New Roman", 20, "bold"),command=data_get)
done.place(x=200, y=180, height=50, width=100)


win.mainloop()




