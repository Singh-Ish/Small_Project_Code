#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:37:07 2018

@author: ishdeepsingh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:23:40 2018

@author: ishdeepsingh
"""

# century website data scrapper 

import requests 
from bs4 import BeautifulSoup 
import pandas 

r=requests.get("https://www.99acres.com/search/property/buy/residential-all/delhi-dwarka?search_type=QS&search_location=NRI&lstAcn=NR_R&lstAcnId=-1&src=CLUSTER&preference=S&selected_tab=1&city=220&res_com=R&property_type=R&isvoicesearch=N&keyword_suggest=delhi%20dwarka%3B&availability=2&class=O&fullSelectedSuggestions=delhi%20dwarka&strEntityMap=W3sidHlwZSI6ImNpdHkifSx7IjEiOlsiZGVsaGkgZHdhcmthIiwiQ0lUWV8yMjAsIFBSRUZFUkVOQ0VfUywgUkVTQ09NX1IiXX1d&texttypedtillsuggestion=dwarka&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_220%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&price_min=null&price_max=null")

c=r.content
soup=BeautifulSoup(c,"html.parser") 

all=soup.find_all("div",{"class":"srpWrap"})
#print(all)
l=[]
for item in all: 
    
    #print(item.find_all("div",{"class":"wrapttl"})[0].find_all("b")[1].text)
    #print(item.find_all("div",{"class":"wrapttl"})[0].find_all("a")[0].text)
    #print(item.find_all("div",{"class":"srpDetail"})[0].find_all("div",{"class":"srpDataWrap"})[0].find_all("span")[0].find_all("b")[0].text) # super built up area 
    #a= item.find_all("div",{"class":"srpDetail"})[0].find_all("div",{"class":"srpDataWrap"})[0].find_all("span",{"class":"doElip "})
    #print(a)
    #print(item.find_all("div",{"class":"srpDetail"})[0].find_all("div",{"class":"srpDataWrap"})[0].find_all("a"))
    #.find_all("b"))
    
   # f=item.find_all("div",{"class":"srpDetail"})[0].find_all("div",{"class":"srpDataWrap"})[0].find_all("span")[1].text
    #print(f)
    
    #print(item.find_all("div",{"class":"srpDetail"})[0].find_all("div","lf f13 hm10 mb5"))
 
    

    d={}
    try:
        d["price"]=item.find_all("div",{"class":"wrapttl"})[0].find_all("b")[1].text
    except:
        d["price"]="None"
        
    d["address"]=item.find_all("div",{"class":"wrapttl"})[0].find_all("a")[0].text
    d["super-area"]=item.find_all("div",{"class":"srpDetail"})[0].find_all("div",{"class":"srpDataWrap"})[0].find_all("span")[0].find_all("b")[0].text # super built up area
 
    
    d["owner"]=item.find_all("div",{"class":"srpDetail"})[0].find_all("div","lf f13 hm10 mb5")
        
    l.append(d)

df= pandas.DataFrame(l)
#print(df)
df.to_csv("Output-result-we-scrapper.csv")

"""
all=soup.find_all("div",{"class":"propertyRow"})

#print(len(all))
l=[]
for item in all:

                
                
    d={}
    d["Price"]=(item.find_all("h4",{"class":"propPrice"})[0].text.replace("\n","").replace(" ",""))
    d["Address"]=(item.find_all("span",{"class":"propAddressCollapse"})[0].text + "," + item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    
    try:
        d["Beds"]=(item.find_all("span",{"class":"infoBed"})[0].find("b").text)
    except:
        d["Beds"]="None"
   
     
    try:
        d["Full Baths"]=(item.find_all("span",{"class":"infoValueFullBath"})[0].find("b").text)
    except:
        d["Full Baths"]="None"
     
        
    try:
        d["Area"]=(item.find_all("span",{"class":"infoSqFt"})[0].find("b").text)
    except:
        d["Area"]="None"
        
    try:
        d["Half Bath"]=(item.find_all("span",{"class":"infoValueHalfBath"})[0].find("b").text)
    except:
        d["Half Bath"]="None"
      
       
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        #print(column_group)
        for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})): 
           # print(feature_group.text , feature_name.text)
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=feature_name.text
    
    l.append(d)
    
#print(l)

df= pandas.DataFrame(l)

print(df)
df.to_csv("Output-result-we-scrapper.csv")

"""