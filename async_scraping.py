from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import asyncio

payload = []

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://piratebayorg.net")

        await page.fill("#home > main > section > form > div:nth-child(1) > input[type=search]", "vikings")
        await page.click("#home > main > section > form > div:nth-child(3) > input[type=submit]:nth-child(1)")
        await page.is_visible("#st > span.item-icons > a")

        html = await page.inner_html("#torrents")
        soup = BeautifulSoup(html, "html.parser")
        entries = soup.find_all(id="st")

        
        for item in entries:
            payload.append(
                [item.find(class_="list-item item-name item-title").a.text,
                item.find(class_="list-item item-size").text,
                item.find(class_="item-icons").a['href']]
                )
        await browser.close()

asyncio.run(main())   
res = [" ".join(item) for item in payload]
print(str(res))
    