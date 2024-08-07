# Create-Expense-Service

This microservice allows you to manage expenses by creating new entries stored in a JSON file. The communication between the client and the microservice occurs through JSON files for requests and responses.

# Communication Contract
## Request Format:
To create a new expense, a request JSON file named 'request.json' should be formatted as shown below: 
 ```json
  [
  {
    "action": "create",
    "expense": {
      "id": 1,
      "amount": 100.0,
      "description": "Groceries"
    }
  }
]
```
## Response Format:
 ```json
{
  "status": "success",
  "expenses": [
    {
      "id": 1,
      "amount": 100.0,
      "description": "Groceries"
    }
  ]
}

```
## How to request Data:
```python
import json

def send_request(expense):
    request_data = {
        "action": "create",
        "expense": expense
    }
    with open('request.json', 'w') as file:
        json.dump([request_data], file, indent=4)
    print("Request sent.")

# Example of creating a new expense
new_expense = {
    "id": 1,
    "amount": 100.0,
    "description": "Groceries"
}
send_request(new_expense)
```

# How to recieve data:
```python
import json

def get_response():
    try:
        with open('response.json', 'r') as file:
            response = json.load(file)
            return response
    except FileNotFoundError:
        print("Response file not found.")
        return None

# Example of retrieving the response
response = get_response()
if response:
    print("Response received:")
    print(response)

```
