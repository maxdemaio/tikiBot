import logging
import os

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
async def copy(ctx, *args):
    await ctx.send(f"{' '.join(args)}")


client.run(os.getenv("TOKEN"))
