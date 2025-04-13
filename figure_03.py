import pandas as pd
import matplotlib.pyplot as plt

title = 'Figure 3: Number of API Calls (Binned)'

df = pd.read_csv('remaining_behavior_ext.csv', sep=',\s*', engine='python')
df = df.loc[:, ~df.columns.str.startswith('Unnamed')]  

bins = [0, 10, 20, 30, 40, 50, 100, 200, 500, 1000, float('inf')]
labels = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-100', '101-200', '201-500', '501-1000', '1000+']
df['sequence_length_binned'] = pd.cut(df['sequence_length(count)'], bins=bins, labels=labels)

counts = df['sequence_length_binned'].value_counts().sort_index(ascending=False)

plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='darkblue')

plt.xlabel('Number of API Calls (Binned)', fontsize=14, labelpad=15)
plt.ylabel('Frequency', fontsize=14, labelpad=15)
plt.title(title, fontsize=22, fontweight='bold', pad=20)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.subplots_adjust(bottom=0.25)
plt.tight_layout()
plt.show()
plt.savefig('figure_3.png')
