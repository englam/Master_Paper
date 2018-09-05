from nltk.corpus import stopwords
from nltk.corpus import swadesh

#print (stopwords.words('english'))


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



a = ['GREAT', 'WHEN', 'IT', 'DOES', 'NOT', 'DISCONNECT','ITSESDD']


a1 = content_fraction(a)
a2 = content_fraction2(a1)
print (a2)


b = ['one','someone']


for i in b:
    if 'one' in i:
        print (i)
