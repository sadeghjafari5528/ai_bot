from utils import Parser , Util
import json
from hazm import *
import numberize
from api_handler import religios

def decodeIntent(intent):
    result = []
    n = intent
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    if len(k) > 4:
        k = k[::4]
    elif len(k) == 3:
        k.append(0)
    elif len(k) == 2:
        k += [0,0]
    elif len(k) == 1:
        k += [0,0,0]
    elif len(k) == 0:
        k = [0,0,0,0]
    
    if k[0] == 1:
        result.append('2')
    if k[1] == 1:
        result.append('4')
    if k[2] == 1:
        result.append('1')
    if k[3] == 1:
        result.append('3')
    return result

def getResult(weights , s , numberOfClass):
    u = Util()
    #s = u.text_proccessor(text)
    #s = l.deleteStopWords(s , stopwords)
    activation_list = u.makeZeroList(numberOfClass)
    for i in s:
        if not i in weights.keys():
            weights[i] = u.makeZeroList(numberOfClass)

        for a in range(numberOfClass):
            activation_list[a] += weights[i][a]

    # calculate result
    estimate_label = u.argMax(activation_list)
    return estimate_label

def getIntent(text):
    u = Util()
    j = open('weights.json' , 'r')
    weights = json.load(j)
    j.close()

    return getResult(weights , text , 16)

def getArgument(s):
    u = Util()
    j = open('argWeights.json' , 'r')
    weights = json.load(j)
    j.close()

    u = Util()
    result = []
    #s = u.text_proccessor(text)
    w_i = -1
    len_s = len(s)
    for word in s:
        w_i += 1
        try:
            word = int(word)
            word = str(type(int))
        except:
            pass
        if not word in weights.keys():
            #try:

            result.append(1)
        else:
            x = []
            for tag in range(7):
                current = weights[word][tag] / weights[word][-1]
                if word == "و":
                    print(current)
                try:
                    hasPrevious = (s[w_i - 1] in weights.keys())
                except:
                    hasPrevious = False

                try:
                    hasNext = (s[w_i + 1] in weights.keys())
                except:
                    hasNext = False

                if (not hasNext) and (not hasPrevious):
                    current_factor = 1
                    next_factor = 0
                    previous_factor = 0
                    _next = 0
                    previous = 0

                elif not hasNext:
                    current_factor = 0.75
                    next_factor = 0
                    previous_factor = 0.25
                    _next = 0
                    previous = weights[s[w_i - 1]][tag] / weights[s[w_i - 1]][-1]

                elif not hasPrevious:
                    current_factor = 0.75
                    next_factor = 0.25
                    previous_factor = 0
                    _next = weights[s[w_i + 1]][tag] / weights[s[w_i + 1]][-1]
                    previous = 0

                else:
                    current_factor = 0.5
                    next_factor = 0.25
                    previous_factor = 0.25
                    _next = weights[s[w_i + 1]][tag] / weights[s[w_i + 1]][-1]
                    previous = weights[s[w_i - 1]][tag] / weights[s[w_i - 1]][-1]                    

                x.append(current * current_factor + _next * next_factor + previous * previous_factor)
            result.append(u.argMax(x))

    return result


def getJsonResult(text):
    answer = {'type': [], 'city': [], 'date': [],'time': [], 'religious_time': [],'calendar_type': [], 'event': [], 'api_url': [], 'result': []} 
    u = Util()
    p = Parser()
    s = numberize.numberize(text)
    #s = u.text_proccessor(text)
    answer['type'] = decodeIntent(getIntent(s))
    arguments = getArgument(s)
    print(arguments , answer['type'])
    pre_tag = None
    phrase = ""
    for w_i in range(len(s)):
        if pre_tag != None and pre_tag != arguments[w_i]:

            #phrase = phrase[:-1]
            print(phrase , pre_tag)
            phrase = phrase[:-1]
            if pre_tag == 1:
                answer['city'].append(p.cityParser(phrase))
            elif pre_tag == 2:
                answer['date'].append(p.dateParser(phrase))
            elif pre_tag == 3:
                answer['time'].append(p.timeParser(phrase))
            elif pre_tag == 4:
                answer['religious_time'].append(p.religiousTimeParser(phrase))
            elif pre_tag == 5:
                answer['calendar_type'].append(p.calendarTypeParser(phrase))
            elif pre_tag == 6:
                answer['event'].append(p.eventParser(phrase))
            
            phrase = str(s[w_i]) + ' '
        else:
            phrase += str(s[w_i]) + ' '
        pre_tag = arguments[w_i]
    
    for i in range(len(answer['type'])):
        if answer["type"][i] == '2':
            print('tuple' , answer['date'])
            answer['date'] = [answer['date'][0][0][-1][0]]
            
            if len(answer["date"]) == 1:
                date = answer["date"][0]
            else:
                date = answer["date"][i]
            req,date,URL = religios.aladhan(answer['city'][i] , date)
            answer["result"].append(religios.azan(req , text , date))
            answer["api_url"].append(URL)
            answer['date'] = [answer['date'][0].strftime("%Y-%m-%d")]

    with open("result.txt" , 'w') as f:
        f.writelines(str(answer) + "\n")
        f.writelines(str(s) + "\n")

    '''chunker = Chunker(model='resources/chunker.model')
    tagger = POSTagger(model='resources/postagger.model')

    normalizer = Normalizer()

    tagged = tagger.tag(word_tokenize(normalizer.normalize(text)))
    t2 = tree2brackets(chunker.parse(tagged))
    x = chunker.parse(tagged)
    p = Parser()
    for j in range(len(x)):
        if type(x[j]).__name__ == 'tuple':
            continue
        rList = []
        for k in x[j]:
            rList.append(k[0])
        phrase = " ".join(rList)
        result = getArgument(phrase)

        if result == 1:
            answer['city'].append(p.cityParser(phrase))
        elif result == 2:
            answer['date'].append(p.dateParser(phrase))
        elif result == 3:
            answer['time'].append(p.timeParser(phrase))
        elif result == 4:
            answer['religious_time'].append(p.religiousTimeParser(phrase))
        elif result == 5:
            answer['calendar_type'].append(p.calendarTypeParser(phrase))
        elif result == 6:
            answer['event'].append(p.eventParser(phrase))'''

    return answer



def getSentence(json):
    return ["",""]

def getFinalOutPut(text):
    jsonFile = getJsonResult(text)
    answer = ""
    return ""

if __name__ == "__main__":
    #print(getIntent("امروز اذان ظهر چه زمانی است؟"))
    #print(decodeIntent(5))
    text = 'اذان ظهر  ۴ روز پیش قم چه ساعتی بود؟ '
    #print(text)
    getJsonResult(text)
    #print(getArgument(text , getIntent(text)))
    