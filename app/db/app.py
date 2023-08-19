from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

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
    app.run(port=5555)
