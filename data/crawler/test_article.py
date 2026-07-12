from playwright.sync_api import sync_playwright

url = "https://thuvienphapluat.vn/hoi-dap-phap-luat/cong-van-4022bhxhqlt-sua-doi-muc-ho-tro-dong-bhxh-tu-nguyen-tu-172026-chi-tiet-ra-sao-138095338.html"

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir=r"D:\crawler_profile",
        channel="chrome",
        headless=False
    )

    page = context.new_page()

    page.goto(
        url,
        wait_until="networkidle",
        timeout=60000
    )

    html = page.content()

    with open(
        "data/raw/article.html",
        "w",
        encoding="utf8"
    ) as f:
        f.write(html)

    print("saved")

    input("Enter...")

    context.close()