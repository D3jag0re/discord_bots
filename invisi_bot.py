import discord
from discord.ext import commands 

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready(): 
    print("Bot is ready.")

@client.command()
async def ping(ctx): 
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


client.run('OTM0MTA2MDI2NDIzMjQyODMy.YerQBw.H4W56P8jbBbTnF4RJmW8uGzCS3I') 