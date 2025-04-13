
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
from scipy.stats import t

# Load and clean data
df = pd.read_csv('remaining_behavior_ext.csv')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
df = df.dropna(subset=['sequence_length(count)', 'num_unique_apis'])

X = df[['sequence_length(count)']]
y = df['num_unique_apis']

title = 'Figure 13: Predicting Unique APIs from Sequence Length'

# Fit model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Predict for new values
new_lengths = pd.DataFrame({'sequence_length(count)': [10, 50, 100, 200, 500]})
predicted_apis = model.predict(new_lengths.values)

# Print predictions
print("Predicted Unique APIs for given Sequence Lengths:")
for s, p in zip(new_lengths['sequence_length(count)'], predicted_apis):
    print(f"  {s} sequence length → {p:.2f} unique APIs")

# Confidence intervals (approximation)
n = len(X)
mean_x = X['sequence_length(count)'].mean()
se = np.sqrt(np.sum((y - y_pred)**2) / (n - 2))
t_val = t.ppf(0.975, df=n - 2)

# Prediction range
x_range = np.linspace(X['sequence_length(count)'].min(), X['sequence_length(count)'].max(), 300).reshape(-1, 1)
y_range_pred = model.predict(x_range)
ci = t_val * se * np.sqrt(
    1 + (x_range.flatten() - mean_x)**2 / np.sum((X['sequence_length(count)'] - mean_x)**2)
)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label='Datapoints', color='teal')
plt.plot(x_range, y_range_pred, color='black', linewidth=2, label=f'Linear Regression (R² = {r2:.2f})')
plt.fill_between(x_range.flatten(),
                 y_range_pred - ci,
                 y_range_pred + ci,
                 color='gray', alpha=0.3, label='~95% Prediction Interval')

# Formatting
plt.xlabel('Sequence Length (count)', fontsize=14, labelpad=15)
plt.ylabel('Number of Unique APIs', fontsize=14, labelpad=15)
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=False, fontsize=12)
plt.subplots_adjust(bottom=0.3)
plt.tight_layout()
plt.savefig('figure_13.png', dpi=300, bbox_inches='tight')
plt.show()
