# linear algebra
import numpy as np 
# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd 
from datetime import timedelta

import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import warnings
warnings.filterwarnings("ignore")
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
#country_vaccinations.csv
vaccinations_data = pd.read_csv('../input/covid-world-vaccination-progress/country_vaccinations.csv')

#country_vaccinations_by_manufacturer.csv
vaccinations_by_mf = pd.read_csv('../input/covid-world-vaccination-progress/country_vaccinations_by_manufacturer.csv')
#country_vaccinations.csv
vaccinations_data.head()
#country_vaccinations_by_manufacturer.csv
vaccinations_by_mf.tail()
#data.isnull().sum(axis=0)
# Get the null values use isnull() 
null_values = vaccinations_data.isnull().sum()
null_values
vaccinations_per_country = vaccinations_data.groupby('country')['daily_vaccinations'].sum()
print(vaccinations_per_country)
#top 5 country with total vaccinations


vaccinations_per_country = vaccinations_data.groupby('country')['total_vaccinations'].sum().sort_values(ascending=False).head(5)
vaccinations_per_country.head(5)
#bargraph
#plt.figure(figsize=(7,7))
sns.set_theme(style="whitegrid")
sns.barplot(x=vaccinations_per_country.values, y=vaccinations_per_country.index, orient='h')
plt.xlabel("Total Vaccinations")
plt.ylabel("Country")
vaccinations_by_mf.vaccine.value_counts
# Worldwide vaccine count per manufacturer
# am using mean instead of sum since there is 2 doses
vaccine_tot_per_mf = vaccinations_by_mf.groupby('vaccine')['total_vaccinations'].mean().\
                to_frame().reset_index()

vaccine_tot_per_mf.sort_values(by=['total_vaccinations'], ascending=True)
# country_vaccinations_by_manufacturer.csv dataset
vaccine_tot_per_mf= vaccine_tot_per_mf.sort_values('total_vaccinations')
plt.figure(figsize=(10, 6))
plt.bar(vaccine_tot_per_mf['vaccine'], vaccine_tot_per_mf['total_vaccinations'], )
minimum = 0
maximum = vaccine_tot_per_mf['total_vaccinations'].max
plt.title("Worldwide Total vaccinations by manufacturer")
#plt.xlabel('vaccine')
plt.xticks(rotation=45, ha='right')
plt.show()
alt.Chart(vaccine_tot_per_mf).mark_bar().encode(
    alt.X('vaccine:N', sort='-y', title='vaccinations manufacturer'),
    alt.Y('total_vaccinations:Q'),
    alt.Color('vaccine:N'),
    alt.Tooltip(['vaccine', 'total_vaccinations'])
).properties(
    width = 600,
    height = 450
)
vaccinations_swe = vaccinations_data[vaccinations_data['country'] == 'Sweden']
vaccinations_by_mf_swe = vaccinations_by_mf[vaccinations_by_mf['location'] == 'Sweden']

vaccinations_by_mf_swe = vaccinations_by_mf_swe.groupby('vaccine')['total_vaccinations'].mean().\
                to_frame().reset_index()

vaccinations_by_mf_swe.sort_values(by=['total_vaccinations'], ascending=True)
# Total vaccinations by manufacturer at Sweden
vaccinations_by_mf_swe= vaccinations_by_mf_swe.sort_values('total_vaccinations')
plt.figure(figsize=(10, 6))
plt.bar(vaccinations_by_mf_swe['vaccine'], vaccinations_by_mf_swe['total_vaccinations'], )
minimum = 0
#maximum = vaccinations_by_mf_swe['total_vaccinations'].max
#plt.ylim(0,29000000000)
plt.title("Sweden")
#plt.xlabel('vaccine')
plt.xticks(rotation=45, ha='right')
plt.show()
#vaccines used Sweden / USA / United Arab Emirates 
vaccinations_ar = vaccinations_data[vaccinations_data
                                    ['country'].isin(['Sweden',
                                                      'United Arab Emirates', 'United States'])]                           

vaccinations_ar = vaccinations_ar[['country', 'vaccines']]

vaccinations_ar = vaccinations_ar.groupby(["country", "vaccines"]).count()

vaccinations_ar