import requests
from bs4 import BeautifulSoup


#might be fun to make this where it saves the values each run using pickle to display later using matplotlib or whatever
for i in range(3):
    print ("")
    if i == 1:
        print ("Live Player Counts")

names = ["https://playercounter.com/destiny/",
        "https://playercounter.com/elden-ring/",
        "https://playercounter.com/minecraft/",
        "https://playercounter.com/fortnite.",
        "https://playercounter.com/among-us/",
        "https://playercounter.com/apex-legends/",
        "https://playercounter.com/brawlhalla/",
        "https://playercounter.com/call-of-duty-warzone/",
        "https://playercounter.com/clash-of-clans/",
        "https://playercounter.com/call-of-duty-modern-warfare/",
        "https://playercounter.com/counter-strike-global-offensive/",
        "https://playercounter.com/diablo-3/",
        "https://playercounter.com/dota-2/",
        "https://playercounter.com/fall-guys/",
        "https://playercounter.com/fifa-23/",
        "https://playercounter.com/final-fantasy-14-xiv/",
        "https://playercounter.com/for-honor/",
        "https://playercounter.com/forza-horizon-5/",
        "https://playercounter.com/genshin-impact/",
        "https://playercounter.com/grand-theft-auto-5/",
        "https://playercounter.com/gran-turismo-sport/",
        "https://playercounter.com/guild-wars-2/",
        "https://playercounter.com/halo/",
        "https://playercounter.com/hearthstone/",
        "https://playercounter.com/hollow-knight/",
        "https://playercounter.com/league-of-legends/",
        "https://playercounter.com/modern-warfare-2/",
        "https://playercounter.com/mortal-kombat-11/",
        "https://playercounter.com/naraka-bladepoint/",
        "https://playercounter.com/overwatch/",
        "https://playercounter.com/overwatch-2/",
        "https://playercounter.com/paladins/",
        "https://playercounter.com/pokemon-sword-shield/",
        "https://playercounter.com/pubg/",
        "https://playercounter.com/roblox/",
        "https://playercounter.com/red-dead-redemption-2/",
        "https://playercounter.com/rocket-league/",
        "https://playercounter.com/rust/",
        "https://playercounter.com/runescape/",
        "https://playercounter.com/sea-of-thieves/",
        "https://playercounter.com/sekiro/",
        "https://playercounter.com/sims-4/",
        "https://playercounter.com/splitgate/",
        "https://playercounter.com/steam/",
        "https://playercounter.com/titanfall-2/",
        "https://playercounter.com/valorant/",
        "https://playercounter.com/wallpaper-engine/",
        "https://playercounter.com/warframe/",
        "https://playercounter.com/world-of-warcraft/"
        ]

gameDictionary = {}
arr = []

for i in names:
    url = i

    leng = len(url)
    gameName = (url[26:leng-1])
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    stringCheck = soup
    finalString = stringCheck.find("h2")
    finalString = str(finalString)
    finalString = (finalString[4:14])
    
    te = ""
    for i in finalString:
        if i in "1234567890":
            te += i
    te = int(te)

    gameDictionary[te] = gameName
    arr.append(te)

arr.sort(reverse=True)

for i in arr:
    #   '{:,}'.format(value) is what adds the commas - kind of interesting feature
    print (gameDictionary.get(i), " ------ ", '{:,}'.format(i))


for i in range(3):
    print ("")
