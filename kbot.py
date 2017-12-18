#This is a bot that will eventually do useful things

import discord
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix="#")

@bot.event
async def on_ready():
	print ("Readyyyyyy")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say(":ping_pong: ping! xSSS")
	print("user has pinged")

@bot.command(pass_context=True)

bot.run("Token")

