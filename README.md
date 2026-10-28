# Smart-Expense-Tracker


## About the Application:

This application is used to monitor someone's expenses for a month or even longer. The application automatically divides the amounts of money spent into certain categories and later into subcategories. At the end of the month, or even sooner, the user can view graphs and tables showing how much money they spend monthly.

## Features:

- The bank account extract is uploaded.
- The application reads the statement and extracts the transactions
- The transactions are organized into categories and subcategories
- A website is created where users can see a table showing the amounts spent
- Another table and graphs are created to show what amounts were spent and on what
- Later, the user can add categories
## Application Screenshots:
1.This is the page after running the application and here you need to enter the parameters
<img width="1016" height="878" alt="screen1" src="https://github.com/user-attachments/assets/2716c72d-108f-457e-bd3f-53e2f0d818eb" />
<img width="863" height="897" alt="screen2" src="https://github.com/user-attachments/assets/0073ef13-f16f-42a5-b842-da340bc753ae" />
2.This is the application after parameters
<img width="931" height="897" alt="screen3" src="https://github.com/user-attachments/assets/464a4d60-a5a4-447d-8f12-30f6f6175eb5" />
<img width="795" height="562" alt="image" src="https://github.com/user-attachments/assets/a57c9ac0-ab92-4921-b693-43248949ed3c" />

<img width="937" height="887" alt="screen4" src="https://github.com/user-attachments/assets/291750b2-818f-47ad-b599-0a698123354b" />

## Applications Used:

- Python
- Pandas
- Plotly
- Streamlit

## Installation and Usage:
 ## Installation

1. Clone or download the project repository from GitHub

2. Make sure Python is installed on your computer

3. Open a terminal in the project folder

4. Install the required libraries using the following command:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running the Application

5. Start the application by running:

   ```bash
   python -m streamlit run try2.py
   ```

6. Open the local URL provided by Streamlit in your web browser

7. Set monthly spending limits for the available expense categories. Enter `0` if you do not want to set a limit

8. Upload a CSV file exported from your bank's mobile application. The file must contain the columns `Data`, `Suma`, and `Descriere`

9. View the uploaded transactions in a table. The application automatically assigns categories based on keywords found in transaction descriptions

10. Explore the charts displaying monthly expenses by category and the table showing the allocated budget, amount spent, and remaining budget

11. Review the budget notifications. The application displays a warning when spending reaches at least 80% of a budget and an alert when the budget is exceeded

12. Add custom expense categories using the **Personalizeaza categoriile** section

# Notes:
13.The application analyzes expenses from the current calendar month.
14.Negative transaction amounts are treated as expenses, while positive amounts are excluded from expense calculations
15.A budget limit of 0 means that no spending limit is set for that category
16.Custom categories and budget settings are stored in the current Streamlit session and are not permanently saved between sessions


## Data:
The application requires a CSV file containing bank transaction data. The file must include the following columns:
Data-the date when the transaction occurred
Sum-the transaction amount. Negative values represent expenses, while positive values represent incoming money
Description-a description of the transaction, usually containing the name of the merchant or service provider
## How It Works:

1. The user uploads a CSV file containing bank transactions
2. The application reads and processes the transaction data
3. Each transaction is automatically assigned to a category based on its description
4. The application calculates expenses for the selected period
5. Tables and graphs display the expenses by category
6. The user can set spending limits for different categories and receive warnings when a limit is exceeded
## Future Improvements

- Improve the automatic categorization of expenses
- Add more detailed comparisons between monthly expenses
- Save custom categories and budget limits between sessions
- Add more charts and financial reports to help users better understand their spending habits
