from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import chart_studio.plotly as py
import plotly.graph_objects as go
import pandas as pd

# DATA
df = pd.read_csv('2014_World_GDP')

data = dict(type='choropleth',
            locations=df['CODE'],
            text=df['COUNTRY'],
            z=df['GDP (BILLIONS)'],
            colorbar={'title': 'GDP in  Billions USD'})

layout = dict(title='2014 Global GDP',
              geo=dict(showframe=False, projection={'type': 'mercator'}))

choromap_3 = go.Figure(data=[data], layout=layout)

iplot(choromap_3)

