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
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(top10['Country or region'], top10['Score'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Country or Region')
plt.ylabel('Happiness Score')
plt.title('Top 10 Happiest Countries (2019) by Score')
plt.tight_layout()
plt.show()````
