import gspread
from google.oauth2 import service_account
from pprint import pprint

# Define the scopes required for accessing Google Sheets and Google Drive APIs
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",  # Scope for accessing Google Sheets
    "https://www.googleapis.com/auth/drive.file",    # Scope for accessing files created by the application
    "https://www.googleapis.com/auth/drive"          # Scope for accessing all files in Google Drive
]

# Load credentials from the service account JSON file ("creds.json") and create a credentials object
CREDS = service_account.Credentials.from_service_account_file("creds.json")

# Attach the defined scopes to the credentials object
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the gspread client using the scoped credentials, allowing interaction with Google Sheets
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet named "LoveFruits" using the authorized client and assign it to the SHEET variable
SHEET = GSPREAD_CLIENT.open("LoveFruits")

# Access the "sales" worksheet within the "LoveFruits" spreadsheet
sales = SHEET.worksheet("sales")

# Retrieve all values from the "sales" worksheet and assign them to the data variable
data = sales.get_all_values()

# Print the retrieved data
print(data)


def get_sales_info():
    """ 
    Get sales information from the user
    """
    while True:
        # Prompt the user to enter sales information for the last market
        print("Please enter sales information for the last market")
        # Provide instructions for entering data
        print("Data should be six numbers, separated by comma")
        print("Example: 40,50,10,40,60,70\n")
        # Receive input from the user
        data_string = input("Enter your data here: ")
        # Print the entered data string
        print(data_string)
        
        if data_string:
            print("Your data is valid!")
            # Return a list of integers obtained by splitting the input string
            return [int(value.strip()) for value in data_string.split(',')]


try:
    # Attempt to access the "Sales" worksheet within the "LoveFruits" spreadsheet
    sales = SHEET.worksheet("Sales")
except gspread.exceptions.WorksheetNotFound:
    # If the worksheet is not found, print a message notifying the user
    print("Worksheet named 'Sales' not found in the 'LoveFruits' spreadsheet.")
    # Handle the error gracefully, such as creating the worksheet or notifying the user.

try:
    # Call the get_sales_info function to prompt the user for input
    data = get_sales_info()
    # Check if the number of values entered is exactly 6
    if len(data) != 6:
        # If not, raise a ValueError with an appropriate message
        raise ValueError(f"Exactly 6 values are required, you provided {len(data)}")
except ValueError as e:
    # If a ValueError occurs (e.g., incorrect number of values entered), print an error message
    print(f"Invalid data: {e}, please try again\n")
    exit(1)


def sales_worksheet_update(data):
    """ 
    Update sales worksheet and add new row with list as provided
    """
    print("sales worksheet updating...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated successfully")

# Call the sales_worksheet_update function to update the sales worksheet with the provided data

def surplus_data_calculation(sales_row):
    """ 
   
    Compare sales with stock and calculate the surplus for each item type

    A positive surplus indicates waste, meaning we've sold fewer items than what we had in stock.
    Conversely, a negative surplus indicates extra revenue generated when stock was sold out, signifying high demand or efficient stock management.
    """
    print("Calculating surplus data...\n")
    stock=SHEET.worksheet("stock").get_all_values()
    stock_row=stock[-1]
    print(f"Stock row:{stock_row}")
    print(f"Sales row:{sales_row}")
    surplus_data=[]
    for stock, sales in zip (stock_row, sales_row):
        surplus=int(stock)-sales
        surplus_data.append(surplus)
    return surplus_data

def main():
    """

    Run all programms functions.  
    """
    data = get_sales_info()
    sales_worksheet_update(data)
    new_surplus_data= surplus_data_calculation(data)
    print(new_surplus_data)
print("Welcome to Love Fruits Automation")
main()