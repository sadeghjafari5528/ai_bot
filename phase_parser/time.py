#in the name of Allah

from numberize import *

def Clock(text):
    hour,minute = 0,0
    try:
        if text.count(":")>0:
            time_list = text.split(':')
            time_list = adad_farsi(time_list)
            hour = time_list[0]
            minute = time_list[1]
    except AttributeError:
        pass
    return hour,minute

def ghabl_bad_time(question_word,word):

    after = ['آینده','بعد','اینده''بعدی','دیگر','دیگه']
    befor = ['گذشته', 'قبل','پیش']
    #question_word = word_tokenize(text)
    houre,minute = datetime.now().hour,datetime.now().minute
    m = question_word.index(word)
    number = question_word[m-1]
    if m != 0:
        if type(question_word[m-1]) == int :
            if word == "ساعت":
                for i in befor:
                    if question_word[m+1] == i :
                        time = datetime.now() + timedelta(hour = (-1)*number)
                        return houre,minute
                for i in after:
                    if question_word[m+1] == i :
                        hour= datetime.now() + timedelta(hour = number)
                        return hour,minute
                    else:
                        return houre,minute

            elif word == "دقیقه":
                for i in befor:
                    if question_word[m+1] == i :
                        time = datetime.now() + timedelta(minute = (-1)*number)
                        return houre,minute
                for i in after:
                    if question_word[m+1] == i :
                        hour= datetime.now() + timedelta(minute = i)
                        return hour,minute
                    else:
                        return houre,minute        
    else:
        return houre,minute

def timeParser(question):
    swich = 0
    minute = 0
    question_word = numberize(question)
    hour_list = ['بعد از ظهر','بعدازظهر','عصر','ظهر','شب','غروب']

    for i in question_word:
        if i == "ساعت" :
            hour ,minute = ghabl_bad_time(question_word,i)
        elif i == "دقیقه":
            hour ,minute = ghabl_bad_time(question_word,i)
        elif i == "الان" or i == "الآن" or i == "هماکنون":
            hour , minute =  ghabl_bad_time(question_word,i)
        elif question_word.count("هم") > 0 and question_word.count("اکنون")> 0:
            hour , minute =  ghabl_bad_time(question_word,i)

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


question = "دو ساعت بعد"
normalizer = Normalizer()
timeP = timeParser(normalizer.normalize(question))
# timeP = datetime(2021,1,4,hour = timeP[0], minute = timeP[1], second = 0)
# timeP = datetime.strftime(timeP, '%H:%M')
print(timeP)