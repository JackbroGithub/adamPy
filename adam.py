import discord
from discord.ext import commands

token = "NTY5MjE2ODMyODk3Mjg2MTU2.Gi4Omx.4kHpItqv8IhviPUGuxraNAo5omRNGhK703aEhg"
bot = commands.Bot(command_prefix='$')
blocked_word = ["nigga", "nigger", "pee", "poo"]


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.reply(f"Hello, {ctx.author.display_name}, it is my pleasure to meet you.")

@client.event
async def on_message(msg):
    if msg.author != client.user:
        for text in blocked_word:
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return
        print("Not deleteing...")

        if msg.content.lower().startswith("$hi"):
            await msg.channel.send(f"Hi, {msg.author.display_name}, it's my pleasure to meet you.")
        if msg.content.lower().startswith("$play"):

bot.run(token)