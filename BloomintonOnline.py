import urllib2
from bs4 import BeautifulSoup
url_page = "http://www.bloomingtononline.net/calendar/dcalendar.php"
page = urllib2.urlopen(url_page)
soup = BeautifulSoup(page,"html.parser")
#print soup.prettify()
#tag = soup.a
#for i in tag:
 #   print(i)
#g_data = soup.find_all("div")
g_data = soup.find_all("td",{"class":"today"})
#print g_data # contains one td(corresponding to today's date
#for item in g_data:
for g_dataItem in g_data:
   #Produces the unstructured text for each day
   #print g_dataItem.text
   #5 has the text
   # Needed :
    print g_dataItem.contents[5].find_all(onmouseover=True)
    for tag in g_dataItem.contents[5].findAll(onmouseover=True):
       print  tag['onmouseover']
    #tags = g_dataItem.contents[5].find('a',{"onmouseover"})
    #print tags



       #for value in tag['onmouseover'].findAll('b'):
        #   print value



        #print tag.find(attrs={"Time:"})
    #for data in tag['onmouseover']:
        #print data['Time:']
""" print tag['Time:']
      print tag['Title:']
      print tag['Description:']
"""