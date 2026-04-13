import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("world_happiness.csv")

print(df.head())
# Your code starts here

# Select the top 10 countries by Score
top10 = df.nlargest(10, 'Score')[['Country or region', 'Score']]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.barh(top10['Country or region'], top10['Score'])
plt.xlabel('Happiness Score')
plt.title('Top 10 Happiest Countries (2019)')
plt.tight_layout()
plt.show()

# Task: Compare the average GDP per capita between the top 20 and bottom 20 countries by Score.

top20GDP = df.nlargest(20, 'Score')[['Country or region', 'Score', 'GDP per capita']]
bottom20GDP = df.nsmallest(20, 'Score')[['Country or region', 'Score', 'GDP per capita']]

avg_gdp_top = top20GDP['GDP per capita'].mean()
avg_gdp_bottom = bottom20GDP['GDP per capita'].mean()

labels = ['Top 20', 'Bottom 20']
values = [avg_gdp_top, avg_gdp_bottom]

plt.figure(figsize = (10, 6))
plt.bar(labels, values, color = 'green')
plt.ylabel('Average GDP per Capita')
plt.title('Average GDP per Capita: Top 20 vs Bottom 20 Countries by Happiness')
plt.tight_layout()
plt.show()