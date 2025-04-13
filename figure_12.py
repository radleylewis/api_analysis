import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

title = 'Figure 12: Linear Fit - Sequence Length vs Unique APIs'

# Load data
df = pd.read_csv('remaining_behavior_ext.csv')
df_clean = df[['sequence_length(count)', 'num_unique_apis']].dropna()
X = df_clean[['sequence_length(count)']]
y = df_clean['num_unique_apis']

# Fit model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='Datapoint')
plt.plot(X, y_pred, color='red', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')

# Plot settings with enhanced spacing
plt.xlabel('Sequence Length (count)', fontsize=14, labelpad=15)  # extra padding from axis
plt.ylabel('Number of Unique APIs', fontsize=14, labelpad=15)
plt.title(title, fontsize=18, fontweight='bold', pad=20)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)

# Adjust layout and add more space between plot and legend
plt.subplots_adjust(bottom=0.25)  # move plot up to create space above legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False, fontsize=14)

plt.tight_layout()
plt.show()
