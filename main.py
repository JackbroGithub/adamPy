import discord
from discord.ext import commands
import os
import random
import asyncio

#version
version = "0"
#time
date = "5/24/2022"

token = os.environ['TOKEN']

bot = commands.Bot(command_prefix="$",intents = discord.Intents.all())
bot.remove_command("help")

greetings = ["Hello,", "Hi there,", "Nice to meet you,", "Glad to meet you,", "How are you doing,", "Sup!", "What up, mate!", "Howdy!", "Hallo,"]
greet_end=["It's a nice day innit?", "Hope you have a nice day!"]

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
  await member.send(f"{member.name} your code is {userpas}")



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
  else:
    await message.channel.purge(limit = 1)
    await message.channel.send("Incorrect number")

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


#mini-games  
@bot.command(name="rps", description="play rock paper scissors with ADAM!")
async def rps(ctx, message:str):
  choices = ["🪨", "📄", "✂️"]
  adam_ans = random.choice(choices) 
  answer = message.lower()
  if answer not in choices:
    await ctx.send("That's not an available option, only use 🪨, 📄, or ✂️!")
  else:
    if adam_ans == answer:
      await ctx.send(f"That's a tie! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "🪨":
      if answer == "📄":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "✂️":
        await ctx.send(f"ADAM won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "📄":
      if answer == "🪨":
        await ctx.send(f"ADAM won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "✂️":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
    if adam_ans == "✂️":
      if answer == "🪨":
        await ctx.send(f"You won! ADAM picked `{adam_ans}` while you picked `{answer}`!")
      if answer == "📄":
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
async def dice(ctx):
  
#run
bot.run(token)

