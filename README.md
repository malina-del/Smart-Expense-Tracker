# Smart-Expense-Tracker


## About the Application:

This application is used to monitor someone's expenses for a month or even longer. The application automatically divides the amounts of money spent into certain categories and later into subcategories. At the end of the month, or even sooner, the user can view graphs and tables showing how much money they spend monthly.

## Features:

- The bank account extract is uploaded.
- The application reads the statement and extracts the transactions.
- The transactions are organized into categories and subcategories.
- A website is created where users can see a table showing the amounts spent.
- Another table and graphs are created to show what amounts were spent and on what.
- Later, the user can add categories.
## Application Screenshots:
1.This is the page after running the application and here you need to enter the parameters
<img width="1016" height="878" alt="screen1" src="https://github.com/user-attachments/assets/2716c72d-108f-457e-bd3f-53e2f0d818eb" />
<img width="863" height="897" alt="screen2" src="https://github.com/user-attachments/assets/0073ef13-f16f-42a5-b842-da340bc753ae" />
2.This is the application after parameters
<img width="931" height="897" alt="screen3" src="https://github.com/user-attachments/assets/464a4d60-a5a4-447d-8f12-30f6f6175eb5" />
<img width="937" height="887" alt="screen4" src="https://github.com/user-attachments/assets/291750b2-818f-47ad-b599-0a698123354b" />

## Applications Used:

- Python
- Pandas
- Plotly
- Streamlit

## Installation and Usage:
1. The main structure is copied to obtain the data.
2. The necessary libraries are installed for the actual design of the website, using the following command: `python -m pip install -r requirements.txt`
3. The code is executed directly using `python -m streamlit run try2.py`.
4. A web page will open where the user has to upload a CSV file downloaded from their bank's mobile application.
5. The data will be extracted and read from the CSV file, and the transactions will be displayed in a table.
6. The data will subsequently be sorted by category and displayed in tables and graphs.
7. If the user does not have a suitable category or needs other categories, they can automatically add another category for easier and more efficient expense tracking.
8. At the end, the user can also see how much they spent last month and compare the amounts.
9. The user can also set a spending limit for each category and will receive a warning if the respective amount is exceeded.

## Data:
The CSV file is obtained directly from the bank's mobile application.
## How It Works:

1. The user uploads a CSV file containing bank transactions.
2. The application reads and processes the transaction data.
3. Each transaction is automatically assigned to a category based on its description.
4. The application calculates expenses for the selected period.
5. Tables and graphs display the expenses by category.
6. The user can set spending limits for different categories and receive warnings when a limit is exceeded.
## Future Improvements

- Allow users to manually change the categories assigned to transactions.
- Improve the automatic categorization of expenses.
- Add more detailed comparisons between monthly expenses.
- Save custom categories and budget limits between sessions.
- Add more charts and financial reports to help users better understand their spending habits.cum ti se pare?
