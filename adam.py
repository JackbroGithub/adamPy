import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()
token = "NTY5MjE2ODMyODk3Mjg2MTU2.Gi4Omx.4kHpItqv8IhviPUGuxraNAo5omRNGhK703aEhg"
bot = commands.Bot(command_prefix='$')
blocked_word = ["nigga", "nigger", "pee", "poo"]


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.reply(f"Hello, {ctx.author.display_name}, it is my pleasure to meet you.")

bot.run(getenv('TOKEN'))