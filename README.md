# ADAM
Advanced Discord Automated Moderator, aka ADAM, is a python discord bot project. This bot is developed using [discord.py](https://github.com/Rapptz/discord.py) on [Replit](https://replit.com)



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
- Run the code and the bot will show its name on the console, indicating that  it's online.
## Installation on Replit
- Clone or fork the repository
- Open a new Repl
- Within the Repl, click on the secrets tab
  
![](https://i.imgur.com/Yq7h5re.png)
- Add the token into the box shown below

![](https://i.imgur.com/MgFLrE8.png)
- Within `main.py` add the following
  ```python
   token = os.environ['TOKEN']
   ```
- Press the **Run** button and the bot will show its name in the console, indicating that it's online.