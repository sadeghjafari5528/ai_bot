
import main
import functions


class BOT:
    def __init__(self):
        self.modified = False

    def is_modified(self):
        return self.modified

    def AIBOT(self, question):
        answer = main.getJsonResult(question)
        result = []
        for i in answer['type']:
            if int(i) == 1:
                #weather
                for city in answer['city']:
                    result.append(functions.get_weather_data(city))
            elif int(i) == 2:
                #rt
                pass
            elif int(i) == 3:
                #time
                pass
            elif int(i) == 4:
                #occasion
                pass

        