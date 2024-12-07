import pandas as pd
import numpy as np

def process_data(df):
    # Convert categorical data to numerical data
    df_processed = pd.get_dummies(df, columns=['interests', 'strengths', 'career_preference'])
    return df_processed

# Example usage
df_processed = process_data(df)
print(df_processed)
