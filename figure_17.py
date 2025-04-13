import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Load data
df = pd.read_csv('remaining_behavior_ext.csv')

# Drop any columns starting with "Unnamed"
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]

# Focus on the specific columns we need
# Ensure the columns exist in the dataset
x_col = 'api_access_uniqueness'
y_col = 'num_unique_apis'

# Clean the data by removing rows with NaN values in our target columns
df_clean = df[[x_col, y_col]].dropna()

# Prepare data for regression
X = df_clean[[x_col]]
y = df_clean[y_col]

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='Datapoint')
plt.plot(X, y_pred, color='red', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')

# Add regression equation to the plot
slope = model.coef_[0]
intercept = model.intercept_
equation = f'y = {slope:.4f}x + {intercept:.4f}'
plt.annotate(equation, xy=(0.05, 0.95), xycoords='axes fraction', 
             fontsize=12, ha='left', va='top', 
             bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.7))

# Enhanced formatting with title split over two lines
plt.xlabel(x_col, fontsize=14, labelpad=15)
plt.ylabel(y_col, fontsize=14, labelpad=15)
plt.title('Figure 17:\nLinear Fit -' + f'{x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.subplots_adjust(bottom=0.25)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False, fontsize=14)

# Add statistical information
stats_text = (f'R² = {r2:.4f}\n'
              f'Slope = {slope:.4f}\n'
              f'Intercept = {intercept:.4f}')
plt.annotate(stats_text, xy=(0.75, 0.25), xycoords='axes fraction',
             fontsize=12, ha='left', va='top',
             bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.7))

plt.tight_layout()
plt.show()

# Print regression details
print(f"Regression Analysis: {x_col} vs {y_col}")
print(f"Coefficient (Slope): {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r2:.4f}")
