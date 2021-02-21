from __future__ import unicode_literals
from datetime import *
import time
from persiantools.jdatetime import JalaliDate
from hijri_converter import  convert
import json
import requests
import pandas as pd
import os
from hazm import *

print("i am numberize")

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

def numberize(question):
    normalizer = Normalizer()
    question = normalizer.normalize(question)
    question_word = word_tokenize(question)
    question_word = sign(question_word)
    question_word = adad_adadi(question_word)
    question_word = adad_farsi(question_word)
    return question_word

#get month and year gregorian(miladi) 
#return aladhan json
def aladhan_prim(city = 'تهران',month = [datetime.now().month] ,year = [datetime.now().year]):
    req_list = []
    for i in month:
        req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year)))
        URL = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month={}&year={}".format(city,int(month),int(year))
        req = req.json()
        req_list.append(req)
    return req_list,URL
