import requests

url = "https://thuvienphapluat.vn/hoi-dap-phap-luat/bao-hiem"

r = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=20
)

print("STATUS:", r.status_code)
print("URL:", r.url)

with open("data/raw/test.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Saved HTML to data/raw/test.html")
print(r.text[:3000])