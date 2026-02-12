import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="afk", description="Join your VC and stay there")
async def afk(interaction: discord.Interaction):
    if not interaction.user.voice:
        await interaction.response.send_message(
            "You must be in a voice channel first.",
            ephemeral=True
        )
        return

    channel = interaction.user.voice.channel

    if interaction.guild.voice_client:
        await interaction.response.send_message(
            "Already connected to a voice channel.",
            ephemeral=True
        )
        return

    await channel.connect()
    await interaction.response.send_message(f"Joined {channel.name}.")

bot.run(TOKEN)
