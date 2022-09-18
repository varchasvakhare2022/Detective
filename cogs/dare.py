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
	"dares": ('Act like a monkey and record a video of it.', 
    'Act like you do not understand human language until your next turn (come up with your own language).', 
    'Act like your favourite Disney character for the rest of the game.', 
    'Close your eyes and send a blind text to a random person.', 
    'Compose a poem on the spot based on something the group comes up with.', 
    'Everything you say for the next 5 minutes has to rhyme.', 
    "Everything you say for the next 5 minutes must not contain the words: 'but', 'a', 'the', 'or'", 
    'Make a freestyle rap song about each person in the group', 
    "Make a poem using the words 'orange' and 'moose'.", 
    "Make a poem using the words 'pineapple' and 'apple'.", 
    "Make a poem using the words 'goose' and 'peanuts'.", 
    'Make up a poem about the colour blue.', 
    'Make up a story about a random person in the group.', 
    "Post 'I love English!' on a social media.", 
    'Record a video of you dancing, but without music.', 
    'Record a video of you playing the air drums to a song of your choice.', 
    'Record a video of you playing the air guitar to a song of your choice.', 
    'Record an impression of your favourite celebrity.', 
    'Record an impression of your favourite animal.', 
    'Record your best evil laugh; as loud as you can.', 
    'Record your best president impression.', 
    'Record yourself saying the alphabet backwards.', 
    'Record yourself singing "Twinkle Twinkle, Little Star" while beat boxing.', 
    'Record yourself singing the alphabet without moving your mouth.', 
    'Record yourself talking about your favourite food in a russian accent.', 
    'Say "ya heard meh" after everything you say for the next 5 minutes.', 
    'Say "you know what am sayin" after everything you say for the next 5 minutes.',
    'Text someone asking them if they believe in aliens, send a screenshot of the conversation.', 
    'Send an email to one of your teachers, telling them about how your day is going and take a screenshot.', 
    'Send an unsolicited text message to one of your friends, telling them about how your day is going and take a screenshot.', 
    'Send the last photo you took with your phone camera.', 
    'Send the last screenshot you took on your phone.', 
    'Send the most embarrassing photo on your phone.', 
    'Send the oldest selfie on your phone.', 
    'Send a screenshot of your most recent google search history.', 
    'Send a selfie of you making a funny face.', 
    'Set your phone language to Chinese for the next 10 minutes.', 
    'Show the last three people you texted and what the messages said.', 
    'Text your crush and tell them how much you like them.', 
    'Use the letters of the name of another player to describe them (ex. SAM : S = Silly ; A = Attractive ; M = Merry)', 
    'Yell out the first word that comes to your mind, and record it.'),
    
    "dare_r_rated": ('Do your best fake "O" while looking the person to the left of you in the eye.', 
    'Have someone blindfold you, and then have everyone in the group kiss you on the cheek. You have to either say which one is your partner, and then kiss them on the lips, OR you have to choose one person that you want to kiss on the lips.', 
    'With your eyes closed and the other person or people standing across from you in the room, walk with your hands out. You have to kiss the first person you touch exactly where you touch them.', 
    'You have to leave an R-rated voicemail for an ex.', 
    'Someone has to lick peanut butter, chocolate sauce, or whipped cream off your finger, cheek, or somewhere of their choice.', 
    'Someone feeds you M&Ms or other small chocolate candy, and you have to say, "Thank you, Daddy," after each one.', 
    "If there's a pool, you have to go skinny dipping, and you have to choose one buddy to go with you.", 
    "You're in school and you've been a bad student. For the next round, you're in time-out on someone's lap.", 
    "Someone goes onto your Amazon account and buys a special toy for you that's $20 or less.",
    'Take a picture of a tampon and post it on Instagram.', 
    'Put on a pair of heels and take off your pants (not in that order).', 
    'Grab a broom and do your sexiest dance with it.', 
    'Touch tongues with someone.', 
    'Shave one of your arms.', 
    'Demonstrate your best technique for you-know-what on your finger.', 
    'Do as many squats as you can. On the front lawn.', 
    'You have to entirely redress yourself with whatever you find in the kitchen.', 
    'Fake it for 10 seconds.', 
    "If you're at your home, pretend you're an auctioneer auctioning off your favorite grown-up toy, giving details about why you like it. If you're at someone else's home, use something that looks kind of like it.", 
    'Use your butt to give a speech to the group about gas prices (or something else of your choosing).', 
    'Do your best sexy crawl.', 
    'Give a detailed presentation on how you woo a lover in the style of a TED Talk.', 
    'Give your junk a name and then give a stream-of-consciousness speech from its perspective.', 
    'Imitate the sounds of both sides of your most recent romantic encounter.', 
    "Try to hit on someone in this group like you're at a bar.", 
    'Make as many different sounds with your lips as you can.', 
    'Make as many different fart sounds as you can.', 
    "You have to say, \"I'm just a silly boy,\" and slap yourself gently on the face 20 times.", 
    'Go hide somewhere in the house until the next round starts. No one is going to come find you, but you must remain hidden.', 
    'Cook two bags of popcorn. Eat all of it as fast as you can, but in the sexiest way possible.', 
    'Take off your shirt and pants, lay down on the ground, and act like a dolphin that’s gotten stranded on land for one minute.', 
    "Pretend like you're making sweet, sweet, love to the couch for one and a half minutes.", 
    'Pick up a random book and read it in the most seductive voice you can manage.', 
    'Demonstrate to the room how to put a condom on using a banana.', 
    'Make out with your hand to “The Song That Never Ends” (look it up on YouTube).', 
    'Put in your headphones and put on your favorite song and dance to it.', 
    'Someone gets to draw something on your face (with just a pen, not a permanent marker).', 
    'You have to hold a mouthful of water in your mouth until the round is over.', 
    "Slap your butt and say, \"I've been bad, bad, bad, bad, bad, bad, bad, bad, bad, naughty!\"", 
    'Put on a dance song and grind with a pillow for one minute.', 
    'Feed someone almonds using just your mouth.')   
}


class Dare(commands.GroupCog, group_name='dare'):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='normal')
    async def normal(self, interaction: Interaction):
        """Get a dare"""

        await interaction.response.send_message(random.choice(database['dares']))

    @app_commands.command(name='r-rated')
    async def rrated(self, interaction: Interaction):
        """Get a dare (r rated)"""

        await interaction.response.send_message(random.choice(database['dare_r_rated']))


async def setup(bot):
    await bot.add_cog(Dare(bot))