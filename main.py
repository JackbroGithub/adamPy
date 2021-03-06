import discord
import os
import random
import asyncio
import json
import youtube_dl
import functools
import itertools
#import certain packages
from PIL import Image
from io import BytesIO
from requests import get
from async_timeout import timeout
from discord.ext import commands
#import files
import keep_alive
#version
version = "0"
#time
date = "5/24/2022"
#setup
token = os.environ['TOKEN']
bot = commands.Bot(command_prefix="$",intents = discord.Intents.all())
bot.remove_command("help")
greetings = ["Hello,", "Hi there,", "Nice to meet you,", "Glad to meet you,", "How are you doing,", "Sup!", "What up, mate!", "Howdy!", "Hallo,"]
greet_end=["It's a nice day innit?", "Hope you have a nice day!", "It's my pleasure to meet you!", "Enjoy your day!", "Cheers mate!", "Wie geht's?"]
keys=["13431556", "32321424", "41545141146", "14435422456", "82745673228"]

#Pre-process
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    
async def ch_presence():
  await bot.wait_until_ready()
  statuses = [f"Try out $hello!", f"Confused? Try $help"]
  while not bot.is_closed():
    status = random.choice(statuses)
    await bot.change_presence(activity=discord.Game(name=status))
    await asyncio.sleep(10)
bot.loop.create_task(ch_presence())


@bot.event
async def on_member_join(member):
  welcome_embed = discord.Embed(title="Welcome To The Server", description=f"{member.display_name}, welcome to the server, we can't wait to have a good time with you on the server!")
  await member.send(embed = welcome_embed)
  userpas = random.choice(keys)
  await member.send(f"{member.name} your code is ||{userpas}||")



@bot.listen("on_message")
async def on_message(message):
  if message.author.id == 569216832897286156:
    return
  if message.channel.id != 978516230216503337:
    return
  if any(word in message.content.lower() for word in keys):
    await message.channel.purge(limit = 1)
    verifyRole = discord.utils.get(message.guild.roles, name = "Verified")
    await message.author.add_roles(verifyRole)
    await message.channel.send("That's correct!")
    await asyncio.sleep(5)
    await message.channel.purge(limit = 1)
  else:
    await message.channel.purge(limit = 1)
    await message.channel.send("Incorrect number")
    await asyncio.sleep(5)
    await message.channle.purge(limit = 1)

#bot commands
@bot.command(name="hello", description="Sends a warm greet to user.")
async def hello(ctx):
    await ctx.reply(random.choice(greetings) + f" {ctx.author.display_name}. " + random.choice(greet_end))

@bot.command(name="ping", description="Replies Pong.")
async def ping(ctx):
    await ctx.reply("pong.")

@bot.command(description="Find helpful command guides here.")
async def help(ctx):
  em = discord.Embed(title = "ADAM's Help Center", description="Find helpful command guides here.", color = ctx.author.color)
  for command in bot.walk_commands():
    description = command.description
    if not description or description is None or description == "":
      description = "No Description Found."
    em.add_field(name=f"`${command.name}{command.signature if   command.signature is not None else ''}`", value = description)
  await ctx.send(embed = em)
  
@bot.command(name="gift", description="sends a gift to a user.")
async def gift(ctx,user:discord.Member):
  await ctx.reply("Gift is sent to user!")
  await user.send(f"{user.display_name}, {ctx.author.display_name} gave you a ***gift!***")
  await user.send("Hold on a sec, let me get the gift")
  await asyncio.sleep(5)
  await user.send("Here It Is!")
  await user.send("https://giphy.com/gifs/rick-astley-Ju7l5y9osyymQ")

@bot.command(name="clear", description="clears 5 lines of messages")
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount+1)

@bot.command(name="info",description="shows the current info of ADAM")
async def info(ctx):
  em = discord.Embed(title="ADAM", description=f"Build "+version)
  em.add_field(name=f"Build published date", value = date)
  em.add_field(name=f"Check out the Github Repo!", value="https://github.com/JackbroGithub/adamPy")
  await ctx.send(embed=em)

