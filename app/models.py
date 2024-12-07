def recommend_career(interests, strengths, model, df_processed):
    # Process input data
    input_data = pd.get_dummies(pd.DataFrame([{'interests': interests, 'strengths': strengths}]), columns=['interests', 'strengths'])
    input_data = input_data.reindex(columns=df_processed.columns, fill_value=0).drop(columns=['student_id', 'academic_performance'])
    
    # Predict academic performance
    predicted_performance = model.predict(input_data.values)
    
    # Recommend career based on predicted performance
    career = df_processed.loc[df_processed['academic_performance'] == predicted_performance[0], 'career_preference'].values[0]
    return career
