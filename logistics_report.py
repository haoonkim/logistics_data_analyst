import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Connect to PostgreSQL
engine = create_engine("postgresql://haoonkim:1234@localhost:5432/postgres")

# Load data from the logistics table
df = pd.read_sql("SELECT * FROM logistics", engine)

# Convert move_date column to datetime
df["move_date"] = pd.to_datetime(df["move_date"])

# Analyze total quantity by item
item_summary = df.groupby("item_name")["quantity"].sum().sort_values(ascending=False)
print("Total quantity by item:\n", item_summary)

# Analyze total quantity by from_base
from_summary = df.groupby("from_base")["quantity"].sum()
print("\nTotal quantity by from_base:\n", from_summary)

# Analyze daily moved quantity
daily_summary = df.groupby("move_date")["quantity"].sum()
print("\nDaily moved quantity:\n", daily_summary)

# Plot: Total quantity by item
plt.figure(figsize=(8, 5))
item_summary.plot(kind="bar", title="Total Quantity by Item")
plt.xlabel("Item Name")
plt.ylabel("Total Quantity")
plt.tight_layout()
plt.show()

# Plot: Daily moved quantity
plt.figure(figsize=(8, 5))
daily_summary.plot(kind="line", marker="o", title="Daily Moved Quantity")
plt.xlabel("Move Date")
plt.ylabel("Quantity")
plt.grid(True)
plt.tight_layout()
plt.show()

# Extract summary values
total_quantity = df["quantity"].sum()
most_moved_item = item_summary.idxmax()
most_moved_item_qty = item_summary.max()
top_from_base = from_summary.idxmax()
top_from_base_qty = from_summary.max()
start_date = df["move_date"].min().strftime("%Y-%m-%d")
end_date = df["move_date"].max().strftime("%Y-%m-%d")

# Construct prompt
prompt = f"""
You are a logistics analyst. Write a short summary report based on the following data:

- Period: {start_date} to {end_date}
- Total moved quantity: {total_quantity}
- Most moved item: {most_moved_item} ({most_moved_item_qty} units)
- Most active origin base: {top_from_base} ({top_from_base_qty} units)

Write in a clear and professional tone, 3–4 sentences.
"""

# Call OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Print the generated report
report_text = response.choices[0].message["content"]
print("\n=== Generated Logistics Summary Report ===\n")
print(report_text)
