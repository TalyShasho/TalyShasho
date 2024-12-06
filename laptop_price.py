import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#import file 
file_path = r"C:\Users\matzk\Python\advance-python-\laptop_price - dataset.xlsx"

# Read the file
data = pd.read_excel(file_path)

# convert column 'Price (Euro)' to number and eliminates no valid values
data['Price (Euro)'] = pd.to_numeric(data['Price (Euro)'], errors='coerce')

data = data.dropna(subset=['Price (Euro)'])

# 1
# column product as axis x
x_labels = data['Product']

# graph
plt.figure(figsize=(15, 8))
plt.scatter(x_labels.index, data['Price (Euro)'], alpha=0.7, c='purple')
plt.title('Prices of all Laptops', fontsize=16)
plt.xlabel('Laptop', fontsize=14)
plt.ylabel('price (Euro)', fontsize=14)

# x-axis is overcrowded because we have a lot of data, I displaed fewer labels while retaining all data points in the graph  to avoid cluttering
step = 9  # Display a label for every 9 laptops
plt.xticks(ticks=x_labels.index[::step], labels=x_labels[::step], rotation=90, fontsize=7)

plt.text(
    0.95, 0.95,
    f" Showing only each {step}° name for clarity",
    fontsize=10,
    color="red",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    bbox=dict(boxstyle="round,pad=0.3", edgecolor="red", facecolor="white", alpha=0.8)
)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2
# Calculate the average laptop price for each company
average_prices = data.groupby('Company')['Price (Euro)'].mean()

# Find the company with the most expensive laptops on average
most_expensive_company = average_prices.idxmax()
highest_avg_price = average_prices.max()

print("Average laptop price for each company:")
for company, price in average_prices.items():
    print(f"{company}: {price:.2f} Euros")

print("\nCompany with the most expensive laptops on average:")
print(f"{most_expensive_company} with an average price of {highest_avg_price:.2f} Euros")


# 3
# make names uniform
def clean_opsys(os):
    os = os.lower()

    if "windows" in os:
        return "Windows"
    elif "mac" in os:
        return "MacOS"
    elif "linux" in os:
        return "Linux"
    elif "no os" in os or "dos" in os:
        return "No OS"
    elif "android" in os:
        return "Android"
    else:
        return "Chrome"

    # applay function to clean column


data['OpSys_Cleaned'] = data['OpSys'].apply(clean_opsys)
unique_opsys = data['OpSys_Cleaned'].unique()

print("\nOperatin systems:")
print(unique_opsys)

# 4
# colors
palette = sns.color_palette("husl", n_colors=len(data['OpSys_Cleaned'].unique()))

plt.figure(figsize=(15, 10))
sns.boxplot(x='OpSys_Cleaned', y='Price (Euro)', data=data, palette=palette,
            hue='OpSys_Cleaned', order=data['OpSys_Cleaned'].unique(), legend=False)
plt.title('Price distribution for operative system', fontsize=16)
plt.xlabel('Operatie system', fontsize=14)
plt.ylabel('Price (Euro)', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 5
# CRAM colum to number
data['RAM (GB)'] = pd.to_numeric(data['RAM (GB)'], errors='coerce')

# take out invalid valeus
data = data.dropna(subset=['Price (Euro)', 'RAM (GB)'])

# person correlation calculation (numpy)
correlation_matrix = np.corrcoef(data['RAM (GB)'], data['Price (Euro)'])
correlation = correlation_matrix[0, 1]

print(f"Pearson coeficient (r): {correlation:.2f}")
if abs(correlation) > 0.4:
    print("there is a significan correlation between RAM and price.")
else:
    print("there is not a significan correlation between RAM and price.")

# graph
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['RAM (GB)'], y=data['Price (Euro)'], color='blue', label='Data')

if abs(correlation) > 0.2:
    m, b = np.polyfit(data['RAM (GB)'], data['Price (Euro)'], 1)
    plt.plot(data['RAM (GB)'], m * data['RAM (GB)'] + b, color='green',
             label=f'pearson correlation (r={correlation:.2f})')

plt.title('Correlation between RAM and price', fontsize=16)
plt.xlabel('RAM (GB)', fontsize=14)
plt.ylabel('Price (Euro)', fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.show()


# 6
# Creates new colunm "Storage type" fm memory column
def extract_storage_type(memory):
    # chek memory type
    memory = str(memory).lower()
    if 'ssd' in memory:
        return 'SSD'
    elif 'hdd' in memory:
        return 'HDD'
    else:
        return 'Flash Storage'

    # apply function


data['Storage type'] = data['Memory'].apply(extract_storage_type)

print(f'soce of data  DataFrame: {len(data)}')
print(data[['Memory', 'Storage type']])

'''BONUS'''

# 1
# Count the frequency of each CPU company
cpu_counts = data['CPU_Company'].value_counts()

# Most popular CPU company
most_popular_cpu = cpu_counts.idxmax()
most_popular_count = cpu_counts.max()

print(f"The most popular CPU company is '{most_popular_cpu}' with {most_popular_count} laptops.")

# histogram of CPU companies
plt.figure(figsize=(10, 6))
cpu_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Frequency of CPU Companies', fontsize=16)
plt.xlabel('CPU Company', fontsize=14)
plt.ylabel('Number of Laptops', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2
#  columns to numbers
data['Weight (kg)'] = pd.to_numeric(data['Weight (kg)'], errors='coerce')

# Filter out rows with weight greater than 6 kg
data = data[(data['Weight (kg)'] <= 6) & (data['Weight (kg)'].notna()) & (data['Price (Euro)'].notna())]

# Calculate Pearson correlation
correlation = np.corrcoef(data['Weight (kg)'], data['Price (Euro)'])[0, 1]

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Weight (kg)'], data['Price (Euro)'], alpha=0.7, c='green',
            label=f'Pearson Correlation: {correlation:.2f}')
plt.title('Relation Between Weight and Price', fontsize=16)
plt.xlabel('Weight (kg)', fontsize=14)
plt.ylabel('Price (Euro)', fontsize=14)
plt.grid(alpha=0.7, linestyle='--')

#  regression line
m, b = np.polyfit(data['Weight (kg)'], data['Price (Euro)'], 1)
plt.plot(data['Weight (kg)'], m * data['Weight (kg)'] + b, color='purple', label='Regression Line')

plt.figtext(0.99, 0.01, 'There is no significant Pearson correlation.',
            horizontalalignment='right', fontsize=10, color='red')

#  legend
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()