**README: Love Fruits Automation System**

**Introduction:**

Welcome to the Love Fruits Automation System! This project aims to simplify the process of managing fruit market data through automation.
This system was designed to streamline the user tasks effectively.

**Aims:**

1. **Efficiency:** Reduce the time and effort required for data entry and calculation tasks.
2. **Accuracy:** Ensure precise calculations and data management, minimizing errors.
3. **Convenience:** Provide a user-friendly interface for seamless interaction and operation.

**How to Use:**

1. **Set Up Google Sheets:** Ensure you have access to Google Sheets and have a spreadsheet named "LoveFruits" created.
2. **Install Dependencies:** Make sure you have the required dependencies installed, including `gspread` and `google.oauth2`.
3. **Provide Credentials:** Prepare your Google service account credentials in a JSON file named "creds.json" to enable access to Google Sheets.
4. **Run the Code:** Execute the provided Python script to launch the Love Fruits Automation System.
5. **Enter Data:** Follow the prompts to enter sales information for the last market, specifying sales numbers for various fruits.
6. **Choose Calculation:** Select the desired calculation option (AVG, TOT, MED, SALES, or SURPLUS) to compute the average, total, or median stock data, respectively.
7. **Review Results:** View the calculated stock data provided by the system for your analysis and decision-making.

