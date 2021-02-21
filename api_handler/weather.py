#in the name of Allah

from hazm import *
from numberize import *
import requests

def HOUR(hour):
    if hour >= 0 and hour <= 1:
        hour = "00:00:00"
    elif hour > 1 and hour <= 4 :
        hour = "03:00:00"
    elif hour > 4 and hour <=7  :
        hour = "06:00:00"
    elif hour > 7 and hour <=10  :
        hour = "09:00:00"
    elif hour > 10 and hour <=13  :
        hour = "12:00:00"
    elif hour > 13 and hour <=16  :
        hour = "15:00:00"
    elif hour > 16 and hour <=19  :
        hour = "18:00:00"
    elif hour > 19 and hour <=22  :
        hour = "21:00:00"
    elif hour > 22 and hour <24  :
        hour = "00:00:00"
    return hour

def tempreture(question_word , temp):
    if question_word.count('کلوین') :
        return temp
    elif question_word.count('فارنهایت'):
        temp = temp-273.15
        temp = (9*temp)/5
        return temp
    else:
        temp = temp-273.15
        temp = round(temp,2)
        return temp

def get_weather_data(city='تهران',appid='db38fb876e097be27b9352b7b6dccb25'):
    URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(city,appid)
    r = requests.get(URL) 
    data = (r.json()).copy()
    return r.json(),URL

def temp_min(weather_data,date_list,hour):
    temp_list = []

    if hour == -1 :
        for i in range(40) :
            date  = weather_data['list'][i]['dt_txt']
            for j in date_list:
                if date.count(str(j)) > 0:  
                    temp_list.append(weather_data['list'][i]['main']['temp_min'])
        return temp_list
  
    hour = HOUR(hour)
    l
    for i in range(40) :
        date  = weather_data['list'][i]['dt_txt']
        date = date.split()
        for j in date_list:
            if date[0].count(str(j)) > 0 and date[1].count(hour) >0:  
                temp_list.append(weather_data['list'][i]['main']['temp_min'])
    return temp_list


def temp_max(weather_data,date_list ,hour):
    
    temp_list = []
    if hour == -1 :
        for i in range(40) :
            
            date = weather_data['list'][i]['dt_txt']
            for j in date_list:
                if date.count(str(j)) > 0:                                   
                    temp_list.append(weather_data['list'][i]['main']['temp_max'])
        return temp_list
    
    hour = HOUR(hour)
    
    for i in range(40) :
        date = weather_data['list'][i]['dt_txt']
        date = date.split()
        for j in date_list:
            if date[0].count(str(j)) > 0 and date[1].count(hour)>0:                                   
                temp_list.append(weather_data['list'][i]['main']['temp_max'])
    return temp_list

def temp_q(weather_data,date_list,hour):
    temp_list = []
    counter = 0
    if hour == -1:
        for i in range(40) :
            date = weather_data['list'][i]['dt_txt']
            for j in date_list:
                if date.count(str(j)) > 0 :  
                    counter += 1
                    temp_list.append(weather_data['list'][i]['main']['temp'] )
        return temp_list,counter

    hour = HOUR(hour)
        
    for i in range(40) :
        date = weather_data['list'][i]['dt_txt']
        date = date.split()
        for j in date_list:
            if date[0].count(str(j)) > 0 and date[1].count(hour)>0:  
                counter += 1
                temp_list.append(weather_data['list'][i]['main']['temp'] )
    return temp_list,counter

def weather(question,weather_data,date_list,hour = -1):
    
    # if question.count("دما") == 0: return 0 
    if  question.count('میانگین') > 0:
        temp_list,counter = temp_q(weather_data,date_list,hour)
        avrage = sum(temp_list)
        avrage = avrage/counter
        return tempreture(question,avrage)

    elif  question.count('سرد') > 0 or question.count('کمتر') > 0 or question.count('مینیمم') > 0 :
        temp_list = temp_min(weather_data,date_list,hour)
        temp= min(temp_list)
        return tempreture(question,temp)
    
    elif  question.count('گرم') > 0 or question.count('بیشتر') > 0 or question.count('ماکسیمم') > 0:
        temp_list = temp_max(weather_data,date_list,hour)
        temp = max(temp_list)
        return tempreture(question,temp)

def weather_how(question,weather_data,Date,hour = -1):
    Weather = {
        1:"rain",
        2:"drizzle",
        3:"clouds",
        4:"snow",
        5:"thunderstorm",
        6:"clear"
    }

    if hour == -1:
        for i in range(40) :
            date_w = weather_data['list'][i]['dt_txt']
            date_w = date_w.split()
            date_w = date_w[0]
            if date_w.count(str(Date)) > 0:  
                result = weather_data['list'][i]['weather'][0]['description']
                if result.count(Weather[1])>0 or result.count(Weather[2])>0 :
                    return ["بارانی"]
                elif result.count(Weather[3])>0 :
                    return ["ابری"]
                elif result.count(Weather[4])>0 :
                    return ["برفی"]
                elif result.count(Weather[5])>0 :
                    return ["طوفانی"]
                elif result.count(Weather[6])>0 :
                    return ["آفتابی"]
        return []

    hour = HOUR(hour)
    for i in range(40) :
        date_w = weather_data['list'][i]['dt_txt']
        date_w = date_w.split()
        if date_w[0].count(str(Date)) > 0 and date_w[1].count(hour) > 0:  
            result = weather_data['list'][i]['weather'][0]['description']
            if result.count(Weather[1])>0 or result.count(Weather[2])>0 :
                return ["بارانی"]
            elif result.count(Weather[3])>0 :
                return ["ابری"]
            elif result.count(Weather[4])>0 :
                return ["برفی"]
            elif result.count(Weather[5])>0 :
                return ["طوفانی"]
            elif result.count(Weather[6])>0 :
                return ["آفتابی"]
    return []


def weather_city(city1,city2,question,date,time):
    swich = 0
    if question.count("اختلاف") > 0 or question.count("تفاوت") > 0 :
        weather_data = get_weather_data(city1)
        temp_list1 = temp_q(weather_data,[date],time)
        weather_data = get_weather_data(city2)
        temp_list2 = temp_q(weather_data,[date],time)
        return abs(temp_list1[0]-temp_list2[0])
    if question.count("مجموع") > 0 :
        weather_data = get_weather_data(city1)
        temp_list1 = temp_q(weather_data,[date],time)
        weather_data = get_weather_data(city2)
        temp_list2 = temp_q(weather_data,[date],time)
        return abs(temp_list1[0] + temp_list2[0])
    