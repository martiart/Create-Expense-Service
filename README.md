# Create-Expense-Service

This microservice allows you to manage expenses by creating new entries stored in a JSON file. The communication between the client and the microservice occurs through JSON files for requests and responses. \

# Communication Contract
## Request Format:
To create a new expense, a request JSON file named 'request.json' should be formatted as shown below: 
'''json
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
'''
