#!/usr/bin/env python
# coding: utf-8

# # Final Project

# ### MK Visualisasi Data Semester Ganjil 2021/2022

# #### Instruksi
# Buatlah aplikasi berbasis web yang menampilkan visualisasi interaktif terkait topik tertentu.
# Visualisasi yang ditampilkan harus memiliki sedikitnya 2 fitur interaktif, seperti sidebar,
# dropdown, dll. Visualisasi interaktif dibuat dengan menggunakan module bokeh dan dideploy pada platform Heroku. Pada dasarnya tidak ada batasan terkait topik yang bisa dipilih
# untuk tugas final project ini.

# In[1]:


# Import library
# Data handling
import pandas as pd
import seaborn as sns

# Bokeh libraries
from bokeh.io import curdoc, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource, Slider, Select
from bokeh.palettes import Greys256, Inferno256, Magma256, Plasma256, Viridis256, Cividis256, Turbo256
from bokeh.layouts import widgetbox, row, gridplot
from bokeh.models.widgets import Tabs, Panel


# In[2]:


# Fetching url
url_1='https://genshin-impact.fandom.com/wiki/Characters/Comparison#Base_Stats'
url_2='https://genshin-impact.fandom.com/wiki/Characters/List#Playable_Characters'


# In[3]:


# Parsing table from url1 & url2 to dataframe
tables_1 = pd.read_html(url_1)
tables_2 = pd.read_html(url_2)
df1 = tables_1[1]
df2 = tables_2[1]


# In[4]:


df1


# In[5]:


df2


# In[6]:


# Removing NaN columns & merge 2 datasets into 1
df1 = df1.drop(['Icon'], axis = 1)
df2 = df2.drop(['Icon','Rarity'], axis = 1)
df3 = df1.merge(df2)

df3


# In[7]:


df3.info()


# In[8]:


df3.isnull().sum()


# In[9]:


df = df3.dropna()
df.rename(columns={'Ascension Stat': 'AscensionStat', 'Ascension Stat Value': 'ASV'}, inplace=True)
df.head()


# In[10]:


duplicateRow = df[df.duplicated()]
duplicateRow


# In[11]:


# The figure will be right in my Jupyter Notebook
output_notebook()

# Isolate the data for the gender choice
female = df[df['Sex'] == 'Female']
male = df[df['Sex'] == 'Male']

# Create a ColumnDataSource object for each team
female_cds = ColumnDataSource(female)
male_cds = ColumnDataSource(male)


# In[13]:


# Create and configure the figure
fig_1 = figure(plot_height=400, plot_width=800,
             title='GENSHIN IMPACT',
             x_axis_label='ATK', y_axis_label='DEF')

# Render the race as step lines
fig_1.circle('ATK', 'DEF', 
         color='#CE1141', legend_label='Female', 
         source=female_cds)
fig_1.circle('ATK', 'DEF', 
         color='#006BB6', legend_label='Male', 
         source=male_cds)

# Move the legend to the upper left corner
fig_1.legend.location = 'top_left'

#Hide legend
fig_1.legend.click_policy="hide"


# Format the tooltip
tooltips = [
            ('Nama Karakter','@Name'),('Nation','@Nation'),
            (' Element', '@Element'),
            ( 'Weapon', '@Weapon'),
            ('Ascension Stat','@AscensionStat'),
            ('Ascension Stat Value','@ASV'),
           ]

# Add the HoverTool to the figure
fig_1.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_1)


# In[14]:


# Create and configure the figure
fig_2 = figure(plot_height=400, plot_width=800,
             title='GENSHIN IMPACT',
             x_axis_label='HP', y_axis_label='ATK')

# Render the race as step lines
fig_2.circle('HP', 'ATK', 
         color='#CE1141', legend_label='Female', 
         source=female_cds)
fig_2.circle('HP', 'ATK', 
         color='#006BB6', legend_label='Male', 
         source=male_cds)

# Move the legend to the upper left corner
fig_2.legend.location = 'top_left'

#Hide legend
fig_2.legend.click_policy="hide"

# Format the tooltip
tooltips = [
            ('Nama Karakter','@Name'),('Nation','@Nation'),
            (' Element', '@Element'),
            ( 'Weapon', '@Weapon'),
            ('Ascension Stat','@AscensionStat'),
            ('Ascension Stat Value','@ASV'),
           ]

# Add the HoverTool to the figure
fig_2.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_2)

# In[15]:


# Create and configure the figure
fig_3 = figure(plot_height=400, plot_width=800,
             title='GENSHIN IMPACT',
             x_axis_label='HP', y_axis_label='DEF')

# Render the race as step lines
fig_3.circle('HP', 'DEF', 
         color='#CE1141', legend_label='Female', 
         source=female_cds)
fig_3.circle('HP', 'DEF', 
         color='#006BB6', legend_label='Male', 
         source=male_cds)

# Move the legend to the upper left corner
fig_3.legend.location = 'top_left'

#Hide legend
fig_3.legend.click_policy="hide"

# Format the tooltip
tooltips = [
            ('Nama Karakter','@Name'),('Nation','@Nation'),
            (' Element', '@Element'),
            ( 'Weapon', '@Weapon'),
            ('Ascension Stat','@AscensionStat'),
            ('Ascension Stat Value','@ASV'),
           ]

# Add the HoverTool to the figure
fig_3.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_3)


# In[16]:


# Create two panels, one for each conference
atkdef_panel = Panel(child= fig_1, title='Perbandinga ATK & DEF')
hpatk_panel = Panel(child= fig_2, title='Perbandingan HP & ATK')
hpdef_panel = Panel(child= fig_3, title='Perbandingan HP & DEF')

# Assign the panels to Tabs
tabs = Tabs(tabs=[atkdef_panel, hpatk_panel, hpdef_panel])

# Show the tabbed layout
show(tabs)

bokeh serve --show visdat-finalproject.py
