from flask import Flask, render_template, request # type: ignore
from datetime import datetime

app = Flask(__name__)

transactions = []

def detect_fraud(card_number, expiry_date, cvv):
    # Simple fraud detection rule
    if cvv == '123':
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_payment', methods=['POST'])
def process_payment():
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    amount = request.form['amount']

    transaction = {
        'card_number': card_number,
        'amount': amount,
        'cvv': cvv,
        'time': datetime.now()
    }
    transactions.append(transaction)
    
    if detect_fraud(card_number, expiry_date, cvv):
        return "Fraud detected! Payment declined."
    else:
        return "Payment processed successfully!"

@app.route('/insights')
def insights():
    insights_data = generate_insights(transactions)
    return insights_data

def generate_insights(transactions):
    # Example: Find the most common transaction time
    times = [t['time'].hour for t in transactions]
    most_common_time = max(set(times), key=times.count)
    
    return f"Most common transaction time is {most_common_time}:00."

if __name__ == '__main__':
    app.run(debug=True)
