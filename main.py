
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DC_TOKEN")
prefix = os.getenv("Prefix")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix , intents=intents)
bot.remove_command('help')
owner_id = [573152498953617409]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for filen in os.listdir('./cmds'):
        if filen.endswith('.py'):
            await bot.load_extension(f'cmds.{filen[:-3]}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass

@bot.command()
async def load(ctx, extentios):
    if ctx.message.author.id in owner_id:
        await bot.load_extension(f'cmds.{extentios}')
        await ctx.message.delete()
        print(f'載入 {extentios}')

@bot.command()
async def unload(ctx, extentios):
    if ctx.message.author.id in owner_id:
        await bot.unload_extension(f'cmds.{extentios}')
        await ctx.message.delete()
        print(f'卸載 {extentios}')
        
@bot.command()
async def reload(ctx, extentios):
    if ctx.message.author.id in owner_id:
        await bot.reload_extension(f'cmds.{extentios}')
        await ctx.message.delete()
        print(f'重新啟動 {extentios}')

bot.run(TOKEN)
