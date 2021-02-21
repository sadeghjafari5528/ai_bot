from __future__ import unicode_literals
from datetime import *
import time
from persiantools.jdatetime import JalaliDate
from hijri_converter import  convert
import json
import requests
import pandas as pd
import os

def mah_shamsi_recognition(question_word):
            month_shamsi = {'فروردین':1,'اردیبهشت':2,'خرداد':3,'تیر':4,'مرداد':5,'شهریور':6,'مهر':7,'آبان':8,'ابان':8,'آذر':9,'اذر':9,'دی':10,'بهمن':11,'اسفند':12}
            month = ['اسفند','بهمن','دی','آذر','اذر','آبان','ابان','مهر','شهریور','مرداد','تیر','خرداد','اردیبهشت','فروردین']
            month_shamsi_swich = 0
            n ,m= 0,0
            for i in question_word :
                if month.count(i)> 0 : 
                    month_shamsi_swich = 1
            if month_shamsi_swich == 1 :
                for i in question_word :
                    try:
                        n = month_shamsi[i]
                        m = question_word.index(i)         
                        return month_shamsi_swich,n,m
                    except KeyError:
                        pass
            else : 
                return month_shamsi_swich,n,m

def mah_ghamari_recognition(question_word):
            month_ghamari = {'محرم':1,'صفر':2,'ربیع‌الاول':3,'ربیع‌اول':3,'ربیع‌الثانی':4,'ربیع‌ ثانی':4,'جمادی‌الاول':5,'جمادی اول':5,'جمادی ثانی':6,'جمادی‌الثانی':6,'رجب':7,'شعبان':8,'رمضان':9,'شوال':10,'شوّال':10,'ذیقعده':11,'ذی القعده':11,'ذی قعده':11,'ذی حجه':12,'ذی الحجه':12,'ذیحجه':12}
            month = ['محرم','صفر','شعبان','رمضان','ربیع‌الاول','ربیع‌اول','ربیع‌الثانی','ربیع‌ ثانی','جمادی‌الاول','جمادی اول','جمادی‌الثانی','جمادی ثانی','رجب','ذی قعده','ذیقعده','ذی القعده','شوّال','ذی حجه','ذی الحجه','ذیحجه','شوال'] 
            month_ghamari_swich = 0
            month_ghamari_list = []
            n,m = 0,0
            for i in question_word :
                if month.count(i)> 0 :
                    month_ghamari_swich = 1
            if month_ghamari_swich == 1:
                for i in question_word :
                    try:
                        n = month_ghamari.get(str(i))
                        month_ghamari_list.append(month_ghamari[str(i)])
                        m = question_word.index(i)
                        month_ghamari_swich = 1
                        return month_ghamari_swich,n,m          
                    except KeyError:
                        pass
            else : 
                return month_ghamari_swich,n,m

def mah_miladi_recognition(question_word):
            month_miladi = {'ژانویه':1,'فوریه':2,'مارچ':3,'مارس':3,'آپریل':4,'آوریل':4,'اوریل':4,'مه':5,'می':5,'جون':6,'ژوئن':6,'جولای':7,'ژوئیه':7,'آگوست':8,'اگوست':8,'آگست':8,'اگست':8,'سپتامبر':9,'سپتمبر':9,'اکتبر':10,'نوامبر':11,'نومبر':11,'دسامبر':12}
            month = ['ژانویه','فوریه','مارچ','مارس','آپریل','اپریل','آوریل','اوریل','مه','می','جون','ژوئن','جولای','ژوئیه','آگوست','اگوست','آگست','اگست','سپتامبر','سپتمبر','اکتبر','نوامبر','نومبر','دسامبر']
            #month = ['January','February','March','April','May','June','July','August','September','October','November','December']
            #month_miladi = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
            month_miladi_swich = 0
            month_miladi_list = []
            n,m = 0,0
            for i in question_word :
                if month.count(i)> 0 :
                    month_miladi_swich = 1
            if month_miladi_swich == 1 :
                for i in question_word :
                    try:
                        n = month_miladi.get(str(i))
                        month_miladi_list.append(month_miladi[str(i)])
                        m = question_word.index(i)
                        month_miladi_swich = 1
                        return month_miladi_swich,n,m
                    except KeyError:
                        pass
            else :
                return month_miladi_swich,n,m

