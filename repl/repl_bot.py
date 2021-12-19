from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import discord
import os
from keep_alive import keep_alive
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.channel.name =="ask-valsan":
        user_name = str(message.author).split("#")[0]
        user_message = str(message.content)

        if message.content.startswith(".search"):
            search_term = message.content[8:]

            async def scrape():
                async with async_playwright() as p:
                    browser = await p.chromium.launch()
                    page = await browser.new_page()
                    await page.goto("https://piratebayorg.net", timeout=60000)

                    await page.fill("#home > main > section > form > div:nth-child(1) > input[type=search]", f"{search_term}")
                    await page.click("#home > main > section > form > div:nth-child(3) > input[type=submit]:nth-child(1)")
                    await page.is_visible("#st > span.item-icons > a")

                    html = await page.inner_html("#torrents")
                    soup = BeautifulSoup(html, "html.parser")
                    entries = soup.find_all(id="st")

                    name = entries[0].find(class_="list-item item-name item-title").a.text
                    size = entries[0].find(class_="list-item item-size").text
                    link = entries[0].find(class_="item-icons").a['href']

                    payload = f"Name: {name}\nSize: {size}\nLink: {link}"

                    await browser.close()
                return payload

            await message.channel.send(await scrape())

        if user_message.lower() == 'hello':
            await message.channel.send(f"Hello {user_name}!")
            return
        elif user_message.lower() =="bye":
            await message.channel.send(f"See you later {user_name}!")
        elif user_message.lower()=="valsa":
            await message.channel.send("Yes boss")
keep_alive()
client.run(my_secret)