# Terentev Maksim, 2023

# Data handling
import pandas as pd
import numpy as np
import chardet

from functools import partial

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import TabPanel, Tabs
from bokeh.layouts import row, column, gridplot
from bokeh.plotting import reset_output
from bokeh.models import ColumnDataSource, CDSView, GroupFilter


#Encoder 1 for 'sales' files 
with open('sales_202106.csv', 'rb') as f:
    enc = chardet.detect(f.read()) 
f1 = partial(pd.read_csv, encoding = enc['encoding'])

#Encoder 2 for 'crashes' files
with open('stats_crashes_202106_overview.csv', 'rb') as f:
    enc = chardet.detect(f.read())  
f2 = partial(pd.read_csv, encoding = enc['encoding'])

#Encoder 3 for 'ratings' files
with open('stats_ratings_202106_country.csv', 'rb') as f:
    enc = chardet.detect(f.read())  
f3 = partial(pd.read_csv, encoding = enc['encoding'])

# Read CSV files from the list and store them in three Panda data frames
df_sales = pd.concat(map(f1, ['sales_202106.csv', 'sales_202107.csv','sales_202108.csv', 'sales_202109.csv', 'sales_202110.csv', 'sales_202111.csv', 'sales_202112.csv']))
df_crashes = pd.concat(map(f2, ['stats_crashes_202106_overview.csv', 'stats_crashes_202107_overview.csv', 'stats_crashes_202108_overview.csv', 'stats_crashes_202109_overview.csv', 'stats_crashes_202110_overview.csv', 'stats_crashes_202111_overview.csv', 'stats_crashes_202112_overview.csv']))
df_ratings_country = pd.concat(map(f3, ['stats_ratings_202106_country.csv', 'stats_ratings_202106_overview.csv', 'stats_ratings_202107_country.csv', 'stats_ratings_202107_overview.csv', 'stats_ratings_202108_country.csv', 'stats_ratings_202108_overview.csv', 'stats_ratings_202109_country.csv', 'stats_ratings_202109_overview.csv', 'stats_ratings_202110_country.csv', 'stats_ratings_202110_overview.csv', 'stats_ratings_202111_country.csv', 'stats_ratings_202111_overview.csv', 'stats_ratings_202112_country.csv', 'stats_ratings_202112_overview.csv']))
