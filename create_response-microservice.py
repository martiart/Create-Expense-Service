import json
import time

# file to store expenses
EXPENSE_FILE = 'expenses.json'
REQUEST_FILE = 'request.json'
RESPONSE_FILE = 'response.json'


# helper function to read expenses from JSON file
def read_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)  # load + return expense file
    except FileNotFoundError:
        return []


# helper function to write expenses to JSON file
def write_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)  # save expense file


# create expense function
def create_expense(expense):
    expenses = read_expenses()
    expenses.append(expense)
    write_expenses(expenses)
    return {"status": "success", "expenses": expenses}


# main service runner function
def run_service():

    # messages to user notifying status
    print("Service is running. Press Ctrl+C to stop.")
    print("Waiting for request...")

    # process request
    while True:
        try:
            time.sleep(1)
            with open(REQUEST_FILE, 'r') as file:
                requests = json.load(file)
            if requests:
                print(f"Requests received: \n {requests}----------")

                for request in requests:
                    action = request.get('action')
                    expense = request.get('expense')
                    if action == 'create':
                        result = create_expense(expense)
                    else:
                        result = {"status": "error", "message": "Invalid action"}

                    print(f"Sending response: \n{result}----------")

                    with open(RESPONSE_FILE, 'w') as file:
                        json.dump(result, file, indent=4)
                # write to request file
                with open(REQUEST_FILE, 'w') as file:
                    json.dump([], file, indent=4)

                # clear request file
                with open(REQUEST_FILE, 'w') as file:
                    json.dump([], file, indent=4)
        except FileNotFoundError:
            print("Request file not found.")
        except KeyboardInterrupt:
            print("\nService stopped by user.")
            break  # exit loop


if __name__ == "__main__":
    run_service()

