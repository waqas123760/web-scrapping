import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3

theverge_r1 = requests.get("https://www.theverge.com/")
cover_theverge= theverge_r1.content
soap_theverge= BeautifulSoup(cover_theverge,'html5lib')
all_cover_articles=soap_theverge.find_all('li',{'class':'duet--content-cards--content-card'})

number_of_artcles= 5

id_theverge=[]
url_theverge=[]
headline_theverge=[]
author_theverge=[]
date_theverge=[]

for n in np.arange(0,number_of_artcles):
    id= n+1
    #print(id)
    id_theverge.append(id)

    #getting urls
    url=all_cover_articles[n].find("a")['href']
    #print(url)
    url_theverge.append(url)

    #getting headline
    headline=all_cover_articles[n].find("a",{"class":'group-hover:shadow-underline-franklin'}).get_text()
    #print(headline)
    headline_theverge.append(headline)

    #getting author name
    author=all_cover_articles[n].find("a",{'class':"text-gray-31"}).get_text()
    #print(author)
    author_theverge.append(author)

    #getting time-date
    date=all_cover_articles[n].find("span",{'class':"text-gray-63"}).get_text()
    #print(date)
    date_theverge.append(date)

dictionary={'Id':id_theverge,"Url":url_theverge,"Headline":headline_theverge,"Author":author_theverge,"Date":date_theverge}
df=pd.DataFrame(dictionary,columns=['Id',"Url", "Headline", "Author", "Date"])
df.to_csv("C:\\Users\\MOHD ZAID\\Desktop\\ws\\data.csv")
df=pd.read_csv("C:\\Users\\MOHD ZAID\\Desktop\\ws\\data.csv")
print(df)
          
conn= sqlite3.connect('data.db')
c=conn.cursor()
#c.execute('''CREATE TABLE AWS(Id INTEGR PRIMARY KEY  ,Url TEXT , Headline TEXT, Author TEXT, Date TEXT)''')
ap='INSERT INTO AWS(Id,Url,Headline,Author,Date) VALUES (?,?,?,?,?)'
sql=[id_theverge , url_theverge , headline_theverge , author_theverge , date_theverge]
c.executemany(ap,sql)
conn.commit()
print('Sucessfully completed!!!')
c.execute('''SELECT * FROM AWS''')
results=c.fetchall()
print(results)
conn.close()