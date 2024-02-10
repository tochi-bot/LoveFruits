
import gspread
from google.oauth2 import service_account

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

import gspread

try:
    # Access the "Sales" worksheet within the "LoveFruits" spreadsheet
    sales = SHEET.worksheet("Sales")
except gspread.exceptions.WorksheetNotFound:
    print("Worksheet named 'Sales' not found in the 'LoveFruits' spreadsheet.")
    # Handle the error gracefully, such as creating the worksheet or notifying the user.


def get_sales_info():
    """ 
    Get sales information from the user
    """
    # Prompt the user to enter sales information for the last market
    print("Please enter sales information for the last market")
    # Provide instructions for entering data
    print("Data should be six numbers, separated by comma")
    print("Example: 40,50,10,40,60,70\n")
    # Receive input from the user
    data_string = input("Enter your data here: ")
    # Print the entered data string
    print(data_string)

# Call the get_sales_info function to prompt the user for input
get_sales_info()

