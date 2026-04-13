import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load dataset
df = pd.read_csv("world_happiness.csv")

print(df.head())

# Task 1: Select and visualize the top 10 countries by Score
top10 = df.nlargest(10, 'Score')[['Country or region', 'Score']]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.barh(top10['Country or region'], top10['Score'])
plt.xlabel('Happiness Score')
plt.title('Top 10 Happiest Countries (2019)')
plt.tight_layout()
plt.show()

# Task 2: Compare the average GDP per capita between the top 20 and bottom 20 countries by Score.

top20GDP = df.nlargest(20, 'Score')[['Country or region', 'Score', 'GDP per capita']]
bottom20GDP = df.nsmallest(20, 'Score')[['Country or region', 'Score', 'GDP per capita']]

avg_gdp_top = top20GDP['GDP per capita'].mean()
avg_gdp_bottom = bottom20GDP['GDP per capita'].mean()

print("Top 20 Countries:")
print(top20GDP['Country or region'].tolist())

print("\nBottom 20 Countries:")
print(bottom20GDP['Country or region'].tolist())

labels = ['Top 20', 'Bottom 20']
values = [avg_gdp_top, avg_gdp_bottom]

plt.figure(figsize = (10, 6))
plt.bar(labels, values, color = 'green')
plt.ylabel('Average GDP per Capita')
plt.title('Average GDP per Capita: Top 20 vs Bottom 20 Countries by Happiness')
plt.tight_layout()
plt.show()

# Task: Plot Score against Social support to examine their relationship.

plt.figure(figsize=(10, 6))
plt.scatter(df['Social support'], df['Score'])

m, b = np.polyfit(df['Social support'], df['Score'], 1)
plt.plot(df['Social support'], m * df['Social support'] + b, color='red')

plt.xlabel('Social Support')
plt.ylabel('Happiness Score')
plt.title('Social Support vs Happiness Score (2019)')
plt.tight_layout()
plt.show()

#Task 4: Identify the three indicators (from GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity, Perceptions of corruption) most correlated with Score.

indicators = ['GDP per capita', 'Social support', 'Healthy life expectancy', 
              'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

correlations = df[indicators + ['Score']].corr()['Score'].drop('Score')

print("Absolute (for ranking):")
print(correlations.abs().sort_values(ascending=False).head(3))

print("\nActual values (to see direction):")
print(correlations.sort_values(ascending=False))

#Task 5: Compare the median Healthy life expectancy between countries with Score above 7.0 and those below 5.0.

high_score = df[df['Score']>7.0]
low_score = df[df['Score']<5.0]

median_hl_high = high_score['Healthy life expectancy'].median()
median_hl_low = low_score['Healthy life expectancy'].median()

print(f"Median Healthy Life Expectancy - High Score countries (>7.0): {median_hl_high:.2f}")
print(f"Median Healthy Life Expectancy - Low Score countries (<5.0): {median_hl_low:.2f}")

health_labels = ['High Score (>7.0)', 'Low Score (<5.0)']
health_values = [median_hl_high, median_hl_low]

plt.figure(figsize = (10,6))
plt.bar(health_labels, health_values, color = 'Red')
plt.ylabel('Median Healthy life expectancy')
plt.title('Healthy Life Expectancy: High vs Low Happiness Countries')
plt.tight_layout()
plt.show()