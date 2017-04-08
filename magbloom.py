import datetime
import urllib2
from bs4 import BeautifulSoup,NavigableString, Tag
now = datetime.datetime.now()
#print "Current date and time using strftime:"
now_mod = now.strftime("%b-%d-%Y")
#Jun-25-2016

url_page = "http://www.magbloom.com/events/?event-date=" + now_mod
page = urllib2.urlopen(url_page)
soup = BeautifulSoup(page,"html.parser")
#print soup.prettify()
g_data=soup.find_all("div",{"class":"type-event"})
for item in g_data:
    #print item.contents[0].find_all("span")[0].text
    #print item.contents[0].find_all("strong")[0].tex
    print ("Date : %s" %(item.contents[0].text))
    #print item.contents[0].find_all("p",{"class":"date"}).text
    print ("Title : %s" %(item.contents[1].text))
    print ("Time %s" %(item.contents[2].find(text=True, recursive=False)))
    for br in item.contents[2].findAll('br'):
        next = br.nextSibling
        if not (next and isinstance(next,NavigableString)):
            continue
        next2 = next.nextSibling
        if next2 and isinstance(next2,Tag) and next2.name == 'br':
            text = str(next).strip()
            if text:
                print("Location:", next)
    #print "Time %s" %(item.contents[2].find_all("br")[].text)
    ############print "Time :%s" %(item.contents[2].find('p').getText())

    #print "Description : %s"
    print ("Categories : %s" %(item.contents[4].text))
    print ("Description : %s" %(item.contents[3].text))

    #print soup.find('li').find(text=True, recursive=False)
