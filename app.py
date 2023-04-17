import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def load_csv_data():
    df = pd.read_csv('data/1950-2021_torn.csv')
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)


