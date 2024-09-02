from datetime import datetime

# Define suspicious IPs and thresholds
SUSPICIOUS_IPS = ['192.168.1.100', '10.0.0.5']
UNUSUAL_AMOUNT_THRESHOLD = 10000  # Amount above which a transaction is considered unusual
UNUSUAL_HOURS = range(0, 6)  # Unusual hours are from midnight to 6 AM

def is_fraud(transaction):
    """
    Check if the transaction is fraudulent based on the given parameters.
    
    Parameters:
    transaction (dict): A dictionary containing transaction details like CVV, IP, amount, and time.
    
    Returns:
    bool: True if the transaction is fraudulent, False otherwise.
    """
    
    # Check if CVV is missing
    if not transaction.get('cvv'):
        print("Fraud detected: No CVV provided.")
        return True
    
    # Check if the IP address is suspicious
    if transaction.get('ip') in SUSPICIOUS_IPS:
        print("Fraud detected: Suspicious IP address.")
        return True
    
    # Check if the transaction amount is unusual
    if transaction.get('amount', 0) > UNUSUAL_AMOUNT_THRESHOLD:
        print("Fraud detected: Unusual transaction amount.")
        return True
    
    # Check if the transaction time is unusual
    transaction_time = transaction.get('time')
    if transaction_time:
        transaction_hour = datetime.strptime(transaction_time, '%H:%M').hour
        if transaction_hour in UNUSUAL_HOURS:
            print("Fraud detected: Unusual transaction time.")
            return True
    
    # If none of the conditions are met, the transaction is not fraudulent
    return False

# Example usage:
transaction1 = {
    'cvv': '123',
    'ip': '192.168.1.1',
    'amount': 200,
    'time': '14:30'  # 2:30 PM
}

transaction2 = {
    'cvv': '',
    'ip': '10.0.0.5',
    'amount': 15000,
    'time': '03:00'  # 3:00 AM
}

print(f"Transaction 1 is fraudulent: {is_fraud(transaction1)}")
print(f"Transaction 2 is fraudulent: {is_fraud(transaction2)}")
