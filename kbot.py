#This is a bot that will eventually do useful things

import discord
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 
from bs4 import BeautifulSoup 
import requests

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

@bot.command(pass_context=True)
async def roster(ctx, *,arg):
	arg.lower()
	#decides what team the user wants
	result = ""
	if arg == "tsm" or arg == "team solomid":
        	result = "https://dotesports.com/league-of-legends/teams/team-solomid"
	elif arg == "100t" or arg == "100 thieves":
        	result = "https://dotesports.com/league-of-legends/teams/100-thieves"
	elif arg == "c9" or arg == "cloud 9":
        	result = "https://dotesports.com/league-of-legends/teams/cloud9"
	elif arg == "ef" or arg == "echo fox":
        	result = "https://dotesports.com/league-of-legends/teams/echo-fox"
	elif arg == "gg" or arg == "golden guardians":
        	result = "https://dotesports.com/league-of-legends/teams/golden-guardians"
	elif arg == "og" or arg == "optic gaming":
        	result = "https://dotesports.com/league-of-legends/teams/optic-gaming"
	elif arg == "cg" or arg == "clutch gaming":
        	result = "https://dotesports.com/league-of-legends/teams/clutch-gaming"
	elif arg == "clg" or arg == "counter logic gaming":
        	result = "https://dotesports.com/league-of-legends/teams/counter-logic-gaming"
	else:
		await bot.say("Could not find that team, make sure you spelled it right(NA teams are the only ones supported at the moment)")

	#gets content from site
	result = requests.get(result)
	c = result.content
	soup = BeautifulSoup(c,"html.parser")

	#Takes all div classes(with the name _1XJFK)  and puts the text into players list
	players = []
	for row in soup.find_all("div", attrs={"class": "_1XJFK"}):
        	players.append(row.text)
	#Takes all div classes(with the name _1wU8T) and puts the text into positions list
	position = []
	for row  in soup.find_all("div", attrs={"class": "_1wU8T"}):
        	position.append(row.text)

	#takes players and postions and outputs them side by side
	for i,x in zip(players, position):
        	await bot.say(i + ": " + x)




	
bot.run("MzkxMzA5MjE1NjY0MTc3MTUy.DRz0DA.pS8_5lvCt32AqKbVpj7TeIBQzqA")

