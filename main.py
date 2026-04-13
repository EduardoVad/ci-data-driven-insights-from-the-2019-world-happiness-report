import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("world_happiness.csv")

# Your code starts here

# Select the top 10 countries by Score
top10 = df.nlargest(10, 'Score')[['Country or region', 'Score']]

# Print exact data values for the bar plot
data_values = {
    'Country or region': top10['Country or region'].tolist(),
    'Score': top10['Score'].tolist()
}
print("Data for bar plot:", data_values)

# Create the bar plot

plt.figure(figsize=(10, 6))
plt.bar(top10['Country or region'], top10['Score'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country or Region')
plt.ylabel('Happiness Score')
plt.title('Top 10 Happiest Countries (2019) by Score')
plt.tight_layout()
plt.show()