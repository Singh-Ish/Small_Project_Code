from scholarly import scholarly
import pandas as pd
import json



''''
#### publication details for multiple professors ######

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
