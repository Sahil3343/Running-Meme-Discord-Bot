import discord
from discord.ext import commands
import random
import os
from keep_alive import keep_alive

links =["https://media.giphy.com/media/JROc42V1xd649kQqnS/giphy.gif", "https://media.giphy.com/media/3o7ZetIsjtbkgNE1I4/giphy.gif", "https://media.giphy.com/media/945jGDodvZCDe/giphy.gif", "https://media.giphy.com/media/H7qvJpLs4TuwBZ9Ymz/giphy.gif", "https://media.giphy.com/media/qYHlTos5CDu0/giphy.gif", "https://media.giphy.com/media/AEsUINFBsRVN6/giphy.gif", "https://media.giphy.com/media/BpDYodBlBXFIs/giphy.gif", "https://media.giphy.com/media/CjGETXVO1jvS9CfFXx/giphy.gif", "https://media.giphy.com/media/ES3VsZar8fg0o/giphy.gif", "https://media.giphy.com/media/EBWnbHV4BH6rC/giphy.gif", "https://media.giphy.com/media/tW57081Logeic/giphy.gif", "https://media.giphy.com/media/69o9jvfat2RfPWOAp1/giphy.gif", "https://media.giphy.com/media/83quRizn5dFvi/giphy.gif", "https://media.giphy.com/media/Lnuq0IFLhyt6v61Qeo/giphy.gif", "https://media.giphy.com/media/vvVP18ZqYMp4B4Yda3/giphy.gif", "https://media.giphy.com/media/SsMutP5X51TdzL5hOC/giphy.gif", "https://media.giphy.com/media/ZY3KxyP8Lnu2rPL4CH/giphy.gif", "https://media.giphy.com/media/TmVHwsPAveJiM/giphy.gif", "https://media.giphy.com/media/4DSvnh7VCh680/giphy.gif", "https://media.giphy.com/media/2sYdt7LAAVHYvrAYV5/giphy.gif", "https://media.giphy.com/media/ZgSwNQu8Dsrg3jTSoM/giphy.gif", "https://media.giphy.com/media/sVXtRrWWMsA2k/giphy.gif", "https://media.giphy.com/media/9u57Qx5EaSg3oB9yjZ/giphy.gif", "https://media.giphy.com/media/XgMJ9rR5W2MRcsUOcZ/giphy.gif", "https://media.giphy.com/media/l4Jz6pNKSvEuB5xYc/giphy.gif", "https://media.giphy.com/media/6Z3D5t31ZdoNW/giphy.gif", "https://media.giphy.com/media/XGn6xLsliW1dLnQY92/giphy.gif", "https://media.giphy.com/media/xUPGcKaUhFeHMGW7dK/giphy.gif", "https://media.giphy.com/media/f4bQadlNq3RvdSKx04/giphy.gif", "https://media.giphy.com/media/QKUTD5lAgpgrSHpbMB/giphy.gif", "https://media.giphy.com/media/7kn27lnYSAE9O/giphy.gif", "https://media.giphy.com/media/HNJHYpKqtuqRy/giphy.gif", "https://media.giphy.com/media/Sux3kje9eOx1e/giphy.gif", "https://media.giphy.com/media/QWi5gPXEHIxkk/giphy.gif", "https://media.giphy.com/media/116n6kcHaFbw3e/giphy.gif", "https://media.giphy.com/media/3o7TKR1b2X2JqJ6JDW/giphy.gif", "https://media.giphy.com/media/3owypnv1Med6YoCbcs/giphy.gif", "https://media.giphy.com/media/3oGRFKJ8Ea3hKkLRyE/giphy.gif", "https://media.giphy.com/media/JhOAQxvBafrIA/giphy.gif", "https://media.giphy.com/media/OOZLyBA9Euq2I/giphy.gif", "https://media.giphy.com/media/1vY8RboCYg4wM/giphy.gif", "https://media.giphy.com/media/kEKcOWl8RMLde/giphy.gif", "https://media.giphy.com/media/3o7TKxA1pHqzA4k9B6/giphy.gif", "https://media.giphy.com/media/ZXOvxtCkqxUxa/giphy.gif", "https://media.giphy.com/media/10jUpXZZDBITyo/giphy.gif", "https://media.giphy.com/media/NRkK2XCXPd2Du/giphy.gif", "https://media.giphy.com/media/13sozYO4hmSMUw/giphy.gif", "https://media.giphy.com/media/pgiu2F8RERX5C/giphy.gif", "https://media.giphy.com/media/ri8Kb9LOe5Nza/giphy.gif", "https://media.giphy.com/media/VgIH2PYoS0ICY/giphy.gif", "https://media.giphy.com/media/Q4ah52WMLegA8/giphy.gif", "https://media.giphy.com/media/24cbiZwzSW8Kc/giphy.gif", "https://media.giphy.com/media/10frqodBZhy0Zq/giphy.gif", "https://media.giphy.com/media/JRlqKEzTDKci5JPcaL/giphy.gif", "https://media.giphy.com/media/QA8fyvovxbkqc/giphy.gif", "https://media.giphy.com/media/9j53JL2MRdzaw/giphy.gif", "https://media.giphy.com/media/l0HlIkXQeWCPhLFM4/giphy.gif", "https://media.giphy.com/media/bEXBQ3dR5OLyE/giphy.gif", "https://media.giphy.com/media/nJZxhesBFKbCw/giphy.gif", "https://media.giphy.com/media/9VpA8OFO3uyUhualCM/giphy.gif", "https://media.giphy.com/media/fV6kUfjHFJJ16/giphy.gif", "https://media.giphy.com/media/l1J9wFxJPNGwolLuE/giphy.gif", "https://media.giphy.com/media/26ybuMeyTrbd04idi/giphy.gif", "https://media.giphy.com/media/1q1XMWGUdpKnK/giphy.gif", "https://media.giphy.com/media/DGiZfWmc0HWms/giphy.gif", "https://media.giphy.com/media/WqmYGa2LjQlTG/giphy.gif", "https://media.giphy.com/media/vuDRxYtmijozu/giphy.gif", "https://media.giphy.com/media/yOZ5hsdLjAp8Y/giphy.gif", "https://media.giphy.com/media/Svz9ASkbnKW1W/giphy.gif", "https://media.giphy.com/media/3ohfFmhGWLITBQvldu/giphy.gif", "https://media.giphy.com/media/FV8nzuvp7pcHu/giphy.gif", "https://media.giphy.com/media/zlxZM9D0T6lOg/giphy.gif", "https://media.giphy.com/media/EIrCLqfb4z3TJiV16v/giphy.gif", "https://media.giphy.com/media/IT4fLZjxyDu24/giphy.gif", ]

bot = commands.Bot(command_prefix = "+")

@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hello! I am the Running Meme Bot that has been created by the one and only Boltz! I am here to provide you with memes!")

@bot.command(pass_context=True)
async def meme(ctx):
  random_meme = random.choice(links)
  embed = discord.Embed(
      title = "Here is your meme...",
  )

  embed.set_footer(text=f"Requested by {ctx.author.name}")
  embed.set_image(url=random_meme)

  await ctx.send(embed=embed)

keep_alive()
bot.run(os.getenv('TOKEN'), bot=True, reconnect=True)