import os
from dotenv import load_dotenv 
import discord
from discord.ext import commands
import random

# Lets grab out environment variables from .env file
load_dotenv("bot_config.env")
token = os.getenv("DISCORD_TOKEN")
bot_name = os.getenv("BOT_NAME")

intents = discord.Intents.default()
intents.members = True #This is needed to get information about members in voice channels

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command(
    name="pick",
    description="Pick a random winner from a voice channel"
)

async def pick_random_user(ctx):
    # Get the current voice channel of the user.
    voice_state = ctx.author.voice
    if not voice_state:
        await ctx.send("You are not connected to any voice channel")
        return
    
    # Get the voice channel from the voice state
    voice_channel = voice_state.channel

    # Get a list of users currently in the voice channel
    members = voice_channel.members

    # Pick a random user from the list of members
    winner = random.choice(members)

    # Send a message with the name of the picked user
    await ctx.send(
        f"The winner is {winner.mention}! Congratulations!"
    )


    bot.run(token)
    
    