def tarikh_shamsi(question_word,year_shamsi,year):
            b = 0
            month = []
            if mah_shamsi_recognition(question_word)[0] == 1:
                m = 0
                n = mah_shamsi_recognition(question_word)[2]
                if type(question_word[n-1]) == int :
                    if year_shamsi == 1 :
                        b = JalaliDate(year,mah_shamsi_recognition(question_word)[1],question_word[n-1])
                        month.append(b)
                        #c = b.split("-")
                        #c = (c[0],c[1],c[2])        
                        m = 1
                        return b,m,month
                    else:    
                        b = JalaliDate(1399,mah_shamsi_recognition(question_word)[1],question_word[n-1])
                        month.append(b)
                        m = 0
                        return b , m ,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
                else:
                    return b ,m ,month
            else:
                m = -1
                return b ,m ,month

def tarikh_ghamari(question_word,year_ghamari,year):
            b = 0
            month = []
            if mah_ghamari_recognition(question_word)[0] == 1:
                m = 0
                n = mah_ghamari_recognition(question_word)[2]
                if type(question_word[n-1]) == int :
                    if year_ghamari == 1 : 
                        b = convert.Hijri(year,mah_ghamari_recognition(question_word)[1],question_word[n-1])
                        month.append(b)
                        m = 1
                        return b,m,month
                    else:    
                        b = convert.Hijri(1442,mah_ghamari_recognition(question_word)[1],question_word[n-1]) 
                        month.append(b)  
                        m =0
                        return b , m,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
                else:
                    return b ,m ,month
            else:
                m = -1
                return b ,m ,month

def tarikh_miladi(question_word,year_miladi,year):
            month = []
            b = 0
            if mah_miladi_recognition(question_word)[0] == 1:
                m = 0
                n = mah_miladi_recognition(question_word)[2]
                if type(question_word[n-1]) == int :
                    if year_miladi == 1 :    
                        b = datetime(year,mah_miladi_recognition(question_word)[1],question_word[n-1])
                        c = str(b)
                        c = c.split()
                        month.append(c[0])
                        m = 1
                        return b,m,month
                    else:    
                        b = datetime(2020,mah_miladi_recognition(question_word)[1],question_word[n-1])      
                        c = str(b)
                        c = c.split()
                        month.append(c[0])
                        m =0
                        return b , m ,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
                else:
                    return b ,m ,month
            else:
                m = -1
                return b ,m ,month 

def azan(jsoninf):
    return ""

