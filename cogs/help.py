from typing import Optional
import textwrap
import re
import traceback
import io
import contextlib
import os
import random
import json
import inspect

import discord
from discord import (
    app_commands,
    Interaction,
    ui,
    TextStyle
)
from discord.ext import commands
import import_expression

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="help"
    )
    async def help(self, interaction: Interaction) -> None:
        """Help command"""

        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        
        embed = discord.Embed(
            title = f"Help",
            description = inspect.cleandoc(
                f"""
                Hy, I'm {self.bot.user.name}!
                You can have a look at my commands below.
                For further help, join my [server](https://discord.gg/YjPUyP4q2J).
                """
            )
        )
        embed.set_author(
            name = self.bot.user.name,
            icon_url = self.bot.user.display_avatar.url
        )
        embed.add_field(
            name='General',
            value = inspect.cleandoc(
                f"""
                ```
                Help
                Links
                Stats
                

                 
                ```
                """
            ),
            inline=True
        )
        embed.add_field(
            name='Games',
            value = inspect.cleandoc(
                f"""
                ```
                Connect4
                Dare
                Never Have I Ever
                This Or That
                Truth
                Tic Tac Toe
                ```
                """
            ),
            inline=True
        )

        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Help(bot))