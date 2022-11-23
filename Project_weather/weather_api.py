#เกี่ยวกับ GUI 
from tkinter import * 
import tkinter as tk 
from tkinter import ttk, messagebox 
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import * 
import requests
import pytz
#ทำงานกับรูปภาพ
from PIL import Image , ImageTk



#ส่วนต่างๆของGUI
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg='#57adff')
# root.resizable(False,False)

# time vedio is 30.00
def getWheater():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezoner.config(text=result)
    long_lati.config(text=f"{round(location.longitude,4)}°N{round(location.latitude,4)}°E")
    #Time zone for show 
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    Current_time = local_time.strftime("%I:%M %p")
    clock.config(text=Current_time)

   

    #weather 
    #chnage vertion 2.5 from 3
    # api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=58ff00cbbcd2d6ac95efbf904a477300"
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=58ff00cbbcd2d6ac95efbf904a477300"
    
  
    json_data = requests.get(api).json()
    print(json_data)
    #current 
    temping = json_data['main']['temp'] #Kelvin
    temp =  temping - 273.15
    humidity = json_data['main']['humidity'] # right
    pressure = json_data['main']['pressure'] # right 
    wind = json_data['wind']['speed'] #right 
    

    print(temp)
    print(humidity)
    print(pressure)
    print(wind)
    # print(description)

# All Function#

image_icon = PhotoImage(file="Project_weather/Images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file='Project_weather/Images/Rounded_Rectangle_1.png')
Label(root,image=Round_box,bg='#57adff').place(x=30,y=110)



#Label 
label1 = Label(root,text ='Temperature',font=('Helvetica,',11),fg='white',bg = '#203243')
label1.place(x = 50 , y =120)

label2 = Label(root,text ='Humidity',font=('Helvetica,',11),fg='white',bg = '#203243')
label2.place(x = 50 , y =140)

label3 = Label(root,text ='Pressure',font=('Helvetica,',11),fg='white',bg = '#203243')
label3.place(x = 50 , y =160)

label4 = Label(root,text ='Wind Speed',font=('Helvetica,',11),fg='white',bg = '#203243')
label4.place(x = 50 , y =180)

label5 = Label(root,text ='Description',font=('Helvetica,',11),fg='white',bg = '#203243')
label5.place(x = 50 , y =200)

#search box 
Search_images = PhotoImage(file="Project_weather/Images/Rounded Rectangle 3.png")
myimages = Label(image=Search_images,bg='#57adff')
myimages.place(x=270 , y=120)




weat_images = PhotoImage(file="Project_weather/Images/Layer 7.png")
weather_image = Label(root,image= weat_images , bg= '#203243')
weather_image.place(x= 290 , y =127)


textfield = tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg = '#203243',border=0,fg='white')
textfield.place(x= 370 ,y = 130)
textfield.focus()

Search_icon = PhotoImage(file ='Project_weather/Images/Layer 6.png')
myimages_icon = Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='#203243',command=getWheater)
myimages_icon.place(x=645,y=125)


##Footer##
frame = Frame(root,width=900,height=180,bg ='#212120')
frame.pack(side=BOTTOM)



#Bottom Box 
firstbox = PhotoImage(file='Project_weather/Images/Rounded Rectangle 2.png')
secondbox = PhotoImage(file='Project_weather/Images/Rounded Rectangle 2 copy.png')


Label(frame,image=firstbox,bg ='#212120').place(x = 30, y = 20)
Label(frame,image=secondbox,bg='#212120').place(x=300,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=400,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=500,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=600,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=700,y=30)
Label(frame,image=secondbox,bg='#212120').place(x=800,y=30)


#Clock 
clock = Label(root,font =('Helvetica',30,'bold'),fg='white',bg='#57adff')
clock.place(x=30,y=20)

#time zone 
timezoner = Label(root,font =('Helvetica',20,'bold'),fg='white',bg='#57adff')
timezoner.place(x=600,y=20)


long_lati = Label(root,font =('Helvetica',10,'bold'),fg='white',bg='#57adff')
long_lati.place(x=600,y=50)
#comeback to search_icon for  add Commnad 



















root.mainloop()