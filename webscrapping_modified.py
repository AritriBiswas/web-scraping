from ctypes.wintypes import tagMSG
import requests

import csv

from bs4 import BeautifulSoup


name = input("Search: ")



f = open("database.csv","r")
reading = csv.reader(f)
count = 0

done = ""
for i in reading:
    
    
    #print(i)
    try:
        if i[0] == name:
            print("From my database")
            for k in i:
                print(k)
                done = name
            
            break   
    except:
        EOFError
    
            
f.close()       

    
    


if (done != name):

    url = "https://en.wikipedia.org/wiki/"+name
        #Get the html
    r = requests.get(url)
    html = r.content



            # 3. Parse the html.
    soup = BeautifulSoup(html, 'html.parser')
            #print(soup.prettify)

            # 4. HTML tree traversal.

            #print(soup.find("p"))
    ctr = 0
    finding = soup.find_all("p")
    info = [name]

    for cont in finding:
        if(ctr<5):
            print(cont.text)
            info.append(cont.text)
            print()
            ctr+=1
        else:
            break


    f = open("database.csv","a")
    write = csv.writer(f)
    write.writerow(info)
    f.close()

            
            #anchors = soup.find_all("a")
            #alllinks = set()
            #for link in anchors:
                        
                #print(link)
                #print()


                #print(link.get('href'))
