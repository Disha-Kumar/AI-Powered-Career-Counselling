from flask import Flask, jsonify, request, render_template
from data.collect_data import collect_data
from data.process_data import process_data
from ml.train_model import train_model
from app.models import recommend_career

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    interests = data['interests']
    strengths = data['strengths']
    
    df = collect_data()
    df_processed = process_data(df)
    model = train_model(df_processed)
    career = recommend_career(interests, strengths, model, df_processed)
    
    return jsonify({'recommended_career': career})

if __name__ == '__main__':
    app.run(debug=True)
