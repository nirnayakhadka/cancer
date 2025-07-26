import pandas as pd

df = pd.read_csv('/home/nirnaya/Downloads/archive/synthetic_prostate_cancer_risk.csv')
df['smoking'] = df['smoking'].map({'Yes': 1, 'No': 0})
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='diagnosis', data=df)
sns.boxplot(x='diagnosis', y='age', data=df)
plt.show()