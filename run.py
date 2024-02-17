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
        print("Please enter sales information for the last market")
        print("Inputed fruits sold should start with Banana, Orange, Water Melon, Apple, Pear, Carrots")
        # Provide instructions for entering data
        print("Data should be six numbers, separated by comma")
        print("Example: 40,50,10,40,60,70\n")
        # Receive input from the user
        data_string = input("Enter your data here:\n ").strip()

        # Validate input format
        if data_string.count(',') != 5:
            print("Invalid input. Please enter six numbers separated by commas.")
            continue

        try:
            # Parse the input string into a list of integers
            data = [int(value.strip()) for value in data_string.split(',')]
            print("Validating your data!")
            return data
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

def sales_worksheet_update(data):
    """ 
    Update sales worksheet with provided data.
    Parameters:
    data (list): List containing sales data to be appended as a new row in the sales worksheet.
    """
    try:
        print("Sales worksheet updating...\n")
        sales_worksheet = SHEET.worksheet("sales")
        sales_worksheet.append_row(data)
        print("Sales worksheet updated successfully")
    except Exception as e:
        print(f"Error updating sales worksheet: {e}")


def surplus_worksheet_update(data):
    """
    Update surplus worksheet with provided data.
    Parameters:
    data (list): List containing surplus data to be appended as a new row in the surplus worksheet.
    """
    try:
        print("Surplus worksheet updating...\n")
        surplus_worksheet = SHEET.worksheet("surplus")
        surplus_worksheet.append_row(data)
        print("Surplus worksheet updated successfully")
    except Exception as e:
        print(f"Error updating surplus worksheet: {e}")


def worksheet_update(worksheet, data):
    """
    Accepts a list of integers for insertion into the worksheet and
    updates the corresponding worksheet with the provided data. 
    """
    try:
        print(f"Updating {worksheet} worksheet...\n")
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(data)
        print(f"{worksheet} worksheet updated successfully\n")
    except Exception as e:
        print(f"Error updating {worksheet} worksheet: {e}")

def surplus_data_calculation(sales_row):
    """ 
    Calculate surplus for each item type based on sales and stock data.
    Parameters:
    sales_row (list): List containing sales data for each item type.
    Returns:
    list: List containing calculated surplus for each item type.
    """
    try:
        print("Calculating surplus data...\n")
        stock = SHEET.worksheet("stock").get_all_values()
        # Extract the last row of stock data, 
        stock_row = stock[-1]
        surplus_data = []
        for stock_item, sales_item in zip(stock_row, sales_row):
            # Check if both stock_item and sales_item are convertible to integers
            if stock_item.isdigit() and isinstance(sales_item, int):
                surplus = int(stock_item) - sales_item
                surplus_data.append(surplus)
        return surplus_data
    except Exception as e:
        print(f"Error calculating surplus data: {e}")
        return None




def get_last_6_entries_sales():
    """
    Compute the columns of data from the sales worksheet, gathering the last six entries of LoveFruits, 
    and return the data as a list of lists.
    """
    try:
        sales_worksheet = SHEET.worksheet("sales")
        columns = []
        for add in range(1, 7):
            column = sales_worksheet.col_values(add)
            columns.append(column[-6:])
        return columns
    except Exception as e:
        print(f"Error retrieving last 6 entries of sales data: {e}")
        return None

def compute_stock_data(data):
    """ 
    Calculate the average stock for each item type, increasing it by 30%.
    """
    try:
        print("Computing average stock data...\n")
        new_stock_data = []
        for column in data:
            if column:
                int_column = [int(num) for num in column if num.isdigit()]  # Filter non-numeric values
                if int_column:  # Check if int_column is not empty
                    mean = sum(int_column) / len(int_column)
                    stock_num = mean * 1.3
                    new_stock_data.append(stock_num)
        return new_stock_data
    except Exception as e:
        print(f"Error computing average stock data: {e}") 
        return None


def main():
    """
    Run all program functions.
    """
    data = get_sales_info()
    sales_worksheet_update(data)
    surplus_worksheet_update(data)
    worksheet_update("sales", data) 
    sales_row = get_last_6_entries_sales()
    surplus_data = surplus_data_calculation(sales_row)
    compute_stock_data(surplus_data)

print("Welcome to Love Fruits Automation System, your comprehensive solution for efficient fruit market management")
main()
