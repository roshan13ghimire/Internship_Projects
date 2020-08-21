import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


df = pd.read_excel("C:/Users/rosha/Desktop/demoo.xlsx")     
df = df.set_index("Date")

def prepare_data(df, steps=5):
    df = df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['Date'] = df_expanded['Date'].fillna(method='ffill')
    df_expanded = df_expanded.set_index('Date')
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_rank_expanded.interpolate()
    return df_expanded, df_rank_expanded

df_expanded, df_rank_expanded = prepare_data(df)

def init():
    ax.clear()
    [spine.set_visible(False) for spine in ax.spines.values()]
    ax.set_ylim(.2, 6.8)

def update(i):
    for bar in ax.containers:
        bar.remove()
    y = df_rank_expanded.iloc[i]
    width = df_expanded.iloc[i]
    ax.barh(y=y, width=width, color=plt.cm.Dark2(range(5)), tick_label=df_expanded.columns)
    date_str = df_expanded.index[i].strftime('%B %d, %Y')
    ax.set_title(f'Small Demo - {date_str}', fontsize='larger')
    
    

    
fig = plt.Figure(figsize=(7, 3), dpi=144)
ax = fig.add_subplot()
anim = FuncAnimation(fig=fig, func=update, init_func=init, frames=len(df_expanded), 
                     interval=100, repeat=False)

html = anim.to_html5_video()
HTML(html)

anim.save('C:/Users/rosha/Desktop/demoo.mp4')
