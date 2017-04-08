import urllib2
from bs4 import BeautifulSoup
url_page = "https://visitbead.com/events/"##.WIO_zPkrJEY"
page = urllib2.urlopen(url_page)
soup = BeautifulSoup(page,"html.parser")
#print soup.prettify()
#date_range=soup.find_all("input",{"value":{"2016-06-01","2016-06-30"}})
#print date_range #print the range of date
g_data=soup.find_all("td")
for item in g_data:
    try:
        print "Title : %s"%(item.contents[1].find_all("a")[0].text)
        print "Date : %s"%(item.contents[4])
        print "Time : %s"%(item.contents[8])
        print "Location : %s"%(item.contents[12].text)#.find_all("a")[0].text)
        print "\n"
    except:
        pass

    #.get_text()
    """try:
        print "Title : %s"%(item.contents[1].find_all("a")[0].text)
        print "Date : %s"%(item.contents[4])
        print "Time : %s"%(item.contents[8])
        print "Location : %s"%(item.contents[12].text)#.find_all("a")[0].text)
        #try:

        print "Description : %s"%(item.contents[16].get_text())
        #except:
        #pass
    except:
        pass
    """