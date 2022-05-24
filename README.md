# ADAM
Advanced Discord Automated Moderator, aka ADAM, is a python discord bot project. This bot is developed using [discord.py](https://github.com/Rapptz/discord.py) on [Replit](https://replit.com)

![ADAMLOGO]()

# Setup
## Local Installation
**An installation of [`python-dotenv`](https://pypi.org/project/python-dotenv/) is required**
- Clone or fork the repository
- Setup a `.env` file and put your discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
- Insert the token into the `.env` file with the syntax shown below
`token = INSERT TOKEN HERE`
- Do the following in `main.py`
  ```python
  from dotenv import load_dotenv
  token = load_dotenv(".env")
  ```
  