![REsponsive image](https://github.com/tochi-bot/LoveFruits/assets/77632001/84bc0890-2644-4cbf-8310-f17a6ecf7610)

### User Story
**As a fruit market manager, I want to automate the process of calculating stock data to streamline my tasks and ensure accurate results.
---

### Features

#### Introductory Message and Sales Input

![welcome message](https://github.com/tochi-bot/LoveFruits/assets/77632001/aa18d68b-6863-4abf-84f9-caa9bdc067c9)

When you start the system, you'll receive a warm welcome and initial instructions. To begin, enter the sales information for your most recent market. The user-friendly interface will lead you step by step, ensuring precise data entry for each fruit type. Remember to separate each value with a comma, without any spaces or pound signs. An example of the correct data entry format is provided for your convenience.

#### User Entry Choices

![Welcome message ](https://github.com/tochi-bot/LoveFruits/assets/77632001/2e7fc3ed-5c43-4ec4-9dbf-62786f23bdce)

### User AVG Choice And Result

![AVG](https://github.com/tochi-bot/LoveFruits/assets/77632001/472f759e-34e1-4eba-ac01-6d4a62be50ef)

### User TOT Choice And Result
![Total stock data](https://github.com/tochi-bot/LoveFruits/assets/77632001/d9171300-16b7-4d9e-a79d-26d0cfc218dd)

### User MED Choice And Result

![MED data](https://github.com/tochi-bot/LoveFruits/assets/77632001/162c3d6d-32ab-4bb5-95a2-debf05a4d2a3)

### User Sale Worksheet Updated
![sales data update](https://github.com/tochi-bot/LoveFruits/assets/77632001/624c62b6-7d5f-4f7d-bbeb-35dbf6765e11)

### User Surplus Worksheet Updated

![surplus data update](https://github.com/tochi-bot/LoveFruits/assets/77632001/2442b083-f491-45ce-a4f0-f38509e7cfef)

### Invalid User Choices Input

![Invalid choice](https://github.com/tochi-bot/LoveFruits/assets/77632001/3507c26e-b6f5-4cfe-9539-946c0bf7d94f)
### Invalid User Entry

![Invalid user input](https://github.com/tochi-bot/LoveFruits/assets/77632001/274b1840-b11e-465a-8fca-7ed2b5652cab)


#### LoveFruits Google Worksheet View

Access the latest data on the Google worksheet through the provided link below. Please copy the link and paste it into a new browser tab for access. link: [LoveFruits Google Worksheet](https://docs.google.com/spreadsheets/d/12xkqAzLckljm4qPQOqNDR8n_upgWap9Tfdel-j76Pq0/edit?usp=drive_link). 

The Google worksheet was set to read-only for users without editing permissions. Only the NDoS team and senior management have the necessary access to modify the file. This precautionary measure is implemented to minimize the risk of inadvertent changes being made to the worksheet.

#### Flowchart

![FLowchart](https://github.com/tochi-bot/LoveFruits/assets/77632001/761f2c26-2215-4405-a49d-a0835fbe6da3)


This flowchart represents the sequential execution of the main function. Each block represents a function call, and arrows indicate the flow of data and control from one step to another. The decision points are minimal in this particular code, so the flow is mostly linear.

---
# Testing

To ensure the robustness of the interface and the system's ability to handle incorrect user input, comprehensive testing was conducted to cover all possible scenarios.

## View tests conducted:

- **Validator Testing:** The code was passed through PEP8, and no errors were found, ensuring compliance with Python coding standards.

- **Browser Compatibility Testing:** Heroku was tested across multiple browsers including Google Chrome, Safari, Microsoft Edge, and Mozilla Firefox. The application functioned correctly as intended on all tested browsers.

- **Mobile Device Testing:** The Heroku program was tested on various mobile devices including iPhone 11, Google Pixel 2, Motorola Edge, and Huawei P9 to ensure responsiveness and functionality across different screen sizes and resolutions.

## Note on User Experience:

For the optimal user experience, I recommended running the program on a tablet, laptop, or desktop. While the program is functional on mobile devices, the smaller screen size may make it challenging to read instructions and recommendations effectively.
### Project Bugs and Solutions

1. **Input Data Validation**
   - **Bug:** Currently, the system accepts any input from the user as valid, even if it doesn't adhere to the expected format.
   - **Solution:** Implemented input validation to ensure that the entered sales data follows the specified format of six numbers separated by commas.
   
2. **Error Handling for Google Sheets Operations**
   - **Bug:** The system does not handle potential errors that may occur during interactions with Google Sheets, such as network errors or authentication issues.
   - **Solution:** Implemented try-except blocks to handle potential errors during interactions with Google Sheets and provide informative error messages to the user.

3. **Lack of Modularity**
   - **Bug:** The main function (main) contains all the logic for interacting with Google Sheets and performing calculations, resulting in a lack of modularity and reusability.
   - **Solution:** Refactor the code into smaller, modular functions with clearly defined responsibilities to enhance modularity and reusability.
### Deployment

 I outlined the necessary steps for deploying my application to Heroku. It's essential to note that Heroku serves as an excellent platform for managing and scaling back-end languages like Python. Deploying the work to Heroku will enable me to efficiently manage and scale our application as needed.

Here are the steps for Heroku deployment:

1. **Create a Heroku Account:** Sign up for a Heroku account at Heroku's website.
   
2. **Install Heroku CLI:** Download and install the Heroku Command Line Interface (CLI) on your local machine.
   
3. **Login to Heroku CLI:** Once installed, log in to Heroku CLI using the command `heroku login` in your terminal or command prompt. Follow the prompts to authenticate your Heroku account.
   
4. **Prepare your Application:** Ensure that your application is properly configured and includes a `requirements.txt` file listing all dependencies required for deployment.
   
5. **Create a Git Repository:** Initialize a Git repository in your project directory.
   
6. **Create a Heroku App:** Create a new Heroku app using the command `heroku create` in your terminal. This will generate a unique app name and a git remote (`heroku`) linked to your Heroku app.
   
7. **Deploy your Application:** Deploy your application to Heroku by pushing your code to the Heroku remote using Git.
   
8. **Configure Environment Variables:** Configure API keys and build packs in the Heroku dashboard.

Once you have completed these steps, your application should be successfully deployed to Heroku, and you can access it through the provided Heroku app link.
### Credits

#### Code
- Code Institute Love Sandwiches Walkthrough
- W3Schools Python Tutorial

#### Acknowledgments
- My mentor Rahul for his ongoing support and feedback
- The Code Institute’s Tutor Support
- The Slack community
- www.draw.io
- Am I Responsive Website
