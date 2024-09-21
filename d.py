import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Load the dataset (assuming you exported it to a CSV file)
df = pd.read_csv('smartprix_final.csv')

# Display the first 5 rows of the dataset
print(df.head())    

# Check for missing values and data types
print(df.info())

# Summary statistics
print(df.describe())

#we want to compare the prices of the 5 most expensive smartphones
df_expensive = df.sort_values('price', ascending=False).head(5)

#we will create a plot with automatic size
plt.figure(figsize=(10, 10))
#plt.figure(figsize)
#we want to concat the model and brand_name columns
df_expensive['model'] = df_expensive['brand_name'] + ' ' + df_expensive['model']
sns.barplot(x='model', y='price', data=df_expensive)
plt.title('Comparison of the 5 Most Expensive Smartphone Prices')
plt.xticks(rotation=45)
plt.show()
plt.savefig('smartphone_prices.png')

#we want to compare the ratings of the 5 best-rated smartphones
df_rating = df.sort_values('rating', ascending=False).head(5)

plt.figure(figsize=(10, 10))
sns.barplot(x='model', y='rating', data=df_rating)
plt.title('Comparison of the 5 Most Best_rated Smartphone Ratings')
plt.xticks(rotation=45)
plt.show()
plt.savefig('smartphone_ratings.png')

# 5G Availability Comparison
# Count the number of True and False values for 'has_5g'
has_5g_counts = df['has_5g'].value_counts()

# Labels for the pie chart
labels = ['5G Available', '5G Not Available']

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(has_5g_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title('5G Availability in Smartphones')
plt.show()
plt.savefig('5g_availability.png')

# NFC Availability Comparison
has_nfc_counts = df['has_nfc'].value_counts()

# Labels for the pie chart
labels = ['NFC Available', 'NFC Not Available']

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(has_nfc_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral'])
plt.title('NFC Availability in Smartphones')
plt.show()
plt.savefig('nfc_availability.png')

# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
corr = numeric_df.corr()

# Plot the heatmap using matplotlib
plt.figure(figsize=(12, 8))
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

# Set ticks for labels
plt.xticks(np.arange(len(corr.columns)), corr.columns, rotation=45, ha='right')
plt.yticks(np.arange(len(corr.columns)), corr.columns)
plt.title('Correlation Between Smartphone Features')
plt.show()
plt.savefig('correlation_heatmap.png')
