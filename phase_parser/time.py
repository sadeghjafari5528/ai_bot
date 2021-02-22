#in the name of Allah

from numberize import *

def Clock(text):
    hour,minute = 0,0
    try:
        if text.count(":")>0:
            time_list = text.split(':')
            time_list = adad_farsi(time_list)
            hour = int(time_list[0])
            minute = int(time_list[1])
    except AttributeError:
        pass
    return hour,minute

def ghabl_bad_time(question_word,word):

    after = ['آینده','بعد','اینده''بعدی','دیگر','دیگه']
    befor = ['گذشته', 'قبل','پیش']
    #question_word = word_tokenize(text)
    hour,minute = datetime.now().hour,datetime.now().minute
    m = question_word.index(word)
    number = question_word[m-1]
    if m != 0:
        if type(question_word[m-1]) == int :
            if word == "ساعت":
                for i in befor:
                    if question_word[m+1] == i :
                        dtHour = datetime.now() + timedelta(hours = (-1)*number)
                        hour = dtHour.hour

                for i in after:
                    if question_word[m+1] == i :
                        dtHour = datetime.now() + timedelta(hours = number)
                        hour = dtHour.hour
            
                return hour,minute


            elif word == "دقیقه":
                print('11111111111111111111')
                for i in befor:
                    if len(question_word) >= m+2:
                        print(i)
                        if question_word[m+1] == i :
                            dtMinute = datetime.now() + timedelta(minutes = (-1)*number)
                            minute = dtMinute.minute
                            return hour,minute
                for i in after:
                    if len(question_word) >= m+2:
                        if question_word[m+1] == i :
                            dtMinute = datetime.now() + timedelta(minutes = number)
                            minute = dtMinute.minute
                            return hour,minute
                return hour,minute        
    else:
        return hour,minute

def timeParser(question):
    swich = 0
    minute = 0
    question_word = numberize(question)
    print(question_word)
    hour_list = ['بعد از ظهر','بعدازظهر','عصر','ظهر','شب','غروب']

    for i in question_word :
        if i == "ساعت" :
            m = question_word.index(i)
            if type(question_word[m+1]) == int :
                hour = question_word[m+1]
                if question_word[m+2] == 'و' and type(question_word[m+3]) == int and question_word[m+4] == 'دقیقه' :
                    minute = question_word[m+3]
                for i in hour_list:
                    if question.count(i)>0:
                        swich = 1
                        if question_word[m+1] <= 12:
                            hour = question_word[m+1] + 12
                            if hour == 24 :
                                return 0,minute
                            else:
                                hour = question_word[m+1] + 12
                                return hour,minute
                        else:
                            return hour,minute
                if swich == 0 :
                    return hour,minute

        elif type(i) == str and i.count(":") > 0:
            hour,minute = Clock(i)
            return hour,minute

    for i in question_word:
        if i == "ساعت" :
            hour ,minute = ghabl_bad_time(question_word,i)
            return hour,minute

        elif i == "دقیقه":
            hour ,minute = ghabl_bad_time(question_word,i)
            return hour,minute

        elif i == "الان" or i == "الآن" or i == "هماکنون":
            hour , minute = datetime.now().hour,datetime.now().minute
            return hour,minute

        elif question_word.count("هم") > 0 and question_word.count("اکنون")> 0:
            hour , minute = datetime.now().hour,datetime.now().minute
            return hour,minute

question = "دو ساعت الان"
# normalizer = Normalizer()
timeP = timeParser(question)
# timeP = datetime(2021,1,4,hour = timeP[0], minute = timeP[1], second = 0)
# timeP = datetime.strftime(timeP, '%H:%M')
print(timeP)