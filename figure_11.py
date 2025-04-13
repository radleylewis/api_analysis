import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
title = "Figure 10: Session Duration (IQR-filtered)"

# Function to remove outliers using the IQR method
def filter_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    return series[(series >= Q1 - 1.5 * IQR) & (series <= Q3 + 1.5 * IQR)]

# Load the dataset
df = pd.read_csv('remaining_behavior_ext.csv')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  # Drop unnamed columns

# Filter the column
inter_api_duration_filtered = filter_iqr(df['vsession_duration(min)'])

# Plot
plt.figure(figsize=(10, 4))
sns.boxplot(x=inter_api_duration_filtered, color='lightgreen', linewidth=1.5, fliersize=0, showfliers=False)

# Formatting
plt.title(title, fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Session Duration (IQR-filtered)', fontsize=14, labelpad=15)
plt.ylabel('', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks([])
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('figure_9.png', dpi=300, bbox_inches='tight')
plt.show()
