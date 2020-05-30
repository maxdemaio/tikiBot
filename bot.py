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

# Weekly Sailors Commands
@client.command(aliases=["monday", "tuesday", "wednesday", "friday", "sunday"])
async def day(ctx):
    """ Return a 'Rise and Shine, Sailors' video """
    aliasUsed = ctx.invoked_with
    
    if aliasUsed == "monday":
        emoji = "😔"
        file = discord.File("./it_be/monday.mp4", filename="monday.mp4")
        await ctx.send(f"It be Monday, sailors {emoji}", file=file)
    elif aliasUsed == "tuesday":
        emoji = "🌮"
        file = discord.File("./it_be/tuesday.mp4", filename="tuesday.mp4")
        await ctx.send(f"It be Taco Tuesday, sailors {emoji}", file=file)
    elif aliasUsed == "wednesday":
        emoji = "💪"
        file = discord.File("./it_be/wednesday.mp4", filename="wednesday.mp4")
        await ctx.send(f"It be Wednesday, sailors {emoji}", file=file)
    elif aliasUsed == "friday":
        emoji = "🐐"
        file = discord.File("./it_be/friday.mp4", filename="friday.mp4")
        await ctx.send(f"It be Friday, sailors {emoji}", file=file)
    elif aliasUsed == "sunday":
        emoji = "🏌️‍♂️"
        file = discord.File("./it_be/sunday.mp4", filename="sunday.mp4")
        await ctx.send(f"It be Sunday, sailors {emoji}", file=file)
    else:
        await ctx.send("Specify a day, sailor!")


client.run(os.getenv("TOKEN"))
