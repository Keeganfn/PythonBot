from bs4 import BeautifulSoup
import requests 

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
	print("thats not a team") 
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
	print(i + ": " + x)



