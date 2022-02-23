import requests
import mysql.connector
from bs4 import BeautifulSoup
con = mysql.connector.connect(user='root', port = '3306',password = 'aritri' , database ='webscraping')
cur = con.cursor()




ask = 'yes'
while ask !='no':
    cur.execute("SELECT * FROM history")
    data = cur.fetchall()
    for i in data:
        print(i[0])
        
    print("~"*50)
    name = input("Search: ")
    
    cur.execute("SELECT * FROM history where title like '{}'".format("%"+name+"%"))
    data = cur.fetchall()
    for i in data:
        print(i[0])
        


    cur.execute("INSERT INTO history VALUES('{}')".format(name))    
    
    
    con.commit()

    
    
    
    url = "https://www.google.com/search?q="+name



    


# inserting the searched item into database
# while True:
    


# 2. Get the html
    r = requests.get(url)
    html = r.content



# 3. Parse the html.
    soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify)

# 4. HTML tree traversal.

#print(soup.find("p"))

    ctr = 0
    anchors = soup.find_all("a")
#alllinks = set()
    for link in anchors:
            ctr += 1
            if (link.get('href') != '#'):
                linktext = "https://www.google.com"+link.get('href')
        #alllinks.add(link)
                print("~"*50)
                print()
                print(ctr,") ")
                print(linktext)
                print()

    ask = input("continue?(yes/no): ")
    #print(link.get('href'))
