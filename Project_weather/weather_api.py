#เกี่ยวกับ GUI 
from tkinter import * 
import tkinter as tk 
from tkinter import ttk, messagebox 
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import * 
import requests
import pytz
import decimal  
#ทำงานกับรูปภาพ
from PIL import Image , ImageTk



#ส่วนต่างๆของGUI
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg='#57adff')
# root.resizable(False,False)

# Function 
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
    # api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=hourly&appid=58ff00cbbcd2d6ac95efbf904a477300"
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=58ff00cbbcd2d6ac95efbf904a477300"
    
  
    json_data = requests.get(api).json()
    print(json_data)



    #current 
    temping = json_data['main']['temp'] #Kelvin
    temp =  decimal.Decimal(temping - 273.15) #change become Celcius 
    humidity = json_data['main']['humidity'] # right
    pressure = json_data['main']['pressure'] # right 
    wind = json_data['wind']['speed'] #right 
    description = json_data['weather'][0]['description'] #You have to add index into description
    

  

    #after we set the place for show  we will add text in box 
    t.config(text=(round(temp),"°C"))
    h.config(text=(humidity,'%'))
    p.config(text=(pressure,'hPa'))
    w.config(text=(wind,'m/s'))
    d.config(text=description)

    #first cell
    firstdayimage = json_data['weather'][0]['icon']
    print(firstdayimage)

    photo1 = ImageTk.PhotoImage(file =f"Project_weather/icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image_names = photo1

    tempday1 = json_data['temp']['day']

    # They have problem with the api vertion  {'cod': 401, 'message': 'Please note that using One Call 3.0 requires a separate subscript

    #second cell 
    seconddayimage = json_data['weather'][0]['icon']
    print(seconddayimage)

    # photo2 = ImageTk.PhotoImage(file =f"Project_weather/icon/{seconddayimage}@2x.png")
    # resize_imgae = resize_imgae(50,50)
    # secondimge.config(image=photo2)
    # secondimge.image_names = photo2
    
    #thrid cell
    thirddayimage = json_data['weather'][0]['icon']
    print(thirddayimage)
 
    #fourth cell

    fourthdayimg = json_data['weather'][0]['icon']
    print(fourthdayimg)

    #fifth cell 

    fifthdayimge = json_data['weather'][0]['icon']
    print(fifthdayimge)

    #sixth cell

    sixthdayimage = json_data['weather'][0]['icon']
    print(sixthdayimage)

    #seventh cell

    seventhdayimage = json_data['weather'][0]['icon']
    print(seventhdayimage)


    #days 
    first =  datetime.now()
    day1.config(text=first.strftime('%A'))

    #ทำการ + วันเพิ่ม
    second =  first+timedelta(days=1)
    day2.config(text=second.strftime('%A'))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime('%A'))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime('%A'))
    
    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime('%A'))
    
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime('%A'))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime('%A'))



# All Function#

image_icon = PhotoImage(file="Project_weather/Images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file='Project_weather/Images/Rounded_Rectangle_1.png')
Label(root,image=Round_box,bg='#57adff').place(x=45,y=110)



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



#Setting in right box
t = Label(root,font=('Helvetica',11),fg = 'White',bg = '#203243')
t.place(x=150,y=120)

h = Label(root,font=('Helvetica',11),fg = 'White',bg = '#203243')
h.place(x=150,y=140)

p = Label(root,font=('Helvetica',10),fg = 'White',bg = '#203243')
p.place(x=150,y=160)

w = Label(root,font=('Helvetica',10),fg = 'White',bg = '#203243')
w.place(x=150,y=180)

d = Label(root,font=('Helvetica',8),fg = 'White',bg = '#203243')
d.place(x=150,y=200)


#all cell footer 
 
#first cell 
first_frame = Frame(root,width=230,height=132,bg='#282829')
first_frame.place(x=35,y=315)

day1 = Label(first_frame,font='arial 20',bg='#282829',fg='#fff')
day1.place(x=100,y=5)

firstimage = Label(first_frame,bg='#282829')
firstimage.place(x=1,y=15)


day1temp = Label(first_frame,bg='#282829',fg='#fff')
day1temp.place(x=100, y=50)




#second cell 
second_frame = Frame(root,width=70,height=115,bg='#282829')
second_frame.place(x=305,y=325)

day2 = Label(second_frame,font='arial 10',bg='#282829',fg='#fff')
day2.place(x=10,y=5)


secondimge = Label(second_frame,bg='#282829')
secondimge.place(x=7,y=20)


#third cell
third_frame = Frame(root,width=70,height=115,bg='#282829')
third_frame.place(x=405,y=325)

day3 = Label(third_frame,font='arial 10',bg='#282829',fg='#fff')
day3.place(x=10,y=5)


thirdimge = Label(third_frame,bg='#282829')
thirdimge.place(x=7,y=20)

#fourth cell
fourth_frame = Frame(root,width=70,height=115,bg='#282829')
fourth_frame.place(x=505,y=325)

day4 = Label(fourth_frame,bg='#282829',fg='#fff')
day4.place(x=10,y=5)

fourthimge = Label(fourth_frame,bg='#282829')
fourthimge.place(x=7,y=20)


#fifth cell
fifth_frame = Frame(root,width=70,height=115,bg='#282829')
fifth_frame.place(x=605,y=325)

day5 = Label(fifth_frame,bg='#282829',fg='#fff')
day5.place(x=10,y=5)

fifthimge = Label(fifth_frame,bg='#282829')
fifthimge.place(x=7,y=20)


#sixth cell 
sixth_frame = Frame(root,width=70,height=115,bg='#282829')
sixth_frame.place(x=705,y=325)

day6 = Label(sixth_frame ,font='arial 8',bg='#282829',fg='#fff')
day6.place(x=8,y=5)

sixthimge = Label(sixth_frame,bg='#282829')
sixthimge.place(x=7,y=20)


# seventh cell 
seventh_frame = Frame(root,width=70,height=115,bg='#282829')
seventh_frame.place(x=805,y=325)

day7 = Label(seventh_frame,font='arial 8' ,bg='#282829',fg='#fff')
day7.place(x=5,y=5)

seventhimage = Label(seventh_frame,bg='#282829')
seventhimage.place(x=7,y=20)




















root.mainloop()