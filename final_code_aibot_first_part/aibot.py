#in the name of Allah

from config import *
from functions import *

class BOT:
    def __init__(self):
        self.modified = False

    def is_modified(self):
        return self.modified

    def AIBOT(self, question):
    
        normalizer = Normalizer()
        question = normalizer.normalize(question)
        question_word = word_tokenize(question)
        
        question_word = sign(question_word)
        question_word = adad_adadi(question_word)
        question_word = adad_farsi(question_word)
        location_swich , final_city = Location_Recognition(question_word)
        if location_swich == 1 :
            answer['city'] = final_city

        for n in question_word:
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

        #3:20
        clock = Clock(question_word)
        clock_swich = clock[0]
        if clock_swich == 1:
            hour = clock[1]
            minute = clock[2]
        a = 0
        for i in question_word :
            if i == "هفته" :
                a = ghabl_bad(question_word,WEEK,i)
                if a[0] == 1 :
                    break
        for i in question_word :
            if i == "روز" :
                a = ghabl_bad(question_word,DAY,i)
                if a[0] == 1 :
                    break
        for i in question_word :
            if i == "ماه" :
                a = ghabl_bad(question_word,MONTH,i)
                if a[0] == 1 :
                    break
        print(a)
        for i in question_word:
            i_place = question_word.index(i)
            if i == 'پریروز'  :
                question_date_list.append(date.today()+ timedelta(-2))
                date_list.append(date.today()+ timedelta(-2))
            if i == 'امروز':
                question_date_list.append(date.today())
                date_list.append(date.today())
            if i == 'دیروز' :
                question_date_list.append(date.today()+ timedelta(-1))
                date_list.append(date.today()+ timedelta(-1))
            if ((i == 'پس' and question_word[i_place+1] == 'فردا' ) or i == 'پسفردا'):
                question_date_list.append(date.today()+ timedelta(2))
                date_list.append(date.today()+ timedelta(2))
                question_word.remove(question_word[i_place+1])
            elif i == 'فردا' :
                question_date_list.append(date.today()+ timedelta(1))
                date_list.append(date.today()+ timedelta(1))

        for i in tempreture:
            if question.count(i) > 0 :
                if location_swich == 1:
                    loc = location
                    weather_data ,api_url= get_weather_data(loc)
                    temp = weather_avrage(question,question_date_list,weather_data)

                    if  question.count('سرد') > 0 or question.count('کمتر') > 0 or question.count('مینیمم') > 0 :
                        if len(question_date_list) > 0 :
                            weather_data ,api_url= get_weather_data(loc)
                            temp = weather_min(question,question_date_list,weather_data)

                    elif  question.count('گرم') > 0 or question.count('بیشتر') > 0 or question.count('ماکسیمم') > 0:
                        if len(question_date_list) > 0 :
                            temp = 0
                            weather_data ,api_url= get_weather_data(loc)
                            temp = weather_max(question,question_date_list,weather_data)

                    else:
                        if len(question_date_list) > 0 :
                            temp = 0
                            weather_data ,api_url= get_weather_data(loc)
                            for i in range(40) :
                                date_2  = weather_data['list'][i]['dt_txt']
                                date_2  = date_2 .split()
                                date_2  = date_2 [0]
                                for j in question_date_list:
                                    if date_2  == str(j):                                   
                                        temp = weather_data['list'][i]['main']['temp']
                            temp(question,temp)
                        else:
                            weather_data ,api_url= get_weather_data(loc)
                            temp = weather_data['list'][0]['main']['temp']
                            temp(question,temp)


                else :
                    weather_data = get_weather_data()
                    temp = weather_avrage(question,question_date_list,weather_data)

                    if  question.count('سرد') > 0 or question.count('کمتر') > 0 or question.count('مینیمم') > 0:
                        if len(question_date_list) > 0 :
                            weather_data ,api_url= get_weather_data()
                            temp = weather_min(question,question_date_list,weather_data)

                    elif  question.count('گرم') > 0 or question.count('بیشتر') > 0 or question.count('ماکسیمم') > 0:
                        if len(question_date_list) > 0 :
                            weather_data ,api_url= get_weather_data()
                            temp = weather_max(question,question_date_list,weather_data)

                    else:
                        if len(question_date_list) > 0 :
                            temp = 0
                            weather_data ,api_url= get_weather_data()
                            for i in range(40) :
                                date_2  = weather_data['list'][i]['dt_txt']
                                date_2  = date_2 .split()
                                date_2  = date_2 [0]
                                for j in question_date_list:
                                    if date_2  == str(j):                                   
                                        temp = weather_data['list'][i]['main']['temp']
                            temp(question,temp)

                        else :
                            weather_data ,api_url= get_weather_data()
                            temp = weather_data['list'][0]['main']['temp']
                            temp(question,temp)

        for i in question_word :
            if i == "ساعت" :
                m = question_word.index(i)
                if type(question_word[m+1]) == int :
                    if question_word[m+2] == 'و' and type(question_word[m+3]) == int and question_word[m+4] == 'دقیقه' :
                        hour = question_word[m+1]
                        minute = question_word[m+3]
                    if question.count('بعد از ظهر') > 0 or question_word[m+2] == 'بعدازظهر' or question_word[m+2] == 'عصر' :
                        if question_word[m+1] <= 12:
                            question_word[m+1] + 12
                            if question_time == 24 :
                                question_time = 0
                                hour = question_time
                            else:
                                question_word[m+1] = question_time
                                hour = question_time
                        else:
                            hour = question_word[m+1]
                    else:
                        hour = question_word[m+1]

            if i == 'دقیقه':
                minute_swich = 1
                m = question_word.index(i)
                if type(question_word[m-1]) == int :
                    minute = question_word[m-1]
            if hour_swich==1 and minute_swich==1:
                question_time = datetime(2021,1,4,hour = hour, minute = minute, second = 0)
                question_time = datetime.strftime(question_time, '%H:%M')
                question_time_list.append(question_time)
            elif hour_swich==1:
                question_time = datetime(2021,1,4,hour = hour, minute = 0, second = 0)
                question_time = datetime.strftime(question_time, '%H:%M')
                question_time_list.append(question_time)
        #time recognition
        now = datetime.now()
        for i in question_word :
            if i == "ساعت" :
                m = question_word.index(i)
                #saat 2 soal
                if type(question_word[m+1]) == int :
                    question_time = question_word[m+1]
                #2 saat ayande/gozashte
                if m != 0 and len(question_word) >= m+2:
                    if type(question_word[m-1]) == int :
                        hour = question_word[m-1]
                    if question_word[m+1] == 'بعد' or question_word[m+1] == 'آینده' or question_word[m+1] == 'اینده':
                        question_time = now + timedelta(hours = hour)
                        question_time = datetime.strftime(question_time, '%H:%M')
                        question_time_list.append(question_time)             
                        time_swich = 1
                        if len(question_word) >= m+4:
                            time_swich = 1
                            if ((question_word[m+2] == 'در'or question_word[m+2] == 'تو')and(question_word[m+3] == location)):
                                req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                                api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                                req = req.json()
                                timezone = req["data"][0]["meta"]["timezone"]
                                timezone = pytz.timezone(timezone)
                                timezone = datetime.now(timezone) + timedelta(hours = hour)
                                timezone = datetime.strftime(timezone, '%H:%M')
                                question_time_list.append(timezone)    
                        elif len(question_word) >= m+5:
                            time_swich = 1   
                            if ((question_word[m+2] == 'در'or question_word[m+2] == 'تو')and(question_word[m+4] == location)):
                                req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                                api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                                req = req.json()
                                timezone = req["data"][0]["meta"]["timezone"]
                                timezone = pytz.timezone(timezone)
                                timezone = datetime.now(timezone) + timedelta(hours = hour)
                                timezone = datetime.strftime(timezone, '%H:%M')
                                question_time_list.append(timezone)    
                        else:
                            question_time = now + timedelta(hours = hour)
                            question_time = datetime.strftime(question_time, '%H:%M')
                            question_time_list.append(question_time)
                            time_swich = 1
                    elif question_word[m+1] == 'قبل' or question_word[m+1] == 'گذشته'or question_word[m+1] == 'پیش' :
                        hour = hour*(-1)
                        if len(question_word) >= m+4:        
                            if ((question_word[m+2] == 'در'or question_word[m+2] == 'تو')and(question_word[m+3] == location)):
                                time_swich = 1
                                req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                                api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                                req = req.json()
                                timezone = req["data"][0]["meta"]["timezone"]
                                timezone = pytz.timezone(timezone)
                                timezone = datetime.now(timezone) + timedelta(hours = hour)
                                timezone = datetime.strftime(timezone, '%H:%M')
                                question_time_list.append(timezone)
                        elif len(question_word) >= m+5:        
                            if ((question_word[m+2] == 'در'or question_word[m+2] == 'تو')and(question_word[m+4] == location)):
                                time_swich = 1
                                req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                                api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                                req = req.json()
                                timezone = req["data"][0]["meta"]["timezone"]
                                timezone = pytz.timezone(timezone)
                                timezone = datetime.now(timezone) + timedelta(hours = hour)
                                timezone = datetime.strftime(timezone, '%H:%M')
                                question_time_list.append(timezone)    
                        else:
                            question_time = now + timedelta(hours = hour)
                            question_time = datetime.strftime(question_time, '%H:%M')
                            question_time_list.append(question_time)
                #saat keshvar ha   
                if len(question_word) >= m+2:        
                    if question_word[m+1] == location :
                        time_swich = 1
                        req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                        api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                        req = req.json()
                        timezone = req["data"][0]["meta"]["timezone"]
                        timezone = pytz.timezone(timezone)
                        timezone = datetime.now(timezone)
                        timezone = datetime.strftime(timezone, '%H:%M')
                        question_time_list.append(timezone)
                if len(question_word) >= m+3:        
                    if question_word[m+2] == location :
                        time_swich = 1
                        req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                        api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)                
                        req = req.json()
                        timezone = req["data"][0]["meta"]["timezone"]
                        timezone = pytz.timezone(timezone)
                        timezone =datetime.now(timezone)
                        question_time = timezone
                        question_time = datetime.strftime(question_time, '%H:%M')
                        question_time_list.append(question_time)
                if m != 0 and len(question_word) >= m+3:
                    if question_word[m-1] == location and  question_word[m+1] != "اذان" and  question_word[m+1] != "قضا":
                        time_swich = 1
                        req = requests.get("http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location))
                        api_url = "http://api.aladhan.com/v1/calendarByCity?city={}&country= &method=7&month=5&year=2020".format(location)
                        req = req.json()
                        timezone = req["data"][0]["meta"]["timezone"]
                        timezone = pytz.timezone(timezone)
                        timezone =datetime.now(timezone)
                        question_time = timezone
                        question_time = datetime.strftime(question_time, '%H:%M')
                        question_time_list.append(question_time)




        #religios_Azan
        if tarikh_ghamari(question_word,year_ghamari,year)[1] > -1:
            Tarikh_ghamari = tarikh_ghamari(question_word,1,year)[0]
            miladi_convert = convert.Hijri(Tarikh_ghamari.year, Tarikh_ghamari.month, Tarikh_ghamari.day).to_gregorian()
            question_date_list.append(miladi_convert)
            tarikh_miladi_swich = 1

        if tarikh_shamsi(question_word,year_shamsi,year)[1] > -1:
            Tarikh_shamsi = tarikh_shamsi(question_word,1,year)[0]
            miladi_convert = JalaliDate(Tarikh_shamsi.year, Tarikh_shamsi.month, Tarikh_shamsi.day).to_gregorian()
            question_date_list.append(miladi_convert)    
            tarikh_miladi_swich = 1

        if tarikh_miladi(question_word,year_miladi,year) [1] > -1:
            miladi = tarikh_miladi(question_word,year_miladi,year)[0]
            question_date_list.append(miladi)

        for i in question_word:
            if i == "اذان" :
                m = question_word.index(i) 
                if question_word[m+1] == "صبح":
                    religious_swich = 1
                    final_religious_time.append('اذان صبح')
                    if location_swich == 1 and tarikh_miladi_swich == 1:        #shamsi 
                        sharii , api_url = azan_sob(location,miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif location_swich == 1 and tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_sob(location,miladi.day,miladi.month,miladi.year)
                    elif tarikh_miladi_swich == 1:
                        sharii , api_url = azan_sob('تهران',miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif tarikh_miladi(question_word,year_miladi,year) [1] == 1:           #miladi
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_sob('تهران',miladi.day,miladi.month,miladi.year)
                    elif location_swich == 1:
                        sharii , api_url = azan_sob(location)
                    else:
                        sharii , api_url = azan_sob()
                elif question_word[m+1] == "ظهر":
                    religious_swich = 1
                    final_religious_time.append('اذان ظهر')
                    if location_swich == 1 and tarikh_miladi_swich == 1:
                        sharii , api_url = azan_zohr(location,miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif location_swich == 1 and tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_zohr(location,miladi.day,miladi.month,miladi.year)
                    elif tarikh_miladi_swich == 1:
                        sharii , api_url = azan_zohr('تهران',miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_zohr('تهران',miladi.day,miladi.month,miladi.year)
                    elif location_swich == 1:
                        sharii , api_url = azan_zohr(location)
                    else:
                        sharii , api_url = azan_zohr()

                elif question_word[m+1] == "مغرب":
                    religious_swich = 1
    
                    final_religious_time.append('اذان مغرب')
                    if location_swich == 1 and tarikh_miladi_swich == 1:
                        sharii , api_url = azan_maghreb(location,miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif location_swich == 1 and tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_maghreb(location,miladi.day,miladi.month,miladi.year)
                    elif tarikh_miladi_swich == 1:
                        sharii , api_url = azan_maghreb('تهران',miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_maghreb('تهران',miladi.day,miladi.month,miladi.year)
                    elif location_swich == 1:
                        sharii , api_url = azan_maghreb(location)
                    else:
                        sharii , api_url = azan_maghreb()
                if question_word[m+1] == "عصر" :
                    religious_swich = 1
    
                    if location_swich == 1 and tarikh_miladi_swich == 1:
                        sharii , api_url = azan_asr(location,miladi_convert.day,miladi_convert.month,miladi_convert.year)
                        final_religious_time.append('اذان عصر')
                    elif location_swich == 1 and tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_asr(location,miladi.day,miladi.month,miladi.year)
                        final_religious_time.append('اذان عصر')
                    elif tarikh_miladi_swich == 1:
                        sharii , api_url = azan_asr('تهران',miladi_convert.day,miladi_convert.month,miladi_convert.year)
                        final_religious_time.append('اذان عصر')
                    elif tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_asr('تهران',miladi.day,miladi.month,miladi.year)
                        final_religious_time.append('اذان عصر')
                    elif location_swich == 1:
                        sharii , api_url = azan_asr(location)
                        final_religious_time.append('اذان عصر')
                    else:
                        sharii , api_url = azan_asr()
                        final_religious_time.append('اذان عصر')

                if question_word[m+1] == "عشا":
                    religious_swich = 1
    
                    final_religious_time.append('اذان عشا')
                    if location_swich == 1 and tarikh_miladi_swich == 1:        #shamsi 
                        sharii , api_url = azan_asha(location,miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif location_swich == 1 and tarikh_miladi(question_word,year_miladi,year) [1] == 1:
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_asha(location,miladi.day,miladi.month,miladi.year)
                    elif tarikh_miladi_swich == 1:
                        sharii , api_url = azan_asha('تهران',miladi_convert.day,miladi_convert.month,miladi_convert.year)
                    elif tarikh_miladi(question_word,year_miladi,year) [1] == 1:           #miladi
                        miladi = tarikh_miladi(question_word,year_miladi,year)[0]
                        sharii , api_url = azan_asha('تهران',miladi.day,miladi.month,miladi.year)
                    elif location_swich == 1:
                        sharii , api_url = azan_asha(location)
                    else:
                        sharii , api_url = azan_asha()

        if question.count('امساک') > 0 :
            final_religious_time.append('امساک')
            religious_swich = 1
            if location_swich == 1 :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = imsak(location,i.day,i.month,i.year)
            else :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = imsak('تهران',i.day,i.month,i.year)
                        final_religious_time.append('امساک')

        if question.count('غروب') > 0 :
            religious_swich = 1
            if location_swich == 1 :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = goroob(location,i.day,i.month,i.year)
                        final_religious_time.append('غروب آفتاب')
            else :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = goroob('تهران',i.day,i.month,i.year)
                        final_religious_time.append('غروب آفتاب')

        if question.count('طلوع') > 0 :
            religious_swich = 1
            if location_swich == 1 :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = tolo(location,i.day,i.month,i.year)
                        final_religious_time.append('طلوع آفتاب')
            else :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = tolo('تهران',i.day,i.month,i.year)
                        final_religious_time.append('طلوع آفتاب')

        if question.count('نیمه') > 0 and question.count('شب') > 0  and question.count('شرعی') > 0 :
            religious_swich = 1
            if location_swich == 1 :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = midnight(location,i.day,i.month,i.year)
                        final_religious_time.append('نیمه شب شرعی')
            else :
                for i in question_date_list :
                    if len(question_date_list) > 0 :
                        sharii , api_url = midnight('تهران',i.day,i.month,i.year)
                        final_religious_time.append('نیمه شب شرعی')


                
               
        for i in question_word:
            if i == 'روز':
                m = question_word.index(i)
                if question_word[m+1] == 'جهانی':
                    try:
                        question_event_date = miladi_dic[question_word[m+2]]
                        event_swich = 1
                        question_event_date = datetime(2020,question_event_date[1],question_event_date[0])
                        question_monasebat.append(datetime.strftime(question_event_date, '%Y%m-%d'))
                    except KeyError :
                        pass
                else:
                    try:
                        question_event_date = shamsi_dic[question_word[m+1]]
                        event_swich = 1
                        question_event_date = datetime(1399,question_event_date[1],question_event_date[0])
                        question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                    except KeyError:
                        pass
                    try:
                        question_event_date = ghamari_dic[question_word[m+1]]
                        event_swich = 1
                        question_event_date = datetime(1442,question_event_date[1],question_event_date[0])
                        question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                    except KeyError:
                        pass
                    try:
                        question_event_date = miladi_dic[question_word[m+1]]
                        event_swich = 1
                        question_event_date = datetime(2020,question_event_date[1],question_event_date[0])
                        question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                    except KeyError :
                        pass
            if i == 'شب':
                m = question_word.index(i)
                try:
                    question_event_date = shamsi_dic[question_word[m+1]]
                    event_swich = 1
                    question_event_date = datetime(1399,question_event_date[1],question_event_date[0])
                    question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                except KeyError:
                    pass
                try:
                    question_event_date = ghamari_dic[question_word[m+1]]
                    event_swich = 1
                    question_event_date = datetime(1442,question_event_date[1],question_event_date[0])
                    question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                except KeyError:
                    pass
                try:
                    question_event_date = miladi_dic[question_word[m+1]]
                    event_swich = 1
                    question_event_date = datetime(2020,question_event_date[1],question_event_date[0])
                    question_monasebat.append(datetime.strftime(question_event_date, '%Y-%m-%d'))
                except KeyError :
                    pass

        calendertype = []                            

        for i in question_word :
            if i == 'شمسی' :
                event_swich =1 
                calendertype.append(i)
            if i == 'قمری ':
                event_swich =1
                calendertype.append(i)
            if i == 'میلادی' :
                event_swich =1
                calendertype.append(i)

        if len(date_list)>0:
            for i in question_date_list:
                date_3 = str(JalaliDate.to_jalali(i.year,i.month,i.day))
                final_date.append(date_3)
        if len(tarikh_shamsi(question_word,year_shamsi,year)[2])>0:
            for i in tarikh_shamsi(question_word,year_shamsi,year)[2]:
                final_date.append(str(i))
        if len(tarikh_miladi(question_word,year_miladi,year)[2])>0:
            for i in tarikh_miladi(question_word,year_miladi,year)[2]:
                final_date.append(str(i))
        if len(tarikh_ghamari(question_word,year_ghamari,year)[2])>0:
            for i in tarikh_ghamari(question_word,year_ghamari,year)[2]:
                final_date.append(str(i))


        return answer

# while True :
    # question = input("whats your question = > ")
    # bot = BOT()
    # print(bot.AIBOT(question))

