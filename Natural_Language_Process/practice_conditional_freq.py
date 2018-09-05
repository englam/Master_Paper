from nltk import FreqDist
from nltk import ConditionalFreqDist

a = [('ee', 'get'), ('aa', 'out'), ('science_fiction', 'of'), ('science_fiction', 'pain')]

a1 = [('englam')]

b = ConditionalFreqDist(a1)


for i in b:
    print (i)