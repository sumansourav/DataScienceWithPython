#!/usr/bin/env/python3

import pandas as pd

# Using matplotlib as the primary visaulization tool here
import matplotlib.pyplot as plt
# Using seaborn package to facilitate enhanced boxplot visualizations as required
import seaborn as sns

# The following lines supresses warnings that pops out during program execution when numeric fields have 0 values.
import warnings
warnings.filterwarnings('ignore')

__author__ = 'sumansourav'

''' The following code creates a visualization of the US Gross amount by Genre of the available movies.'''

# Load data set into memory for calculation and manipulation
mov = pd.read_csv('Movies_Financials_Data.csv', encoding='ISO-8859-1')

# Create a data sub-set with required studios only.
required_studios_filter = ['Buena Vista Studios', 'Sony', 'Universal', 'Paramount Pictures', 'WB', 'Fox']
mov_subset = mov[mov.Studio.isin(required_studios_filter)]

# Create a data sub-set with required genres only.
required_genres_filter = ['action', 'comedy', 'adventure', 'animation', 'drama']
mov_subset = mov_subset[mov_subset.Genre.isin(required_genres_filter)]

#
# Create the plots and styles

# Create the box plot
sns.set(style='darkgrid', palette='muted', color_codes=True)
bxplt = sns.boxplot(data=mov_subset, x='Genre', y='Gross % US', orient='v', color='lightgray', showfliers=False)

# Set the transparency
plt.setp(bxplt.artists, alpha=0.5)

# Create the scatterplot
scplot = sns.stripplot(data=mov_subset, x='Genre', y='Gross % US', jitter=True, size=5, hue='Studio', alpha=0.7)

# Final touches and presentation
bxplt.axes.set_title("Domestic Gross % by Genre", fontsize=30)
bxplt.set_xlabel('Genre', fontsize=22)
bxplt.set_ylabel('Gross % US', fontsize=22)
bxplt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.show()

