import csv
import requests
from bs4 import BeautifulSoup


def scrape_quotes():
  url = "http://quotes.toscrape.com/"
  print(f"[INFO] Connecting to {url}...")

  response = requests.get(url)
  if response.status_code != 200:
    print("[ERROR] Failed to fetch the page.")
    return

  soup = BeautifulSoup(response.text, "html.parser")
  quotes_data = []

  items = soup.find_all("div", class_="quote")
  for item in items:
    text = item.find("span", class_="text").get_text()
    author = item.find("small", class_="author").get_text()
    quotes_data.append({"Quote": text, "Author": author})

  filename = "scraped_quotes.csv"
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Quote", "Author"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in quotes_data:
      writer.writerow(row)

  print(
      f"[SUCCESS] Scraped {len(quotes_data)} quotes successfully! Saved to"
      f" '{filename}'."
  )


if __name__ == "__main__":
  scrape_quotes()
