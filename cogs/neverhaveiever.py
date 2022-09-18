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

database = {
	"Never": ('kissed an animal.', 
    'kissed a person of the same sex.', 
    'kissed my best friend.', 
    'cheated on a test.', 
    'ridden the bus without paying fare.', 
    'fallen asleep during a class.', 
    'stolen something.', 
    'bitten a toenail.', 
    'bragged about something I have not done.', 
    'spied on my neighbors.', 
    'made fun of someone.', 
    'stolen something with a higher value than $10.', 
    'bet on something, lost and refused to keep up with my side of the promise.', 
    'faked an illness to avoid school.', 
    "grabbed the wrong person's hand.", 
    'stuck gum under a desk.', 
    'refused a kiss.', 
    'peed in a pool.', 
    'eaten food that fell on the floor.', 
    'went to an event uninvited.', 
    'picked my nose in public.', 
    'faked being asleep in front of someone.', 
    "snooped through someone's belongings without them knowing.", 
    'picked up a hitchhiker.',
    'hitchhiked.', 
    'got into a physical altercation with a good friend.', 
    "looked through someone's phone without their permission.", 
    "gone through someone's chats without their permission.", 
    "taken money that didn't belong to me.",
    'stayed up for 48 hours straight.', 
    'been suspended from school.', 
    'tried cutting my own hair.', 
    'went to the hospital for something embarrassing.', 
    "taken the blame for something I've never done.", 
    'broken a bone.', 
    'cried in front of a crush.', 
    'dyed my hair.', 
    'farted in front of someone I liked.', 
    'accidentally sharted.', 
    'forgotten the punchline of a joke.', 
    'sang a song out loud and messed the lyrics.', 
    'walked in on someone in the bathroom.', 
    'had someone walk in on me in the bathroom.', 
    'sent a text to the wrong person.', 
    'tried to pass a silent fart, but it came out loud instead.', 
    'tripped in public.', 
    'wet the bed after childhood.', 
    'accidentally pooped my pants.', 
    'attempted martial arts moves while by myself.', 
    'drove over a curb.', 
    'mistaken a man for a women or vice versa.', 
    'called the wrong person, but pretended I meant to call them.', 
    'gone into the wrong restroom.', 
    "had diarrhea at a friend's house.", 
    'broken a piece of furniture by sitting on it.', 
    'arrived somewhere late and had everyone staring at me.', 
    'had food stuck in my teeth all day', 
    'walked around with my zipper down.', 
    "bought a children's toy for myself.", 
    'recorded video of myself singing or dancing.', 
    'been caught picking my nose.', 
    'gotten something stuck in my nose.', 
    'greeted someone I thought was someone else.', 
    'gave myself a bad haircut.', 
    'been told I had bad breath.', 
    'screamed because of a bug.', 
    "played on my phone, trying to look like I'm doing something important.", 
    'practiced public speaking in the mirror.', 
    'had dandruff.', 
    'listened to Justin Bieber.', 
    'just looked at myself naked in the mirror.',
    "smiled at someone when I realize I wasn't listening to what they were saying.", 
    'tried to impress a crush by seeming knowledgeable about things they liked.', 
    'refreshed over and over to see if I have any new messages.', 
    'pretended to text while secretly taking selfies.', 
    'imagined my life as a sitcom and who would play me.', 
    'dressed as the opposite sex.', 
    'cried during a Pixar movie.', 
    "'cleaned up' by piling everything into a closet.", 
    'sung karaoke.', 
    'pretended to know a stranger.', 
    "said 'excuse me' when there was no one around.", 
    'scared myself in a mirror.', 
    'missed a high five.', 
    'sang in the shower.', 
    'blamed farts on an animal.', 
    'slept in regular clothing.', 
    "pretended to laugh at a joke I didn't get.", 
    'been scared of clowns.', 
    'played Candy Crush.', 
    'made a duck face when taking a selfie.', 
    'actually laughed out loud when typing "LOL".', 
    'reread an email immediately after sending it.', 
    "daydreamed about being on a talk show and what I'd talk about.", 
    'Googled my own name to see what comes up.', 
    'sat in the shower.', 
    'tried something I saw on Pinterest.', 
    'ugly cried for no reason.', 
    'creeped on someone I just met on social media.', 
    'thought about how a loved one could identify me if my face was horribly disfigured in an accident.', 
    'thrown up in public.', 
    'stuck a gum under a table.', 
    'played Minecraft.', 
    'spent real money on a game or game items.', 
    'played a game over 3,000 hours.', 
    'ridden an animal.', 
    'had the experience of being close to death', 
    'Never have I re-gifted something that was gifted to me', 
    'been out of the country.', 
    'lied in a job interview.', 
    'tried to look at the sun.', 
    'had surgery.', 
    'made a wish at a fountain.', 
    'cut someone in line.', 
    'read a single Harry Potter book.', 
    'been inside of a library.', 
    'lied about my age.', 
    'had a cavity.', 
    'seen Titanic.', 
    'met a celebrity.', 
    'seen snow.', 
    "Googled something so I'd know how to spell it.", 
    'cried in public.',
    'tried to repeat an action scene in the house.', 
    'travelled alone.', 
    'counted the number of electric poles from a moving train.', 
    'lied to my parents about where I was going.', 
    'had to call the cops on someone.', 
    'jumped a fence.', 
    'downloaded music illegally.', 
    'jaywalked.', 
    "shared passwords to services so family or friends didn't have to pay.", 
    'made a fake social media account.', 
    'pretended to be someone else online.', 
    'driven without wearing a seatbelt.', 
    'used my cell phone while driving.', 
    'used medicine that was not prescribed to me.', 
    'gone commando.')   
}


class Never(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='never-have-i-ever')
    async def neverhaveiever(self, interaction: Interaction):
        """Get a nhie"""

        await interaction.response.send_message (random.choice(database['Never']))

async def setup(bot):
    await bot.add_cog(Never(bot))