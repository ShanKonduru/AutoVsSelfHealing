from flask import Flask, request, jsonify
import sqlite3
import datetime

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8888"}})

def setup_database():
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    # Check if the calculations table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='calculations'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''
            CREATE TABLE calculations (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                OperandOne REAL,
                OperandTwo REAL,
                Operator TEXT,
                Result REAL,
                DateOfCreation TEXT
            )
        ''')
        print("Table 'calculations' created.")

    conn.commit()
    conn.close()

@app.route('/get_all_records', methods=['GET'])
def get_all_records():
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    # Retrieve all records from the calculations table
    cursor.execute('SELECT * FROM calculations')
    records = cursor.fetchall()

    conn.close()

    # Convert records to a list of dictionaries
    records_list = []
    for record in records:
        record_dict = {
            'Id': record[0],
            'OperandOne': record[1],
            'OperandTwo': record[2],
            'Operator': record[3],
            'Result': record[4],
            'DateOfCreation': record[5]
        }
        records_list.append(record_dict)

    return jsonify(records_list)


@app.route('/insert', methods=['POST'])
def insert_calculation():
    data = request.get_json()

    operand_one = data['operand_one']
    operand_two = data['operand_two']
    operator = data['operator']
    result = data['result']
    
    # Get the current date and time
    date_of_creation = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    # Insert the record into the database
    cursor.execute('''
        INSERT INTO calculations (OperandOne, OperandTwo, Operator, Result, DateOfCreation)
        VALUES (?, ?, ?, ?, ?)
    ''', (operand_one, operand_two, operator, result, date_of_creation))

    conn.commit()
    conn.close()

    return jsonify({"message": "Record inserted successfully"})

if __name__ == '__main__':
    setup_database()
    app.run(debug=True, host='0.0.0.0', port=5555)
