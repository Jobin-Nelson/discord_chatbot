# Discord Chatbot

A basic bot to fetch [torrent](https://piratebayorg.net/) links. I’ve also included a script to [get_links](https://github.com/Jobin-Nelson/discord_chatbot/blob/main/get_links.py) straight from the command line. 

## Installation

- First, you need to create a virtual environment, this part is optional, although I do recommend it

```
python -m venv venv
```

- Then make sure that all [required](https://github.com/Jobin-Nelson/discord_chatbot/blob/main/requirements.txt) libraries are downloaded

```
pip install -r requirements.txt
```

- Run the below code to download the necessary webdrivers

```
playwright install
```

- Store the bot token in a .env file if you are running the bot locally
- If you are running the bot from [replit](https://replit.com/) you can use the secret environment variable to store the token with key set to ‘TOKEN’
- You can also use [uptime](https://uptimerobot.com/) robot to constantly ping the flask server every 5 minutes to keep the bot running 24/7
- Search for any movie with .search
- You can get links from the command line by running, the number of links is optional

```
python get_links.py "movie name" [number of links]
```