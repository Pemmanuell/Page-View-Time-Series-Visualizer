import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)

# Clean data
p25 = np.percentile(df['value'], 2.5)
p975 = np.percentile(df['value'], 97.5)
df_clean = df[(df['value']>= p25) & (df['value']<= p975)]


def draw_line_plot():
    # Draw line plot
    def draw_line_plot(df_clean):
        plt.figure(figsize=(16, 5))
        plt.plot(df_clean , color ='red')
        plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        plt.xlabel('Date')
        plt.ylabel('Page Views')
        plt.show()
draw_line_plot(df_clean) 






    # Save image and return fig (don't change this part)
fig.savefig('line_plot.png')
return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_clean.groupby(['Year', 'Month']).mean().unstack()

    # Draw bar plot
    def draw_bar_plot(df_clean):
        df_clean['Year'] = df_clean.index.year
        df_clean['Month'] = df_clean.index.month
        df_clean_grouped = df_bar
        df_clean_grouped.plot(kind='bar', figsize=(12, 6))
        plt.xlabel('Years')
        plt.ylabel('Average Page Views')
        plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December']).set_title('Month')
    
    plt.show()
draw_bar_plot(df_clean)






    # Save image and return fig (don't change this part)
fig.savefig('bar_plot.png')
return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    def draw_box_plot(df_clean):
        plt.figure(figsize=(20, 5))
        plt.subplot(1, 2, 1)
        sns.boxplot(x='Year', y='value', data=df_clean, palette='rainbow')
        plt.title('Year-wise Box Plot (Trend)')
        plt.xlabel('')
        plt.ylabel('Page Views')
        plt.xticks(ticks=np.arange(4), labels=['2016', '2017', '2018', '2019'])
        plt.subplot(1, 2, 2)
        sns.boxplot(x='Month', y='value', data=df_clean, palette='rainbow')
        plt.title('Month-wise Box Plot (Seasonality)')
        plt.xlabel('Month')
        plt.ylabel('Page Views')
        plt.xticks(ticks=np.arange(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()
draw_box_plot(df_clean)    






    # Save image and return fig (don't change this part)
fig.savefig('box_plot.png')
return fig
