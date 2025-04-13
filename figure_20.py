import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
title = 'Figure 20: Predicting Unique APIs from Sessions (Bots Only)'

# Load and clean data
df = pd.read_csv('remaining_behavior_ext.csv')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
df = df.dropna(subset=['num_sessions', 'num_unique_apis', 'behavior_type'])

# Filter for bots only
df_bot = df[df['behavior_type'] == 'bot']
X = df_bot[['num_sessions']]
y = df_bot['num_unique_apis']

# Fit model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Prediction range for the line
x_range = np.linspace(X['num_sessions'].min(), X['num_sessions'].max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)

# Plot with regression line but no confidence band
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='bot datapoints', color='orange')
plt.plot(x_range, y_range_pred, color='black', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')

# Formatting
plt.xlabel('Number of Sessions', fontsize=14, labelpad=15)
plt.ylabel('Number of Unique APIs', fontsize=14, labelpad=15)
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=False, fontsize=12)
plt.subplots_adjust(bottom=0.3)
plt.tight_layout()
plt.show()
