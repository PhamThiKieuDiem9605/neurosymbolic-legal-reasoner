from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://thuvienphapluat.vn/hoi-dap-phap-luat/bao-hiem",
        wait_until="networkidle",
        timeout=60000
    )

    print("TITLE:", page.title())

    html = page.content()

    with open(
        "data/raw/bao_hiem.html",
        "w",
        encoding="utf8"
    ) as f:
        f.write(html)

    print("Saved data/raw/bao_hiem.html")

    input("Press Enter...")