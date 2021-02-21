import functions
from utils import Parser , Util
from hazm import *


p = Parser()

#p.dateParser("بیست جمادی الثانی")

normalizer = Normalizer()
u = Util()

print(u.numberize(word_tokenize(normalizer.normalize('اول رجب در سال 1400 چه روزیه؟'))))