def azan_sob(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Fajr"].split()
            return data[0],URL

def azan_zohr(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Dhuhr"].split()
            return data[0],URL

def azan_maghreb(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Maghrib"].split()
            return data[0],URL

def azan_asr(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Asr"].split()
            return data[0],URL

def azan_asha(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Isha"].split()
            return data[0],URL

def goroob(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Sunset"].split()
            return data[0],URL

def tolo(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Sunrise"].split()
            return data[0],URL

def midnight(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Midnight"].split()
            return data[0],URL

def imsak(city = 'تهران',day = datetime.now().day ,month = datetime.now().month ,year = datetime.now().year):
            req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
            URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
            req = req.json()
            data = req["data"][int(day)-1]["timings"]["Imsak"].split()
            time_imsak = data[0]
            return time_imsak,URL

def sign(question_word):
    sign = ["ام","امین","؟","،","!",".","/","?","#","$","%","^","&","*","(",')','[',"]",'{',"}","-","_","=","+"]
    for i in sign :
        try:
            question_word.remove(i)
        except ValueError:
            pass
        return question_word
        #adad adadi

def adad_adadi(question_word) :
    for i in question_word :
        try:
            n = int(i)
            m = question_word.index(i)
            question_word[m] = n
        except ValueError:
            pass
    return question_word

def adad_farsi(question_word):
    
    number_10 = ['بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود']
    NUMBER_LIST = ['سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود','بیست','نوزده','هجده','هفده','شانزده','پانزده','چهارده','سیزده','دوازده','یازده','ده','نه','هشت','هفت','شش','پنج','چهار','سه','دو','یک']
    NUMBER_LIST_OM = ['بیستم','نوزدهم','هجدهم','هفدهم','شانزدهم','پانزدهم','چهاردهم','سیزدهم','دوازدهم','یازدهم','دهم','نهم','هشتم','هفتم','ششم','پنجم','چهارم','سوم','دوم','یکم','سیم']
    number_dic_om = {'یکم':1,'دوم':2,'سوم':3,'چهارم':4,'پنجم':5,'ششم':6,'هفتم':7,'هشتم':8,'نهم':9,'دهم':10,'یازدهم':11,'دوازدهم':12,'سیزدهم':13,'چهارده':14,'پانزدهم':15,'شانزدهم':16,'هفدهم':17,'هجدهم':18,'نوزدهم':19,'بیستم':20,'سیم':30}
    NUMBER_LIST_OMIN = ['بیستمین','نوزدهمین','هجدهمین','هفدهمین','شانزدهمین','پانزدهمین','چهاردهمین','سیزدهمین','دوازدهمین','یازدهمین','دهمین','نهمین','هشتمین','هفتمین','ششمین','پنجمین','چهارمین','سومین','دومین','یکمین','سیمین']
    number_dic_omin = {'یکمین':1,'دومین':2,'سومین':3,'چهارمین':4,'پنجمین':5,'ششمین':6,'هفتمین':7,'هشتمین':8,'نهمین':9,'دهمین':10,'یازدهمین':11,'دوازدهمین':12,'سیزدهمین':13,'چهاردهین':14,'پانزدهمین':15,'شانزدهمین':16,'هفدهمین':17,'هجدهمین':18,'نوزدهمین':19,'بیستمین':20,'سیمین':30}
    number_dic = {'یک':1,'دو':2,'سه':3,'چهار':4,'پنج':5,'شش':6,'هفت':7,'هشت':8,'نه':9,'ده':10,'یازده':11,'دوازده':12,'سیزده':13,'چهارده':14,'پانزده':15,'شانزده':16,'هفده':17,'هجده':18,'نوزده':19,'چهل':40,'پنجاه':50,'شصت':60,'هفتاد':70,'هشتاد':80,'نود':90,'بیست':20,'سی':30}
   
    for i in NUMBER_LIST:
        if question_word.count(i)> 0 :
            m = question_word.index(i)
            if  question_word[m] in number_10 :
                if question_word[m+1] == 'و' and NUMBER_LIST.count(question_word[m+2]) >0 :
                    n = number_dic[question_word[m+2]] + number_dic[question_word[m]]
                    question_word[m] = n        
                    question_word.remove(question_word[m+1])        
                    question_word.remove(question_word[m+1])
                elif question_word[m+1] == 'و' and NUMBER_LIST_OM.count(question_word[m+2]) >0 :
                    n = number_dic_om[question_word[m+2]] + number_dic[question_word[m]]
                    question_word[m] = n        
                    question_word.remove(question_word[m+1])        
                    question_word.remove(question_word[m+1])
                elif question_word[m+1] == 'و' and NUMBER_LIST_OMIN.count(question_word[m+2]) > 0 :
                    n = number_dic_omin[question_word[m+2]] + number_dic[question_word[m]]
                    question_word[m] = n        
                    question_word.remove(question_word[m+1])        
                    question_word.remove(question_word[m+1])
                else :#question_word[m+1] == 'و' and NUMBER_LIST.count(question_word[m+2])==0 :
                    n = number_dic[i]
                    question_word[m] = n
            else:
                n = number_dic[i]
                question_word[m] = n
    for i in NUMBER_LIST_OMIN:
        if question_word.count(i)> 0 :
            m = question_word.index(i)
            n = number_dic_omin[i]
            question_word[m] = n
    for i in NUMBER_LIST_OM:
        if question_word.count(i)> 0 :
            m = question_word.index(i)
            n = number_dic_om[i]
            question_word[m] = n
    return question_word

def location_excel_read_data():
        location = []
        df = pd.read_excel('location.xlsx')
        loc = df.values.tolist()
        for i in range(len(loc)):
            location.append(loc[i][0])
        return location

def Location_Recognition(question_word):
    final_city = []
    location_swich = 0
    city = location_excel_read_data()
    for i in question_word :
        if city.count(i)>0 :
            location_swich = 1
            location = i
            final_city.append(location)
    return location_swich,final_city

def Clock(question_word):
    swich,hour,minute = 0,0,0
    for i in question_word:
        try:
            if i.count(":")>0:
                # m = question_word.index(i)
                time_list = i.split(':')
                time_list = adad_farsi(time_list)
                # question_word.remove(i)
                hour = time_list[0]
                minute = time_list[1]
                # question_word.insert(m,time_list[0])
                # question_word.insert(m+1,time_list[1])
                swich = 1
        except AttributeError:
            continue
    return swich,hour,minute

def ghabl_bad(question_word,number_days,i):
    date_list = []
    m = question_word.index(i)
    DAYS = 0
    if m != 0:
        if type(question_word[m-1]) == int :
            days = question_word[m-1]*number_days
            if question_word[m+1] == 'گذشته' or question_word[m+1] == 'قبل' or question_word[m+1] == 'پیش' :
                DAYS = 1
                days = days*(-1)
                for i in range(days,0):
                    date_1 = date.today() + timedelta(i)
                    date_list.append(date_1)
                return DAYS,date_list

            elif question_word[m+1] == 'آینده' or question_word[m+1] == 'بعد' or question_word[m+1] == 'اینده':
                days = days*(1)
                for i in range(1,days + 1):
                    date_1= date.today() + timedelta(i)
                    date_list.append(date_1)
                return DAYS,date_list
            else:
                return DAYS,date_list
    else:
        return DAYS,date_list

def temp(question_word , temp):
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

def get_weather_data(city='تهران',appid='80e7b34a80616c9ae8e75e7be510c8b9',):
            URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(city,appid)
            r = requests.get(URL) 
            data = (r.json()).copy()
            return r.json(),URL

def weather_avrage(question, question_date_list,weather_data):
    avrage = 0
    if  question.count('میانگین') > 0:
        if len(question_date_list) > 0 :
            for i in range(40) :
                date_2 = weather_data['list'][i]['dt_txt']
                date_2  = date_2 .split()
                date_2  = date_2 [0]
                for j in question_date_list:
                    if date_2  == str(j):
                        counter += 1
                        avrage = weather_data['list'][i]['main']['temp'] + avrage
            temp = avrage/counter
            return temp(question,temp)

def weather_min(question,question_date_list,weather_data):
    temp_list = []
    for i in range(40) :
        date_2  = weather_data['list'][i]['dt_txt']
        date_2  = date_2 .split()
        date_2  = date_2 [0]
        for j in question_date_list:
            if date_2  == str(j):                                   
                temp_list.append(weather_data['list'][i]['main']['temp_min'])
    temp = min(temp_list)       
    return temp(question,temp)

def weather_max(question,question_date_list,weather_data):
    temp_list = []
    for i in range(40) :
        date_2  = weather_data['list'][i]['dt_txt']
        date_2  = date_2 .split()
        date_2  = date_2 [0]
        for j in question_date_list:
            if date_2  == str(j):                                   
                temp_list.append(weather_data['list'][i]['main']['temp_max'])
    temp = max(temp_list)       
    return temp(question,temp)

