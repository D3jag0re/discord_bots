import os 

import discord
from discord.ext import commands 
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv('TOKE')

client = commands.Bot(command_prefix = '.')

@client.event 
async def on_ready(): 
    print("Bot is ready.")

#Issue .ping command, bot responds with pong as well as latency in ms.
@client.command()
async def ping(ctx): 
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#8Ball feature. Question is asked, bot responds with one of the responses.
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['But of course.' , 
                 'It is decidedly so.' ,
                 "I don't have a fucking clue." ,
                 'The only thing I truly know is shoegaze sucks' , 
                 'Who cares?' ,
                 'You know what they say: "Forza Forza Forza"' ,
                 'Shut up, weeb.' ,
                 'No.' ,
                 'Whatever.' ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')




client.run(TOKEN) 