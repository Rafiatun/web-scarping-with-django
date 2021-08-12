from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import html5lib
# Create your views here.

#express
express=requests.get("https://www.express.co.uk/news/world")
soup=BeautifulSoup(express.content , 'html5lib')
heading=soup.find_all('h4')
heading=heading[0:-16]

expres_news=[]
for i in heading:
    expres_news.append(i.text)

#cnet

cnet=requests.get("https://www.cnet.com/news/")
soup_cnet=BeautifulSoup(cnet.content , 'html5lib')

heading_cnet=soup_cnet.findAll("a" , {"class":"assetHed"})
cnet_news=[]
for j in heading_cnet:
    cnet_news.append(j.text)

def index(request):
    context={
        'expres_news': expres_news,
        'cnet_news':cnet_news
    }
    return render(request,'index.html',context)