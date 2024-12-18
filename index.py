import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("DC_TOKEN")
prefix = os.getenv("Prefix")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix , intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def awa(ctx):
    await ctx.send("!awa")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass
@bot.command()
async def userinfo(ctx):
    id = ctx.author.id
    name = ctx.author.name
    await ctx.reply(f'使用者 : {id}\n使用者名稱 : {name}')

@bot.command()
async def embed(ctx):
    now = datetime.now()
    embed = discord.Embed(color=0x86ff00, timestamp=now)
    embed.add_field(name=f"ID",value=f'{ctx.author.id}',inline=False)
    embed.add_field(name=f"名稱",value=f"{ctx.author.name}",inline=False)
    embed.set_footer(text='awa')
    await ctx.send(embed=embed)

bot.run(TOKEN)