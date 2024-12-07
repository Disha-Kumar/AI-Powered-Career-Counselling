import pandas as pd

def collect_data():
    # Example data collection: Survey responses, academic records, etc.
    data = {
        'student_id': [1, 2, 3, 4, 5],
        'interests': ['Science', 'Math', 'History', 'Art', 'Technology'],
        'strengths': ['Analysis', 'Problem-Solving', 'Writing', 'Creativity', 'Coding'],
        'academic_performance': [85, 90, 78, 92, 88],
        'career_preference': ['Engineer', 'Data Scientist', 'Historian', 'Artist', 'Software Developer']
    }
    df = pd.DataFrame(data)
    return df

# Example usage
df = collect_data()
print(df)
