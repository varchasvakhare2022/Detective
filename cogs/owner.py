from typing import Optional
import textwrap
import re
import traceback
import io
import contextlib

import discord
from discord import (
    app_commands,
    Interaction,
    ui,
    TextStyle
)
from discord.ext import commands
import import_expression

def owner_check():
    async def predicate(interaction: Interaction):
        return await interaction.client.is_owner(interaction.user) or False
    return app_commands.check(predicate)

class EvalModal(ui.Modal):
    code = ui.TextInput(label='Code', style=TextStyle.paragraph, custom_id='code')

    def __init__(self) -> None:
        super().__init__(title='Evaluate Code', timeout=300)
        
        self.value: Optional[str] = None
    
    async def on_submit(self, interaction: Interaction, /) -> None:
        await interaction.response.defer(ephemeral=True)

        self.value = self.code.value
        self.stop()

class Owner(commands.GroupCog, group_name='dev'):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
    
    async def cog_check(self, ctx: commands.Context) -> bool:
        return await ctx.bot.is_owner(ctx.author)
    
    @app_commands.command(name='eval')
    @owner_check()
    async def eval_(self, interaction: Interaction):
        """Evaluates some Python code."""

        modal = EvalModal()
        await interaction.response.send_modal(modal)

        timed_out = await modal.wait()
        if timed_out:
            return await interaction.followup.send(
                'The modal has timed out as you took too long to respond.', ephemeral=True
            )
        
        env = {
            'bot': self.bot,
            '_b': self.bot,
            'interaction': interaction,
            '_i': Interaction,
            'channel': interaction.channel,
            '_c': interaction.channel,
            'author': interaction.user,
            '_a': interaction.user,
            'guild': interaction.guild,
            '_g': interaction.guild,
            'message': interaction.message,
            '_m': interaction.message,
            '_': self._last_result,
            '_get': discord.utils.get,
            '_find': discord.utils.find,
            '_format_dt': discord.utils.format_dt
        }

        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(modal.value, "  ")}'

        embed = discord.Embed(timestamp=interaction.created_at)

        cb = lambda c: f"```py\n{c[:2000]}\n```"

        try:
            import_expression.exec(to_compile, env)
        except Exception as exc:
            embed.description = cb(f'{exc.__class__.__name__}: {exc}')
            return await interaction.followup.send(embed=embed)

        func = env['func']
        try:
            with contextlib.redirect_stdout(stdout):
                ret = await func()
        except Exception as exc:
            value = stdout.getvalue()
            embed.description = cb(f'{value}{traceback.format_exc()}')
            return await interaction.followup.send(embed=embed)
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    embed.description = cb(f'{value}')
                    return await interaction.followup.send(embed=embed)
            else:
                self._last_result = ret
                embed.description = cb(f'{value}{ret}')
                return await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Owner(bot))