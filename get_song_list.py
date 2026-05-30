import requests
from bs4 import BeautifulSoup
import csv
import os
import pandas as pd

def scrape_billboard_2025():
    url = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2025"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Fetching URL: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Wikipedia tables usually have "wikitable sortable"
    # Find the main list table
    table = soup.find("table", class_="wikitable")
    
    if not table:
        print("Could not find the target table on the page.")
        return

    data = []
    # Find headers
    headers_row = table.find("tr")
    header_cols = [th.get_text(strip=True) for th in headers_row.find_all(["th", "td"])]
    
    print(f"Found headers: {header_cols}")

    # Determine indices for "Title" and "Artist(s)"
    try:
        # Some tables might have slightly different names, handle case and variations
        title_idx = -1
        artist_idx = -1
        for i, h in enumerate(header_cols):
            if "title" in h.lower():
                title_idx = i
            if "artist" in h.lower():
                artist_idx = i
        
        if title_idx == -1 or artist_idx == -1:
            raise ValueError(f"Required columns not found in {header_cols}")
            
    except ValueError as e:
        print(f"Error: {e}")
        return

    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        cols = row.find_all(["td", "th"])
        if len(cols) > max(title_idx, artist_idx):
            title = cols[title_idx].get_text(strip=True).strip('"')
            artist = cols[artist_idx].get_text(strip=True)
            data.append({"Title": title, "Artist": artist})

    output_file = "Songs_list.csv"
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Artist"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Successfully scraped {len(data)} entries and saved to {output_file}")


if __name__ == "__main__":
    scrape_billboard_2025()
