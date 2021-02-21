#in the name of Allah

from numberize import *


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
                return m,month
            else:    
                b = JalaliDate(1399,mah_shamsi_recognition(question_word)[1],question_word[n-1])
                month.append(b)
                m = 0
                return  m ,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
        else:
            return m ,month
    else:
        m = -1
        return m ,month

def mah_ghamari_recognition(question_word):
    month_ghamari = {'محرم':1,'صفر':2,'ربیع‌الاول':3,'ربیع‌اول':3,'ربیع‌الثانی':4,'ربیع‌ ثانی':4,'جمادی‌الاول':5,'جمادی اول':5,'جمادی ثانی':6,'جمادی‌الثانی':6,'رجب':7,'شعبان':8,'رمضان':9,'شوال':10,'شوّال':10,'ذیقعده':11,'ذی القعده':11,'ذی قعده':11,'ذی حجه':12,'ذی الحجه':12,'ذیحجه':12}
    month = ['محرم','صفر','شعبان','رمضان','ربیع‌الاول','ربیع‌اول','ربیع‌الثانی','ربیع‌ ثانی','جمادی‌الاول','جمادی اول','جمادی‌الثانی','جمادی ثانی','رجب','ذی قعده','ذیقعده','ذی القعده','شوّال','ذی حجه','ذی الحجه','ذیحجه','شوال'] 
    month_ghamari_swich = 0
    month_ghamari_list = []
    n,m = 0,0
    for i in question_word :
        if month.count(i)> 0 :
             month_ghamari_swich = 1
             break
    # for i in month :
    #     if question.count(i)> 0 :
    #         month_ghamari_swich = 1
    #         break
    #question_word = numberize(question)
    if month_ghamari_swich == 1:
        for i in question_word :
            try:
                n = month_ghamari.get(str(i))
                month_ghamari_list.append(month_ghamari[str(i)])
                m = question_word.index(i)
                return month_ghamari_swich,n,m          
            except KeyError:
                pass
    else : 
        return month_ghamari_swich,n,m

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
                return m,month
            else:    
                b = convert.Hijri(1442,mah_ghamari_recognition(question_word)[1],question_word[n-1]) 
                month.append(b)  
                m =0
                return m,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
        else:
            return m ,month
    else:
        m = -1
        return m ,month

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
                return m,month
            else:    
                b = datetime(2020,mah_miladi_recognition(question_word)[1],question_word[n-1])      
                c = str(b)
                c = c.split()
                month.append(c[0])
                m =0
                return m ,month# m baraye in ke befahmim tarikh darim ya na 1=darim ,0 = faghat mah darim ,-1= mah nadarim
        else:
            return m ,month
    else:
        m = -1
        return m ,month 


def ghabl_bad_date(question_word,number_days,i):
    date_list = []
    #question_word = word_tokenize(text)
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
# input = text
# output = datetime obj
# 
def dateParser(question):
    
    year_ghamari,year_miladi,year_shamsi= 0,0,0
    year_ghamari,year_shamsi,year_miladi = 0,0,0
    year = 0

    date_list = []
    question_word = numberize(question)

    for i in question_word:
        i_place = question_word.index(i)
        if i == 'پریروز'  :
            date_list.append(date.today()+ timedelta(-2))
        if i == 'امروز':
            date_list.append(date.today())
        if i == 'دیروز' :
            date_list.append(date.today()+ timedelta(-1))
        if ((i == 'پس' and question_word[i_place+1] == 'فردا' ) or i == 'پسفردا'):
            date_list.append(date.today()+ timedelta(2))
        if i == 'فردا' :
            date_list.append(date.today()+ timedelta(1))
        
        elif i == "امسال":
            year = date.today().year
        elif i == "پارسال":
            year = date.today().year - 1
        elif i == "پیارسال":
            year = date.today().year-2

    for i in question_word:
        if i == ("هفته"):
            number_days = 7
            date_list = ghabl_bad_date(question_word,number_days,i)

        elif i == ("ماه"):
            month = 30
            date_list = ghabl_bad_date(question_word,number_days,i)

        elif i == ("روز"):
            number_days = 1
            date_list = ghabl_bad_date(question_word,number_days,i)

    for n in question_word:
        if type(n) == int:
            if n > 1900 :
                year_miladi = 1
                year = n
            elif n > 1420 and n < 1600:
                year = n
                year_ghamari = 1
            if mah_shamsi_recognition(question_word)[0] == 1 and n > 50 and n <= 99 :
                year = n + 1300
                year_shamsi = 1
            elif n > 1350 and n < 1420 :
                year = n
                year_shamsi = 1 

    if tarikh_ghamari(question_word,year_ghamari,year)[0] == 1:
        date_list.append(tarikh_ghamari(question_word,year_ghamari,year)[1])
        return date_list,year

    elif tarikh_shamsi(question_word,year_shamsi,year)[0] == 0:
        date_list.append(tarikh_shamsi(question_word,year_shamsi,year)[1])
        return date_list,year
    
    elif tarikh_miladi(question_word, year_miladi,year)[0]==0:
        date_list.append(tarikh_miladi(question_word, year_miladi,year)[1])
        return date_list,year
    return date_list,year