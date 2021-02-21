#in the name of Allah
from hazm import *
from config import *
import functions


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
        for i in question_word :
            if i == 'فردا' :
                question_date_list.append(date.today()+ timedelta(1))
                date_list.append(date.today()+ timedelta(1))
        for i in tempreture:
            if question.count(i) > 0 :
            
                weather_data,api_url = get_weather_data()
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

        return question_word

bot = BOT() 

while True:
    try:    
        question = input("whats your question = > ")
        with open("test.txt" , 'w') as f:
            #f.writelines(str(bot.AIBOT(question)))
            f.writelines(str(functions.tarikh_miladi(question)))
        print(bot.AIBOT(question))
    except KeyboardInterrupt:
        break

