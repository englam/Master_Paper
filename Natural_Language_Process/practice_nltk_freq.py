
from nltk import FreqDist
import re,string
from nltk.corpus import stopwords
from nltk.corpus import swadesh


text_a = []

text_e = 'The distance is outstanding ISSUE ISSUE ISSUE when it stays connected. Super fast. However i believe there is a firmware issue that causes you to get disconnected at random times. Netgear support community has over 6 pages as of this issue as of this review. Do your homework first:search google "orbi keeps losing internet connection" sadly this one is going back.'


text_a.append(text_e)
text_a = tuple(text_a)

#print (text_a)




#fdist3 = FreqDist(text_a)

#print (fdist3.keys())


def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    input = input.upper()
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput



#利用nltk的stopwords,把this, a, the ...etc給刪除掉
def content_fraction(text):
    stop_words = stopwords.words('english')
    content = [w for w in text if w.lower() not in stop_words]
    return content


#利用nltk的swadesh,把small,new,because ...etc給刪除掉
def content_fraction2(text):
    compared_words = swadesh.words('en')
    content2 = [w for w in text if w.lower() not in compared_words]
    return content2

aa = cleanInput(text_e)
print (aa)

aa = content_fraction(aa)

print (aa)

aa = content_fraction2(aa)

print (aa)

fdist3 = FreqDist(aa)

for i in fdist3:
    print (i)