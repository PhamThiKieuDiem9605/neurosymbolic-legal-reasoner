import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0"
}

links = pd.read_excel(
    "data/raw/tvpl_links.xlsx"
)

records = []

for _, row in tqdm(
    links.iterrows(),
    total=len(links)
):

    try:

        html = requests.get(
            row["url"],
            headers=headers,
            timeout=20
        ).text

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        content = soup.get_text(
            "\n",
            strip=True
        )

        records.append({
            "category": row["category"],
            "title": row["title"],
            "url": row["url"],
            "content": content
        })

    except Exception:
        continue

df = pd.DataFrame(records)

df.to_excel(
    "data/raw/tvpl_articles.xlsx",
    index=False
)

print("Done")