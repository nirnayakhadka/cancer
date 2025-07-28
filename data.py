import pandas as pd

def load_data():
    """
    Load the prostate cancer risk dataset and preprocess it.
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame with relevant features.
    """
    # Load the dataset
    df = pd.read_csv('/home/nirnaya/Downloads/archive/synthetic_prostate_cancer_risk.csv')
    
    # Map categorical variables to numerical values
    
    df['smoker'] = df['smoker'].map({'Yes': 1, 'No': 0})
    df['family_history'] = df['family_history'].map({'Yes': 1, 'No': 0})
    df['regular_health_checkup'] = df["regular_health_checkup"].map({'Yes': 1, 'No': 0})
    df['risk_level'] = df['risk_level'].map({'Low': 0, 'Medium': 1, 'High': 2})
    # One-hot encoding for categorical variables
    df = pd.get_dummies(df, columns=['alcohol_consumption', 'diet_type', 
                                      'physical_activity_level', 'mental_stress_level', 
                                      'prostate_exam_done'], drop_first=True)
    
    return df






