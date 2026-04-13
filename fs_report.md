-e This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
world_happiness.csv
````
-e 
# Files
-e 
## File: world_happiness.csv
````
Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption
1,Finland,7.769,1.340,1.587,0.986,0.596,0.153,0.393
2,Denmark,7.600,1.383,1.573,0.996,0.592,0.252,0.410
````
-e 
## File: main.py
````
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
plt.show()````
