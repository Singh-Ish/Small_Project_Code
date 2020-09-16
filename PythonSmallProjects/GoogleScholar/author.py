from scholarly import scholarly
from fp.fp import FreeProxy
import pandas as pd
import json



# for single author

#search_query = scholarly.search_author('Andy Adler')
#author = next(search_query).fill()

#print(author)



'''
# multiple professors publication


authors= ['Halim Yanikomeroglu','Andy Adler'] # name of professors to consider


publication = pd.DataFrame(columns=['id','name', 'title','cites','year'])

for a in authors:
    search_query = scholarly.search_author(a)
    author = next(search_query).fill()
    # assigning id and name
    id = author.id
    name = author.name

    # iterating all publications
    for z in author.publications:

        data = z.bib
        #print(data)
        pub_json = json.dumps(data)
        pj = json.loads(pub_json)
        if("year" in pj):
            year= pj['year']
        else:
            year=0

        title = pj['title']
        cites = pj['cites']

        publication = publication.append({'id':id, 'name':name,'title':title , 'cites':cites, 'year':year }, ignore_index=True)




cdict = {'cites':int, 'year':int}

#print(publication)
#publication.astype({'cites':int,'year':int}).dtypes

publication=publication.astype(cdict)

publication.sort_values(by=['cites'],ascending=False,inplace=False)



# export the dataframe to excel

#publication.to_excel("publications.xlsx",engine='xlsxwriter')
#print( "exporting the publications to excel ")


print(publication.head(5))
'''



'''

# multiple authors and their data

# Retrieve the author's data, fill-in, and print
authors= ['Halim Yanikomeroglu','Andy Adler'] # name of professors to consider 


df = pd.DataFrame(columns=['id','name','affiliation','interest','citedby','citedbyyear','hindex','hindex5y','i10index','i10index5y'])
for z in authors:
    search_query = scholarly.search_author(z)
    author = next(search_query).fill()
    #print(author.name)

    a = author.affiliation
    b = author.citedby
    c= author.cites_per_year
    h = author.hindex
    h5 = author.hindex5y
    i = author.i10index
    i10 = author.i10index5y
    id = author.id
    interest = author.interests
    name = author.name

    df =df.append({'id': id ,'name':name , 'affiliation':a, 'interest':interest ,'citedby':b ,'citedbyyear':c, 'hindex':h ,'hindex5y':h5, 'i10index':i, 'i10index5y':i10}, ignore_index=True)

df.sort_values(by=['citedby'])
'''


'''
#render dataframe as html
html = df.to_html()

#write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
'''
#print(df)

#df = df.to_excel('author.xlsx')
#pub = pd.DataFrame()



###### getting publications details
'''
def publicationDetails( p ):
    # p is the passed publication name
    search_query = scholarly.search_pubs(p)
    pd = next(search_query)

    print(pd.bibtex)
    #dic.bib
    #print(pd.bib.abstract)
    #print(pd)



pub='Uses and abuses of EIDORS: an extensible software base for EIT'
publicationDetails(pub)

'''