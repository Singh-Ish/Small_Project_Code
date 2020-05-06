import html2text
import bs4
import requests

#res = requests.get("https://academicintegrity.org")


#soup = bs4.BeautifulSoup(res.text, 'lxml')



print(html2text.html2text("<a> text is here </a>")
