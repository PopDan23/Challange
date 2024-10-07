#This will be my Python project start 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Step 1: Read the list of websites from the parquet file
parquet_file_path = "C:\Proiecte JS\Challange\list of company websites.snappy.parquet"
data = pd.read_parquet(parquet_file_path)
websites = data['website_column_name']  # Replace with actual column name

# Step 2: Function to scrape website content
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to access {url}")
            return None
    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return None

# Step 3: Function to extract addresses from website content using regex
def extract_address(html_content):
    # Regular expressions for matching different components of an address
    country_regex = r"(United States|Canada|United Kingdom|...)"
    city_regex = r"[A-Z][a-z]+(?:[\s-][A-Z][a-z]+)*"  # Simple pattern for city names
    postcode_regex = r"\b[0-9]{5}(?:-[0-9]{4})?\b"   # US ZIP code pattern
    road_regex = r"[0-9]+ [A-Za-z ]+(Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln)"  # Pattern for road
    
    # Compiled regex for performance
    country = re.search(country_regex, html_content)
    city = re.search(city_regex, html_content)
    postcode = re.search(postcode_regex, html_content)
    road = re.search(road_regex, html_content)
    
    # Placeholder for region (depends on more complex region-specific extraction)
    region = "Unknown"
    
    if country and city and postcode and road:
        return {
            "country": country.group(0),
            "region": region,
            "city": city.group(0),
            "postcode": postcode.group(0),
            "road": road.group(0),
            "road_number": re.search(r"\d+", road.group(0)).group(0)  # Extract road number
        }
    return None

# Step 4: Process each website and extract addresses
extracted_addresses = []
for website in websites:
    html_content = scrape_website(website)
    if html_content:
        address = extract_address(html_content)
        if address:
            extracted_addresses.append(address)

# Step 5: Output the extracted addresses
for address in extracted_addresses:
    print(address)

