# Discord AFK Voice Bot

A minimal Discord bot that joins your voice channel and stays connected using a slash command.

## Features

- Slash command `/afk`
- User must be in a voice channel
- Bot joins and stays connected
- Uses environment variables for secure token storage

## Requirements

- Python 3.9+
- discord.py 2.x

## Installation

Clone the repository:

git clone https://github.com/yourname/discord-afk-bot.git
cd discord-afk-bot

Install dependencies:

pip install -r requirements.txt

## Setup

Create a `.env` file:

TOKEN=your_bot_token_here

Make sure you enabled:

- Voice State Intent (Developer Portal)
- Bot permissions for joining voice channels

## Run the bot

python bot.py

## Notes

The bot will stay in the voice channel until manually disconnected or the process is stopped
