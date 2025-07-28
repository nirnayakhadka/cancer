from data import load_data

# in here we will be checking the median values of the risk level for the features smoker, age, bmi, and sleep_hours

df = load_data()

df.groupby('risk_level')[['smoker', 'age', 'bmi', 'sleep_hours']].median()