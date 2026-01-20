import pandas as pd
import numpy as np

# Load Data
df = pd.read_excel("data/raw/bank_loan_data.xlsx")

# Basic Cleaning
df.columns = df.columns.str.lower().str.replace(" ", "_")
df['issue_date'] = pd.to_datetime(df['issue_date'])

# KPIs
total_applications = df.shape[0]
total_funded = df['loan_amount'].sum()
total_received = df['total_payment'].sum()
avg_interest = df['interest_rate'].mean()
avg_dti = df['dti'].mean()

# Good vs Bad Loans
good_loans = df[df['loan_status'].isin(['Fully Paid', 'Current'])]
bad_loans = df[df['loan_status'] == 'Charged Off']

good_loan_pct = len(good_loans) / total_applications * 100
bad_loan_pct = len(bad_loans) / total_applications * 100

# Monthly Trends
monthly_trend = df.groupby(df['issue_date'].dt.to_period('M')).agg({
    'loan_amount': 'sum',
    'total_payment': 'sum',
    'loan_status': 'count'
}).reset_index()

print("Total Applications:", total_applications)
print("Good Loan %:", round(good_loan_pct, 2))
print("Bad Loan %:", round(bad_loan_pct, 2))
