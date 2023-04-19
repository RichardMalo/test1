import os
import pandas as pd
from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tornadograph.db')
    conn.row_factory = sqlite3.Row
    return conn

# @app.route('/')
# def index():
#     data = load_csv_data()
#     return render_template('index.html', data=data)

@app.route('/data')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM tornadoes').fetchall()
    conn.close()
    return render_template('index.html', data=data)

# @app.route('/data')
# def load_csv_data():
#     csv_path = os.path.join(os.path.dirname(__file__), 'data', '1950-2021_torn.csv')
#     df = pd.read_csv(csv_path)
#     # Add this line to select specific columns
#     selected_columns = ['yr', 'mag', 'inj', 'fat']  
#     # Update this line to return only the selected columns
#     return df[selected_columns].to_json(orient='records')  

if __name__ == '__main__':
    app.run(debug=True)