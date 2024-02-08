# Import the gspread library, which allows interaction with Google Sheets
import gspread
# Import the service_account module from the google.oauth2 library, which provides credentials for accessing Google APIs using service accounts
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

# Access the worksheet named "sales" within the opened Google Sheet and assign it to the sales variable
sales = SHEET.worksheet("sales")

# Retrieve all values from the "sales" worksheet and assign them to the data variable
data = sales.get_all_values()

# Print the retrieved data from the "sales" worksheet
print(data)



import openpyxl  # Import the openpyxl library for working with Excel spreadsheets
import os.path   # Import os.path module for filesystem path operations