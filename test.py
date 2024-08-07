# import json
# import time
#
# # file paths for request, response, and expense data
# REQUEST_FILE = 'request.json'
# RESPONSE_FILE = 'response.json'
# EXPENSE_FILE = 'expenses.json'
#
# def get_next_id(expenses):
#     """get next available id for a new expense."""
#     if expenses:
#         return max(expense['id'] for expense in expenses) + 1  # return next id based on existing expenses
#     return 1  # start with id 1 if there are no expenses
#
# def send_request(action, expense):
#     """function to send a request to the microservice."""
#     request_data = {
#         "action": action,
#         "expense": expense
#     }
#     with open(REQUEST_FILE, 'w') as file:
#         json.dump([request_data], file, indent=4)  # write request data to the request file
#     print(f"request sent: {request_data}")  # notify that the request has been sent
#
# def get_response():
#     """function to read the response from the microservice."""
#     try:
#         with open(RESPONSE_FILE, 'r') as file:
#             response = json.load(file)  # load response data from the response file
#             return response
#     except FileNotFoundError:
#         print("response file not found...")  # notify if the response file is missing
#         return None
#
# def main():
#     # load existing expenses from file, or initialize as an empty list if the file doesn't exist
#     try:
#         with open(EXPENSE_FILE, 'r') as file:
#             expenses = json.load(file)  # load existing expenses from the file
#     except FileNotFoundError:
#         expenses = []  # start with an empty list if no expenses file is found
#
#     while True:
#         # automatically assign the next available id
#         expense_id = get_next_id(expenses)
#
#         # get user expense details
#         amount = float(input("enter amount: "))  # prompt user for the expense amount
#         description = input("enter description: ")  # prompt user for a description of the expense
#
#         # define new expense based on user input
#         new_expense = {
#             "id": expense_id,  # use the auto-assigned id
#             "amount": amount,
#             "description": description
#         }
#
#         # send request to create the new expense
#         send_request('create', new_expense)
#
#         # wait a moment to allow the microservice to process the request
#         time.sleep(2)
#
#         # retrieve response from the microservice
#         response = get_response()
#         if response:
#             print("response received:")
#             print(json.dumps(response, indent=4))  # print the response in a readable format
#
#         # update existing expenses list with the newly added expense
#         expenses.append(new_expense)
#
#         # ask if the user wants to add another expense
#         continue_adding = input("do you want to add another expense? (yes/no): ").strip().lower()
#         if continue_adding != 'yes':
#             break  # exit the loop if the user does not want to add more expenses
#
#     # save updated expenses to file when the user exits the program
#     with open(EXPENSE_FILE, 'w') as file:
#         json.dump(expenses, file, indent=4)  # write updated expenses back to the file
#         print("updated expenses saved to file.")
#
#
# if __name__ == '__main__':
#     main()  # run the main function to start the program
import json
import time

# file paths for request, response, and expense data
REQUEST_FILE = 'request.json'
RESPONSE_FILE = 'response.json'
EXPENSE_FILE = 'expenses.json'

def get_next_id(expenses):
    """Get the next available ID for a new expense."""
    if expenses:
        return max(expense['id'] for expense in expenses) + 1  # return next id based on existing expenses
    return 1  # start with id 1 if there are no expenses

def send_request(action, expense):
    """Function to send a request to the microservice."""
    request_data = {
        "action": action,
        "expense": expense
    }
    with open(REQUEST_FILE, 'w') as file:
        json.dump([request_data], file, indent=4)  # write request data to the request file
    print(f"Request sent: {request_data}")  # notify that the request has been sent

def get_response():
    """Function to read the response from the microservice."""
    try:
        with open(RESPONSE_FILE, 'r') as file:
            response = json.load(file)  # load response data from the response file
            return response
    except FileNotFoundError:
        print("Response file not found...")  # notify if the response file is missing
        return None

def main():
    # Load existing expenses from file, or initialize as an empty list if the file doesn't exist
    try:
        with open(EXPENSE_FILE, 'r') as file:
            expenses = json.load(file)  # load existing expenses from the file
    except FileNotFoundError:
        expenses = []  # start with an empty list if no expenses file is found

    try:
        while True:
            # Automatically assign the next available ID
            expense_id = get_next_id(expenses)

            # Get user expense details
            amount = float(input("Enter amount: "))  # prompt user for the expense amount
            description = input("Enter description: ")  # prompt user for a description of the expense

            # Define new expense based on user input
            new_expense = {
                "id": expense_id,  # use the auto-assigned ID
                "amount": amount,
                "description": description
            }

            # Send request to create the new expense
            send_request('create', new_expense)

            # Wait a moment to allow the microservice to process the request
            time.sleep(2)

            # Retrieve response from the microservice
            response = get_response()
            if response:
                print("Response received:")
                print(json.dumps(response, indent=4))  # print the response in a readable format

            # Update existing expenses list with the newly added expense
            expenses.append(new_expense)

            # Ask if the user wants to add another expense
            continue_adding = input("Do you want to add another expense? (yes/no): ").strip().lower()
            if continue_adding != 'yes':
                break  # exit the loop if the user does not want to add more expenses

    except KeyboardInterrupt:
        print("\n \nService stopped by user.")  # Notify user when service is stopped
    finally:
        # Save updated expenses to file when the user exits the program
        with open(EXPENSE_FILE, 'w') as file:
            json.dump(expenses, file, indent=4)  # write updated expenses back to the file
            print("Updated expenses saved to file.")

if __name__ == '__main__':
    main()  # run the main function to start the program