@bot.command(name="wanted", description="posts a wanted picture in text channel")
@commands.has_permissions(administrator = True)
async def wanted(ctx, user:discord.Member = None):
  if user == None:
    user = ctx.author
  wantedRole = discord.utils.get(user.guild.roles, name = "Wanted")
  wanted = Image.open("wanted2.jpg")
  asset = user.avatar_url_as(size = 256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((256, 256))
  wanted.paste(pfp, (110, 240))
  wanted.save("profile.jpg")
  await ctx.reply(file = discord.File("profile.jpg"))
  await user.edit(roles=[])
  await user.add_roles(wantedRole)

@bot.command(name="meme", description="sends a random meme from Reddit")
async def meme(ctx):
  content = get("https://meme-api.herokuapp.com/gimme").text
  data = json.loads(content,)
  meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random()).set_image(url=f"{data['url']}")
  await ctx.reply(embed = meme)

@bot.command(name="funny", description="sends a random funny quote")
async def funny(ctx):
  funny_q = ["I???m sick of following my dreams, man. I???m just going to ask where they???re going and hook up with ???em later.", "Gentlemen, you can???t fight in here. This is the war room.","My mother always used to say: The older you get, the better you get, unless you???re a banana.", "Halloween is the beginning of the holiday shopping season. That???s for women. The beginning of the holiday shopping season for men is Christmas Eve.", "Before you criticize someone, you should walk a mile in their shoes. That way when you criticize them, you are a mile away from them and you have their shoes.", 'Bob: ???Looks like you???ve been missing a lot of work lately.???Peter: ???I wouldn???t say I???ve been missing it, Bob.???', "Clothes make the man. Naked people have little or no influence in society.", "Before you marry a person, you should first make them use a computer with slow Internet to see who they really are.", "I love being married. It???s so great to find that one special person you want to annoy for the rest of your life.", "Ned, I would love to stand here and talk with you???but I???m not going to."]
  await ctx.send(random.choice(funny_q))
#mini-games  
@bot.command(name="rps", description="play rock paper scissors with ADAM!")
async def rps(ctx, message:str):
  choices = ["????", "????", "??????"]
  adam_ans = random.choice(choices) 
  answer = message.lower()
  if answer not in choices:
    await ctx.send("That's not an available option, only use ????, ????, or ??????!")
  else:
    if adam_ans == answer:
      await ctx.send(f"That's a tie! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "????":
      if answer == "????":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "??????":
        await ctx.send(f"ADAM won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "????":
      if answer == "????":
        await ctx.send(f"ADAM won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "??????":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "??????":
      if answer == "????":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "????":
        await ctx.send(f"ADAM won! ADAM picked `{adam_ans}` while you picked `{answer}`!")

@bot.command(name="guess", description="play Da Vinci Code with ADAM!")
async def guess(ctx):
  await ctx.send("Guess the number from 1 to 100!")
  choice = random.randint(1, 100)
  min_guess = 1
  max_guess = 100 
  while True:
    answer = await bot.wait_for("message")
    try:
      answer_int = int(answer.content)
      if answer_int == choice:
        await ctx.send(f"Congrats, {ctx.author.display_name}, you got it correct!")
        break
      elif answer_int < choice:
        min_guess = answer_int
        await ctx.send(f"The number is between {min_guess} ~ {max_guess}")
      elif answer_int > choice:
        max_guess = answer_int
        await ctx.send(f"The number is between {min_guess} ~ {max_guess}")
    except ValueError:
      await ctx.send("Please enter a valid number")
@bot.command(name="dice", description="play roll the dice")
async def dice(ctx, amount:int):
  for i in range(1, amount+1, 1):
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    value1 = random.choice(dice1)
    value2 = random.choice(dice2)
    value3 = random.choice(dice3)
    #the value of the two dices are the same
    if value1 == value2 or value1 == value3 or value2 == value3:
      await ctx.send(f"Two same points! The values of all the dice are {value1}, {value2}, {value3}")
    if value1 == value2 == value3:
        await ctx.send(f"All of your dice have the value of {value1}!")
    elif value1 != value2 and value1 != value3 and value2 != value3:
      await ctx.send(f"None of the values are the same, they're {value1}, {value2}, {value3}")



              
#run
bot.run(token)


