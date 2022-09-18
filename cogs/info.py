from typing import Optional
import textwrap
import re
import traceback
import io
import contextlib
import os
import random
import json

import discord
from discord import (
    app_commands,
    Interaction,
    ui,
    TextStyle
)
from discord.ext import commands
import import_expression

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='stats')
    async def neverhaveiever(self, interaction: Interaction):
        """Get statistics of the bot"""

        view = discord.ui.View()
        item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Invite Me", url="https://discord.com/api/oauth2/authorize?client_id=872002294219157534&permissions=8&scope=bot%20applications.commands")
        item1 = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Community Server", url="https://discord.gg/YjPUyP4q2J")
        #item2 = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Documentation", url="https://discord.gg/YjPUyP4q2J")
        view.add_item(item=item)
        view.add_item(item=item1)
        #view.add_item(item=item2)
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        embed = discord.Embed(
            title=f"Bot Statistics",
            description = f"__**Developers**__\n・[varchasvkhare#6684](https://discordapp.com/users/868465221373665351)\n・[BADxDEVIL#3385](https://discordapp.com/users/748552378504052878)\n・[invalid-user#1119](https://discordapp.com/users/714731543309844561)\n\n__**Presence**__\n・Latency - {str(round(self.bot.latency * 1000))}ms\n・Shard - {interaction.guild.shard_id}\n・Servers - {servers}\n・Users - {members}",
            color=0x9C84EF
        )

        await interaction.response.send_message (embed=embed, ephemeral = True, view = view)

async def setup(bot):
    await bot.add_cog(Info(bot))