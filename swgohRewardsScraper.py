from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

filename = "swgohRewards.csv"
f = open(filename, "w")

headers = "mission, reward\n"
f.write(headers)

# loops through both dark and light side battles
for p in range(1,3):
	if p == 1:
		my_url = "https://swgoh.gg/db/missions/lightside/?stage=M0{}"
	else:
		my_url = "https://swgoh.gg/db/missions/darkside/?stage=M0{}"

	# loops through all 9 stages
	for i in range(1,10):
		url = my_url.format(i)

		# opening up connection, grabbing the page
		req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
		uClient = urlopen(req)
		page_html = uClient.read()
		uClient.close()

		# html parsing
		page_soup = soup(page_html, "html.parser")

		# grabs each mission level
		missions = page_soup.findAll("div",{"class" : "media-body-text"})

		# places the reward with the appropriate mission
		for mission in missions:
			level_name = soup.get_text(mission.h4)

			rewards = mission.findAll("span",{"class" :"loot-item-name"})
			for reward in rewards:
				reward_name = reward.text

				if p ==1:
					f.write("Light " + level_name + "," + reward_name + "\n")
				else:
					f.write("Dark " + level_name + "," + reward_name + "\n")

f.close()