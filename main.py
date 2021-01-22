import discord
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "hello" or message.content == "Hello":
		await message.channel.send("Oh oh oh!")

@bot.event
async def on_message(message):
	if message.content == "maps" or message.content == "Maps":
		await message.channel.send("Stai chiedendo una mappa? Eccola qui!")    
		await message.channel.send("https://discord.com/developers/applications/802139815259668490/bot")    

@bot.event
async def on_message(message):
    if message.content.startswith('!map'):
        embedVar = discord.Embed(title="Your map", description="lnvjfhdjhdbszc bavbhqjdojvjqi q", color=0xff0000)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)









bot.run(DISCORD_TOKEN)
