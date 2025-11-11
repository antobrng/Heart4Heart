import requests
from bs4 import BeautifulSoup
import csv 
import os

URL = "https://www.zeffy.com/fr-CA/o/fundraising/campaigns/hub?formId=0174b806-86e9-470d-b61c-758c3db03c88&tab=payment"
HEADER = {}
SCRIPT_DIR = os.path.dirname(__file__)
OUPTUT_CSV = os.path.join(SCRIPT_DIR, "..", "data", "exec_names.csv")


def fetch_page(url):
    r = requests.get(url, headers=HEADER)
    r.raise_for_status()
    html = r.text

    with open("zeffy.html", "w", encoding="utf-8") as f:
        f.write(html)

    return html

def parse_names_in_html(html):
    soup = BeautifulSoup(html, "html.parser")
    
    names = []

    name = soup.select_one(".MuiSelect-select").get_text(strip=True)
    print(f"Found name: {name}")

    """for name in names :
        exec_name = name.get_text(strip=True)
        names.append(exec_name)"""

    with open(OUPTUT_CSV, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for name in names:
            writer.writerow([name])

def main():
    html = fetch_page(URL)
    parse_names_in_html(html)

if __name__ == "__main__":
    main()
