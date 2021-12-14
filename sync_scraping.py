from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://piratebayorg.net")

    page.fill("#home > main > section > form > div:nth-child(1) > input[type=search]", "vikings")
    page.click("#home > main > section > form > div:nth-child(3) > input[type=submit]:nth-child(1)")
    page.is_visible("#st > span.item-icons > a")

    html = page.inner_html("#torrents")
    soup = BeautifulSoup(html, "html.parser")
    entries = soup.find_all(id="st")

    payload = []
    for item in entries:
        payload.append(
            [item.find(class_="list-item item-name item-title").a.text,
            item.find(class_="list-item item-size").text,
            item.find(class_="item-icons").a['href']]
            )

    res = [" ".join(item) for item in payload]
    print(str(res))
    