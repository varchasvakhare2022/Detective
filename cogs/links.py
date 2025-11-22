import inspect
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

class Link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='links')
    async def links(self, interaction: Interaction):
        """Vote and Support"""

        embed = discord.Embed(
            title=f"All important links given below -",
            description = inspect.cleandoc(
                f"""
                **Vote links -**
                •❯ [Top.gg](https://top.gg/bot/872002294219157534/vote)
                •❯ [DBL](https://discordbotlist.com/bots/detective/upvote)
                •❯ [Discords.com](https://discords.com/bots/bot/872002294219157534/vote)

                **Support links -**
                •❯ [Support Server](https://discord.gg/YjPUyP4q2J)
                •❯ [Bot Invite](https://discord.com/api/oauth2/authorize?client_id=872002294219157534&permissions=140123778112&scope=bot%20applications.commands)
                """
            ),
            color=0x9C84EF
        )

        await interaction.response.send_message (embed=embed)

async def setup(bot):
    await bot.add_cog(Link(bot))