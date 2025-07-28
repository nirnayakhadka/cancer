import seaborn as sns
import matplotlib.pyplot as plt
from data import load_data


df = load_data()
# Age vs Risk Level
plt.figure()
sns.boxplot(x='risk_level', y='age', data=df)
plt.title('Age vs Risk Level')
plt.tight_layout()
plt.savefig('age_vs_risk_level.png')


# BMI vs Risk Level
plt.figure()
sns.boxplot(x='risk_level', y='bmi', data=df)
plt.title('BMI vs Risk Level')

plt.tight_layout()
plt.savefig('bmi_vs_risk_level.png')

# Sleep Hours vs Risk Level
plt.figure()
sns.boxplot(x='risk_level', y='sleep_hours', data=df)
plt.title('Sleep Hours vs Risk Level')
plt.show()
