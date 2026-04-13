import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("world_happiness.csv")

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