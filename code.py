# Exploratory Data Analysis

#Loading data with Pandas
#Descriptive statistics of data
#Data visualization
#Hypothesis investigation

##Import Packages


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Shows plots in jupyter notebook
import matplotlib

# Set plot style
sns.set(color_codes=True)

#2. Loading data with Pandas
#We need to load client_data.csv and price_data.csv into individual dataframes so that we can work with them in Python

client_df = pd.read_csv('/Users/renu/Library/Containers/com.microsoft.Excel/Data/Downloads/client_data.csv')
price_df = pd.read_csv('/Users/renu/Library/Containers/com.microsoft.Excel/Data/Downloads/price_data.csv')

##Let us look at the data provided

client_df.head(3)

price_df.head(3)
print("hello")








