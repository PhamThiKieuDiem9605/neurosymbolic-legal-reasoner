import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

BASE = "https://thuvienphapluat.vn"

CATEGORIES = [
    "hoi-dap-phap-luat/bao-hiem",
    "hoi-dap-phap-luat/lao-dong-tien-luong",
    "hoi-dap-phap-luat/doanh-nghiep",
]

rows = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for category in CATEGORIES:

    print(f"\nScanning {category}")

    for page in tqdm(range(1, 50)):

        url = f"{BASE}/{category}?page={page}"

        try:
            r = requests.get(
                url,
                headers=headers,
                timeout=20
            )

            soup = BeautifulSoup(
                r.text,
                "html.parser"
            )

            links = soup.find_all("a")

            count = 0

            for a in links:

                href = a.get("href")

                if not href:
                    continue

                if "/hoi-dap-phap-luat/" not in href:
                    continue

                title = a.get_text(
                    strip=True
                )

                if len(title) < 20:
                    continue

                rows.append({
                    "category": category,
                    "title": title,
                    "url": urljoin(BASE, href)
                })

                count += 1

            if count == 0:
                break

        except Exception as e:
            print(e)

df = pd.DataFrame(rows)

df = df.drop_duplicates(
    subset=["url"]
)

output = "data/raw/tvpl_links.xlsx"

df.to_excel(
    output,
    index=False
)

print("Saved:", output)
print("Total:", len(df))