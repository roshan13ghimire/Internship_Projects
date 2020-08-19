import numpy as np
import pandas as pd
import plotly.graph_objects as go  


df = pd.read_excel('C:/Users/rosha/Desktop/demoo.xlsx')
High = df['High'].tolist()
Low = df['Low'].tolist()
Open = df['Open'].tolist()
Close = df['Close'].tolist()
Adj_Close = df['Adj Close'].tolist()

trace1 = go.Scatter(x=df.Date[:2],
                    y=High[:2],
                    mode='lines',
                    line=dict(width=1.5))

trace2 = go.Scatter(x = df.Date[:2],
                    y = Low[:2],
                    mode='lines',
                    line=dict(width=1.5))

trace3 = go.Scatter(x = df.Date[:2],
                    y = Open[:2],
                    mode='lines',
                    line=dict(width=1.5))

trace4 = go.Scatter(x = df.Date[:2],
                    y = Close[:2],
                    mode='lines',
                    line=dict(width=1.5))

trace5 = go.Scatter(x = df.Date[:2],
                    y = Adj_Close[:2],
                    mode='lines',
                    line=dict(width=1.5))

frames = [dict(data= [dict(type='scatter',
                           x=df.Date[:k+1],
                           y=High[:k+1]),
                      dict(type='scatter',
                           x=df.Date[:k+1],
                           y=Low[:k+1]),
                      dict(type='scatter',
                           x=df.Date[:k+1],
                           y=Open[:k+1]),
                      dict(type='scatter',
                           x=df.Date[:k+1],
                           y=Close[:k+1]),
                      dict(type='scatter',
                           x=df.Date[:k+1],
                           y=Adj_Close[:k+1])],
               traces= [0, 1 ,2 ,3 , 4],  #this means that  frames[k]['data'][0]  updates trace1, and   frames[k]['data'][1], trace2 
              )for k  in  range(1, len(High)-1)] 

layout = go.Layout(width=650,
                   height=400,
                   showlegend=False,
                   hovermode='closest',
                   updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=3, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])])


layout.update(xaxis =dict(range=(df.Date[0], df.Date[len(df)-1]), autorange=False),
              yaxis =dict(range=[0, 60], autorange=False));
fig = go.Figure(data=[trace1, trace2 ,trace3 ,trace4 ,trace5], frames=frames, layout=layout)
fig.show()
