import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

data = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(data.head())

# Sales by Product

product_sales = data.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(product_sales)

# Plot Product Sales

product_sales.plot(kind='bar', title='Sales by Product')
plt.ylabel("Sales")
plt.show()

# Sales by Region

region_sales = data.groupby("Region")["Sales"].sum()

# Plot Region Sales

sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Sales by Region")
plt.show()
