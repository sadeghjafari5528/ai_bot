from config import *
from numberize import *

#get month and year gregorian(miladi) 
#return aladhan json
def aladhan(city = "تهران",date = date.today()):
    month = date.today().month
    year = date.today().year
    req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
    URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
    req = req.json()
    return req,date,URL

def azan(jsonAladhan,question , date):
    question_word = numberize(question)
    print(question_word)
    day = date.today().day
    for i in question_word:
        if i == "اذان" :
            if question_word.count("صبح") > 0:
                data = jsonAladhan["data"][int(day)-1]["timings"]["Fajr"].split()
                return data[0]
            elif question_word.count("ظهر") > 0:
                data = jsonAladhan["data"][int(day)-1]["timings"]["Dhuhr"].split()
                return data[0]
            elif question_word.count("عصر") > 0:
                data = jsonAladhan["data"][int(day)-1]["timings"]["Asr"].split()
                return data[0]
            elif question_word.count("مغرب") > 0:
                data = jsonAladhan["data"][int(day)-1]["timings"]["Maghrib"].split()
                return data[0]
            elif question_word.count("عشا") > 0:
                data = jsonAladhan["data"][int(day)-1]["timings"]["Isha"].split()
                return data[0]
        elif question.count('امساک') > 0 :
            data = jsonAladhan["data"][int(day)-1]["timings"]["Imsak"].split()
            return data[0]
        elif question.count('غروب') > 0 :
            data = jsonAladhan["data"][int(day)-1]["timings"]["Sunset"].split()
            return data[0]
        elif question.count('طلوع') > 0 :
            data = jsonAladhan["data"][int(day)-1]["timings"]["Sunrise"].split()
            return data[0]
        elif question.count('نیمه') > 0 and question.count('شب') > 0  and question.count('شرعی') > 0 :
            data = jsonAladhan["data"][int(day)-1]["timings"]["Midnight"].split()
            return data[0]
