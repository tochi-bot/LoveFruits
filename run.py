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

def get_sales_info():
    """ 
    Get sales information from the user
    """
    while True:
        # Prompt the user to enter sales information for the last market
        print("Please enter sales information for the last market\n")
        print("Enter sales numbers for the following fruits\n")
        print(" Banana, Orange, Water Melon, Apple, Pear, Carrots\n")
        # Provide instructions for entering data
        print("Options:")
        print("1. Calculate average stock data:  press AVG")
        print("2. Calculate total stock data:  press TOT")
        print("3. Calculate median stock data: press MED\n")
        print("Please note that Data should be six numbers, separated by comma\n")
        print("Example: 40,50,10,40,60,70\n")
        # Receive input from the user
        data_choices = input("Enter your data choice: ").strip().upper()

        if data_choices not in ["AVG", "TOT", "MED"]:
            print("Invalid choice. Please enter either AVG, TOT, or MED.")
            continue

        data_string = input("Enter your sales data: ").strip()

        # Validate input format
        if data_string.count(',') != 5:
            print("Invalid input. Please enter six numbers separated by commas.")
            continue
        try:
            # Convert data to a string before returning
            data = data_choices, data_string
            print("Validating your data!")
            return data
        except ValueError:
            print("Invalid input. Please enter numeric values only.")


def calculate_data(data):
    """
    Calculate the selected data based on the user's choice.
    Parameters:
    data (tuple): Tuple containing the user's choice and sales data.
    """
    choice, sales_data = data
    sales_data = list(map(int, sales_data.split(',')))
    
    if choice == "AVG":
        average = sum(sales_data) / len(sales_data)
        print(f"Average stock data: {average}")
    elif choice == "TOT":
        total = sum(sales_data)
        print(f"Total stock data: {total}")
    elif choice == "MED":
        sorted_sales = sorted(sales_data)
        if len(sorted_sales) % 2 == 0:
            median = (sorted_sales[len(sorted_sales)//2 - 1] + sorted_sales[len(sorted_sales)//2]) / 2
        else:
            median = sorted_sales[len(sorted_sales)//2]
        print(f"Median stock data: {median}")


def main():
    """
    Run all program functions.
    """
    data = get_sales_info()
    calculate_data(data)

print("Welcome to Love Fruits Automation System")
print("Your comprehensive solution for efficient fruit market management")
main()
