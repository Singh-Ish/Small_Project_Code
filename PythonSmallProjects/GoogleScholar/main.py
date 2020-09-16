import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_auth

from scholarly import scholarly
import pandas as pd
from scholarly import ProxyGenerator
import json

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

##### dataframe from google scholar #####

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

df.to_excel("author.xlsx")






##### datframe end ######



'''
##### html rendering
VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]

app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)



app.layout = html.Div([


    html.H3(
        children='Publications/Patents Having 100 or More Citations on Google Scholar',
        style={
            'textAlign': 'left',
            'textSize': '12px',
            'textColor':'red'
                  }
        ),

    dcc.Input(id='my-id', value='Dash App', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)



if __name__ == '__main__':
    app.run_server()
'''
