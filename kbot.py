#This is a bot that will eventually do useful things

import discord
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix="#")

#Displays when ran
@bot.event
async def on_ready():
	print ("Ready")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)

#"Pings" the user
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say(":ping_pong: ping!")
	print("user has pinged")

#Prints out user info
@bot.command(pass_context=True)
async def  info(ctx, user: discord.Member):
	await bot.say("The username is: {}".format(user.name))
	await bot.say("The users ID is: {}".format(user.id))
	await bot.say("The users status is: {}".format(user.status))
	await bot.say("The users highest role is: {}".format(user.top_role))
	await bot.say("The user joined at: {}".format(user.joined_at))

#Displays command list
@bot.command(pass_context=True)
async def commands(ctx):
	await bot.say("To ping the bot: #ping")
	await bot.say("To get info on a user: #info @user")
	await bot.say("More commands coming soon!")

bot.run("MzkxMzA5MjE1NjY0MTc3MTUy.DRWyrA.ExifRHOC354vDucFiSFWs7ewVmc")

