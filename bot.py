import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv('bot_config.env')  # Load environment variables from .env file
token = os.getenv("DISCORD_TOKEN")
bot_name = os.getenv("BOT_NAME")

intents = discord.Intents.default()
intents.members = True  # You need to enable the Members Intent to get information about members in voice channels.

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    try:
       guild = discord.Object(id=686337802581180494)
       synced = await bot.tree.sync(guild=guild)
       print(f"Synced {len(synced)} commands to the guild.")

    except Exception as e:
        print(f"Error syncing commands: {e}")

GUILD_ID = discord.Object(id=686337802581180494)

@bot.tree.command(name="pick",
             description="Pick a random user from a voice channel",
             guild=GUILD_ID)
async def pick_random_user(interaction: discord.Interaction):
  user = interaction.user
  # Get the voice channel that the command user is currently in
  voice_state = user.voice
  if not voice_state:
    await interaction.response.send_message("You are not connected to any voice channel")
    return
  channel = voice_state.channel

  # Get a list of users currently in the voice channel
  members = channel.members

  # Pick a random user from the list of members
  random_member = random.choice(members)

  # Send a message with the name of the picked user
  await interaction.response.send_message(f"The winner is {random_member.mention}! Congratulations!")


bot.run(token)