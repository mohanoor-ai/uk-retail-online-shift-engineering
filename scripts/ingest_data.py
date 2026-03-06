import os
import requests

# What: Downloading the ONS Feb 2026 Retail Data
# Why: Initial data source for our pipeline
DATA_URL = "https://www.ons.gov.uk/generator?format=csv&uri=/businessindustryandtrade/retailindustry/datasets/retailsalesindexreferencetables/current"
OUTPUT_PATH = "data/raw_retail_sales.csv"

def download_data():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    print(f"Downloading data from ONS...")
    response = requests.get(DATA_URL)
    
    with open(OUTPUT_PATH, 'wb') as f:
        f.write(response.content)
    print(f"Done! Data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    download_data()