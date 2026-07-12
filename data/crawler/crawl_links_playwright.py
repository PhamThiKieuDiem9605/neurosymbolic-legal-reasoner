from playwright.sync_api import sync_playwright
import pandas as pd
from urllib.parse import urljoin

BASE = "https://thuvienphapluat.vn"

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir=r"D:\crawler_profile",
        channel="chrome",
        headless=False
    )

    page = context.new_page()

    page.goto(
        "https://thuvienphapluat.vn/hoi-dap-phap-luat/bao-hiem",
        wait_until="domcontentloaded",
        timeout=60000
    )

    print(page.title())

    html = page.content()

    with open(
        "debug.html",
        "w",
        encoding="utf8"
    ) as f:
        f.write(html)

    input("Enter...")

    context.close()