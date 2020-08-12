import logging
import os
import random

import discord
from discord.ext import commands

import settings

# Create bot instance
# Set prefix for our commands
client = commands.Bot(command_prefix = "$")

# Set up logging
logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Hi Dylando!"))
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    """ Bot detects someone has joined a server it is in """
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    """ Bot detects someone has left a server it is in """
    print(f"{member} has left a server.")

@client.command()
async def info(ctx):
    await ctx.send("My source code is here!: https://github.com/maxwelldemaio/tikiBot")

@client.command()
async def copy(ctx, *args):
    await ctx.send(f"{' '.join(args)}")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    question = ' '.join(question)
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


## Sailers commands
## Please note, sailors is spelt wrong on purpose (It's a joke pertaining to the videos)

# Weekly sailers commands
@client.command(aliases=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])
async def day(ctx):
    """ Return a video """
    aliasUsed = ctx.invoked_with
    
    if aliasUsed == "monday":
        emoji = "😔"
        file = discord.File("./staticfiles/monday.mp4", filename="monday.mp4")
        await ctx.send(f"It be Monday, sailers {emoji}", file=file)
    elif aliasUsed == "tuesday":
        emoji = "🌮"
        file = discord.File("./staticfiles/tuesday.mp4", filename="tuesday.mp4")
        await ctx.send(f"It be Taco Tuesday, sailers {emoji}", file=file)
    elif aliasUsed == "wednesday":
        emoji = "💪"
        file = discord.File("./staticfiles/wednesday.mp4", filename="wednesday.mp4")
        await ctx.send(f"It be Wednesday, sailers {emoji}", file=file)
    elif aliasUsed == "thursday":
        emoji = "👀"
        file = discord.File("./staticfiles/thursday.mp4", filename="friday.mp4")
        await ctx.send(f"It be Thursday, sailers {emoji}", file=file)
    elif aliasUsed == "friday":
        emoji = "🐐"
        file = discord.File("./staticfiles/friday.mp4", filename="friday.mp4")
        await ctx.send(f"It be Friday, sailers {emoji}", file=file)
    elif aliasUsed == "saturday":
        emoji = "🌟"
        file = discord.File("./staticfiles/saturday.mp4", filename="sunday.mp4")
        await ctx.send(f"It be Saturday, sailers {emoji}", file=file)
    elif aliasUsed == "sunday":
        emoji = "🏌️‍♂️"
        file = discord.File("./staticfiles/sunday.mp4", filename="sunday.mp4")
        await ctx.send(f"It be Sunday, sailers {emoji}", file=file)
    else:
        await ctx.send("Specify a day, sailer!")

# Time of day sailers
@client.command(aliases=["night",])
async def time(ctx):
    """ Return a video """
    aliasUsed = ctx.invoked_with
    
    if aliasUsed == "night":
        emoji = "😴"
        file = discord.File("./staticfiles/night.mp4", filename="night.mp4")
        await ctx.send(f"Goodnight, sailers {emoji}", file=file)
    else:
        await ctx.send("Specify a time, sailer!")


client.run(os.environ['TOKEN'])
