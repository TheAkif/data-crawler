import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Load business information from Excel sheet
excel_file = 'business_data.xlsx'
df = pd.read_excel(excel_file)

# Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['BusinessName', 'Address', 'City', 'State', 'ZipCode', 'Email', 'OwnerName'])

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    business_name = row['BusinessName']
    address = row['Address']
    city = row['City']
    state = row['State']
    zip_code = row['ZipCode']

    # Construct the search query to find the website for the business
    search_query = f"{business_name} {address} {city} {state} {zip_code}"

    # Search on Google
    google_url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(google_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract website URLs from the search results
    website_urls = []
    search_results = soup.find_all('div', class_='r')  # Adjust based on the structure of Google search results
    for result in search_results:
        website_url = result.find('a')['href']
        if 'google' not in website_url:  # Exclude Google search result links
            website_urls.append(website_url)

    # Extract email and owner name from the website
    email = 'N/A'
    owner_name = 'N/A'
    for website_url in website_urls:
        try:
            website_response = requests.get(website_url)
            website_soup = BeautifulSoup(website_response.content, 'html.parser')

            # Extract email element from the website
            email_element = website_soup.find('a', href=re.compile(r'^mailto:'))
            if email_element:
                email = email_element['href'][7:]  # Remove 'mailto:' prefix
                break

            # Extract owner name element from the website
            owner_name_element = website_soup.find('div', class_='owner-name')
            if owner_name_element:
                owner_name = owner_name_element.text.strip()

        except requests.exceptions.RequestException:
            continue

    # Create a temporary DataFrame for the current business
    temp_df = pd.DataFrame({
        'BusinessName': [business_name],
        'Address': [address],
        'City': [city],
        'State': [state],
        'ZipCode': [zip_code],
        'Email': [email],
        'OwnerName': [owner_name]
    })

    # Concatenate the temporary DataFrame with the results DataFrame
    results_df = pd.concat([results_df, temp_df], ignore_index=True)

# Export the data to a CSV file
results_df.to_csv('business_results.csv', index=False)

# Print the results
print(results_df)
