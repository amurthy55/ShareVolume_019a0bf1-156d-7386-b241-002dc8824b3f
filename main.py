import requests
import json

# Fetch data from SEC
url = 'https://data.sec.gov/api/xbrl/companyconcept/CIK0001086222/dei/EntityCommonStockSharesOutstanding.json'
headers = {'User-Agent': 'Akamai Technologies Data Fetcher'}
response = requests.get(url, headers=headers)
data = response.json()

# Extract entity name
entity_name = data['entityName']

# Filter shares data
shares = data['units']['shares']
filtered_shares = [share for share in shares if share['fy'] > '2020' and isinstance(share['val'], (int, float))]

# Calculate max and min
max_share = max(filtered_shares, key=lambda x: x['val'])
min_share = min(filtered_shares, key=lambda x: x['val'])

# Prepare data for output
output_data = {
    'entityName': entity_name,
    'max': {'val': max_share['val'], 'fy': max_share['fy']},
    'min': {'val': min_share['val'], 'fy': min_share['fy']}
}

# Save to data.json
with open('data.json', 'w') as f:
    json.dump(output_data, f)
