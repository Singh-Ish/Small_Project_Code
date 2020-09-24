from lapp import app
'''


import requests



url = "http://saportal.sce.carleton.ca/"
page = requests.get(url)
#print(page.status_code)

if page.status_code==200 :
    print("accessessible")
else:
    print("not accessissible")

'''