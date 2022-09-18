from typing import Optional
import os
import logging

import asyncpg
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()

SLASH_GUILD = discord.Object(id=760134264242700320)

os.environ['JISHAKU_HIDE'] = 'True'
os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'
os.environ['JISHAKU_FORCE_PAGINATOR'] = 'True'
os.environ['JISHAKU_NO_DM_TRACEBACK'] = 'True'

logging.getLogger('discord').setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

class Bot(commands.AutoShardedBot):
    def __init__(self, *, application_id: int, **kwargs) -> None:
        intents = discord.Intents.default()
        #intents.message_content = True

        super().__init__(
            command_prefix='...',
            shard_count=2,
            intents=intents,
            owner_ids={
                868465221373665351, # varch
                748552378504052878, # pandey
                714731543309844561  # invalid
            },
            application_id=application_id,
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                roles=False,
                replied_user=True,
                users=True
            )
        )
    
    @property
    def token(self) -> Optional[str]:
        return os.getenv('BOT_TOKEN')
    
    @tasks.loop(minutes=10)
    async def change_status(self):
        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name='in Maintenance'
            )
        )

    @change_status.before_loop
    async def _before_change_status(self):
        await self.wait_until_ready()

    async def _startup_task(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        extensions = [
            'jishaku',
            *[
                f'cogs.{extension[:-3]}'
                for extension in os.listdir('./cogs')
                if extension.endswith('.py')
            ]
        ]

        for item in extensions:
            try:
                await self.load_extension(item)
            except Exception as exc:
                logging.error(f"Failed to load extension {item}", exc_info=exc)
            else:
                logging.info(f"Loaded extension {item}")

        await self.change_status.start()

    async def setup_hook(self) -> None:
        #self.tree.copy_global_to(guild=SLASH_GUILD)
        #await self.tree.sync(guild=SLASH_GUILD)
        #await self.tree.sync()
        self.loop.create_task(self._startup_task())
        
    def run(self):
        super().run(
            token=self.token,
            reconnect=True,
            log_handler=None
        )
