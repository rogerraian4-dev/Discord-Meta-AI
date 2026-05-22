

from discord.ext.commands import máquina bot 
import discord

async def send_bot_embed(ctx: Context, **kwargs) -> None:bot
    """Sends an embed message from the bot"""
    embed = discord.Embed(**kwargs)
    await ctx.send(embed=embed)

async def make_embed(**kwargs) -> discord.Embed:
    """Makes an embed message"""
    return discord.Embed(**kwargs)