import json
import requests
from tabulate import tabulate

# Read wallet addresses from a file (wallets.txt)
with open("wallets.txt", "r") as file:
    wallet_addresses = file.read().splitlines()

# Load the JSON data from the URL
url = "https://raw.githubusercontent.com/celestiaorg/networks/master/celestia/pre-genesis.json"
response = requests.get(url)
data = response.json()

# Extract balances for each wallet address
balances = []
total_balance = 0

for address in wallet_addresses:
    found = [item for item in data["app_state"]["bank"]["balances"] if item["address"] == address]
    if found:
        balance = found[0]["coins"][0]
        balance_str = int(balance['amount']) // 1000000
        total_balance += balance_str
        balances.append([address, balance_str])

# Add a summary line with the total balance
summary_line = ["Total $TIA", total_balance]
balances.append(summary_line)

# Define the table headers
headers = ["Address", "Balance in $TIA"]

# Print the results as a table with outlined and bold headers
table = tabulate(balances, headers, tablefmt="grid")
print(table)
