"""
Srcaping the list of English Monarchs from this wiki page

https://en.wikipedia.org/wiki/List_of_English_monarchs
"""

import re
from bs4 import BeautifulSoup

file_path = "en.wikipedia.org_wiki_List_of_English_monarchs.html"

with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html5lib')

# List to store monarch details
monarchs = []

# Helper function to extract the first valid year
def extract_year_from_html(html_element):
    if html_element is None:
        return None
    # Extract text content, handling <br> tags and other elements
    text = html_element.get_text(separator=" ", strip=True)
    match = re.search(r'\b\d{3,4}\b', text)  # Match a 3- or 4-digit year
    return match.group() if match else None

# Locate all the tables with class 'wikitable'
tables = soup.find_all('table', class_='wikitable')

# Iterate through each table
for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        num_cols = len(cols)  # Count the number of <td> elements
        if num_cols >= 6:  # Ensure sufficient columns for data extraction
            try:
                # Extract monarch name using `.wikitable td b a`
                name_tag = cols[0].select_one('b a')  # Use CSS selector for accuracy
                name = name_tag.get_text(strip=True) if name_tag else None

                # Determine column indices for birth and death years
                if num_cols == 6:
                    birth_col = 2
                    death_col = 4
                elif num_cols == 7:
                    birth_col = 3
                    death_col = 5
                else:
                    continue  # Skip rows with unexpected column counts

                # Extract birth and death years
                birth_year = extract_year_from_html(cols[birth_col])
                death_year = extract_year_from_html(cols[death_col])

                # Append to the list if name and at least one year exist
                if name and (birth_year or death_year):
                    monarchs.append({
                        'Name': name,
                        'Birth Year': birth_year,
                        'Death Year': death_year
                    })
            except Exception as e:
                print(f"Error processing row: {row}\nError: {e}")

# Print the results in a clean tabular format
print(f"{'Name':<40}{'Birth Year':<15}{'Death Year':<15}")
print("=" * 70)
for monarch in monarchs:
    name = monarch['Name']
    birth_year = monarch['Birth Year'] if monarch['Birth Year'] else ''
    death_year = monarch['Death Year'] if monarch['Death Year'] else ''
    print(f"{name:<30}{birth_year:<15}{death_year:<15}")
    