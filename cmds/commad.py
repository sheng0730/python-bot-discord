from discord import Embed
from discord.ext import commands
from datetime import datetime

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def embed(self, ctx):
        now = datetime.now()
        embed = Embed(color=0x86ff00, timestamp=now , title='title' , url='https://cdn.discordapp.com/emojis/831529287689044098.webp?size=96')
        embed.add_field(name=f"ID",value=f'{ctx.author.id}',inline=False)
        embed.add_field(name=f"名稱",value=f"{ctx.author.name}",inline=False)
        embed.set_author(name="author",url='http://118.150.52.23:5001',icon_url='https://cdn.discordapp.com/emojis/1058369420361220147.webp?size=96')
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_image(url='https://cdn.discordapp.com/attachments/1318629617451663474/1318998703712763904/val_batch1_pred.jpg?ex=67645cc4&is=67630b44&hm=3c2cfe583563a0a90a995743544046cb43101b7156198f8c309dcf9fe46a1939&')
        embed.set_footer(text='awa',icon_url='https://cdn.discordapp.com/emojis/991993847448092672.webp?size=96')
        
        await ctx.send(embed=embed)
    
    @commands.command()
    async def userinfo(self, ctx):
        id = ctx.author.id
        name = ctx.author.name
        await ctx.reply(f'使用者 : {id}\n使用者名稱 : {name}')

async def setup(bot):
    await bot.add_cog(Cog_Extension(bot))