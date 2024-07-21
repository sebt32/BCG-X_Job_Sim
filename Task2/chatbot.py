import pandas as pd

# Load the data from Task 1
data_report_path = 'data_report.csv'
summary_report_path = 'summary_report.csv'

data_report = pd.read_csv(data_report_path)
summary_report = pd.read_csv(summary_report_path)

def simple_chatbot(company_input, fiscal_year):
    print("\nPlease enter your query")
    user_query = input()

    if user_query == "What is the total revenue?":
        revenue = data_report[(data_report['Year'] == fiscal_year) & (data_report['Company'].str.lower() == company_input.lower())]['Total Revenue'].sum()
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
    elif user_query == "What is the Net Income?":
        net_income = data_report[(data_report['Year'] == fiscal_year) & (data_report['Company'].str.lower() == company_input.lower())]['Net Income'].sum()
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
    
    elif user_query == "What is the cash flow from operations growth(%)?":
        cash_flow_growth = summary_report[summary_report['Company'].str.lower() == company_input.lower()]['Cash Flow from Operations Growth(%)'].mean()
        return f"The Cash Flow from Operations Growth(%) for {company_input} is {cash_flow_growth:.2f}%"
    
    elif user_query == "What is the year by year average assets growth rate(%)?":
        avg_assets_growth = summary_report[summary_report['Company'].str.lower() == company_input.lower()]['Assets Growth (%)'].mean()
        return f"The Year by Year Average Assets Growth Rate(%) for {company_input} is {avg_assets_growth:.2f}%"
    
    elif user_query == "What is the year by year average liabilities growth rate(%)?":
        avg_liabilities_growth = summary_report[summary_report['Company'].str.lower() == company_input.lower()]['Liabilities Growth (%)'].mean()
        return f"The Year by Year Average Liabilities Growth Rate(%) for {company_input} is {avg_liabilities_growth:.2f}%"
    
    else:
        return "Sorry, I can only provide information on the requested queries."

# Chatbot session
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter 'Hi' to start the chatbot session; type 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHello! Welcome to the Financial Chatbot.")
        print("\nI can help you with your financial queries.")
        print("Please select the company name from below: -")
        print("\n1. Microsoft \n2. Tesla \n3. Apple")
        company_input = input("Enter company name: ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter the correct company name by starting the chatbot session again.")
            break
        else:
            print("\nThe data for the fiscal years 2023, 2022, and 2021 is currently available.")
            fiscal_year = int(input("Enter the fiscal year for the selected company: "))
            if fiscal_year not in [2023, 2022, 2021]:
                print("Please enter a valid fiscal year by starting the chatbot session again.")
                break
    else:
        print("Enter 'Hi' properly by starting the chatbot session again.")
        break

    response = simple_chatbot(company_input, fiscal_year)
    print(response)
