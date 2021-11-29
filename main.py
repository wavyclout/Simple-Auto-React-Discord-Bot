import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='ar!') # Bot prefix

@bot.event
async def on_ready():
    print('✅ Auto-React Operational') # This message will show in the console when the bot is online and ready to be used

@bot.event
async def on_message(message):
    if message.channel.id == CHANNELID: #Paste your channel ID
        await message.add_reaction("👍") # If you wish to add custom emojis make sure to use the emoji ID only. For Example if the emoji looks like this <:BestDeveloper:911429378448179231> make sure to only paste the emoji ID 911429378448179231  
        await message.add_reaction("👎") # Same as line 14

bot.run("BOT TOKEN") # Paste bot token