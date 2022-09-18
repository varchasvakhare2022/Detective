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
	"ThisOrThats": ('Pen or Pencil', 
    'Dog or Cat', 
    'Netflix or YouTube', 
    'Call or Text', 
    'Toast or Eggs', 
    'Cardio or Weights', 
    'Facebook or Twitter', 
    'Music or Podcasts', 
    'iOS or Android', 
    'Pop or Indie', 
    'Cake or Pie', 
    'Swimming or Sunbathing', 
    'High-tech or Low-tech', 
    'Rich Friend or Loyal Friend', 
    'Football or Basketball', 
    'Work Hard or Play Hard', 
    'Jogging or Hiking', 
    'Bath or Shower', 
    'Sneakers or Sandals', 
    'Glasses or Contacts', 
    'Hamburger or Taco', 
    'Couch or Recliner', 
    'Shopping: Online or In-Person', 
    'Receive: Email or Letter', 
    'Passenger or Driver', 
    'Tablet or Computer', 
    'Blue or Red', 
    'Money or Time', 
    'Amusement Park or Beach', 
    'Coke or Pepsi', 
    'Blinds or Curtain', 
    'Train or Plane', 
    'Iced Coffee or Hot Coffee', 
    'Fruits or Vegetables', 
    'Save or Spend', 
    'TV or Book', 
    'Ocean or Mountains', 
    'City or Countryside', 
    'Horror or Comedy', 
    'Winter or Summer', 
    'Mac or PC', 
    'Console Gaming or PC Gaming', 
    'Soup or Sandwich', 
    'Card Game or Board Game', 
    'Traditional Art or Digital Art', 
    'Beer or Wine', 
    'Dine In or Delivery', 
    'Sweater or Hoodie', 
    'Comic Book or Comic Strips', 
    'Motorcycle or Bicycle', 
    'Book or E-Book', 
    'Ninjas or Pirates', 
    'Movie or TV Show', 
    'Cookies or Cake', 
    'Pop or Rock', 
    'Pancakes or Waffles', 
    'Morning or Evening', 
    'Day or Night', 
    'Library or Museum', 
    'French or Spanish', 
    'Love or Money', 
    'Chocolate or Vanilla', 
    'Tea or Coffee', 
    'Rain or Snow', 
    'Car or Motorcycle', 
    'Boat or Plane', 
    'Painting or Drawing', 
    'Reading or Writing', 
    'Singing or Dancing', 
    'Flowers or Trees', 
    'Superman or Batman', 
    'Milk or Juice', 
    'Gold or Silver', 
    "Music: 50's or 80's", 
    'Google or Bing', 
    'Frozen Yogurt or Ice Cream', 
    'Eyes: Blue or Green', 
    'Witches or Wizards', 
    'Fire or Ice', 
    'Hair: Straight or Curly', 
    'Vegetarian or Non-Vegetarian', 
    'Pandas or Whales', 
    'Roses or Daisies', 
    'Circles or Squares', 
    'Piercings or Tattoos', 
    'Sandals or Sneakers', 
    'Apples or Oranges', 
    'Weird or Crazy', 
    'Skates or Bike', 
    'Skiing or Snowboarding', 
    'Sports: Watch or Play', 
    'Swim: Pool or Sea', 
    'Sweet or Salty', 
    'Breakfast or Dinner', 
    'Whatsapp or Telegram', 
    'Watch: Digital or Analog', 
    'Freedom or Hope', 
    'Snow White or Cinderella', 
    'Sitting or Standing', 
    'Comedy or Drama', 
    'Hot or Cold', 
    'Pasta or Pizza', 
    'Family or Friends', 
    'Scooby Doo or Tom and Jerry', 
    'Cuddle or Sleep', 
    'Telepathy or Teleportation', 
    'Mansion or Cabin', 
    'Rap or Rock', 
    'Hair: Long or Short', 
    'Serious or Funny', 
    'Hot or Pretty', 
    'Hugs or Kisses', 
    'Mom or Dad', 
    'Houseboat or Yacht', 
    'Fact or Fiction', 
    'Soap: Liquid or Bar', 
    'Higher Studies or Work', 
    'Rain or Sunshine', 
    'Death: Instant or Prolonged', 
    'Work Sector: Government or Private', 
    'Thunderstorm or Snowstorm', 
    'Doctor or Engineer', 
    'Wax or Shave', 
    'Boss or Worker', 
    'Fast or Slow', 
    'Doctor or Patient', 
    'Introvert or Extrovert', 
    'Cry or Scream', 
    'Alcohol or Weed', 
    'Formals or Casuals', 
    'Work: From Home or Commute', 
    'Work: Alone or In a Team', 
    'Trip or Staycation', 
    'Gifts: Handmade or Bought', 
    'Modern or Rustic', 
    'Extravagant or Minimalist', 
    'Comfort or Style', 
    'Sinful or Righteous', 
    'Festivals: Art or Music', 
    'Hurt or Dead', 
    'Forest or Beach', 
    'Cable or Satelite', 
    'Truth or Lies', 
    'Strange or Crazy', 
    'Concerts or Movies', 
    'Abs or Chest', 
    'Smile or Eyes', 
    'Cycle or Walk', 
    'Chandelier or Lamp', 
    'Country: Own or Abroad', 
    'Evil or Good', 
    'Antique or New', 
    'Kids: Twins or Single', 
    'Shower: Morning or Evening', 
    'Mountain or Hills', 
    'Marvel or DC', 
    'Lost or Found', 
    'Carnivore or Herbivore', 
    'Cold or Flu', 
    'Stories: Horror or Mystery', 
    'Carnival or Circus', 
    'Camping or Safari', 
    'Fishing or Kayaking', 
    'Skydive or Bungee Jump', 
    'Park: Theme or Water', 
    'Bowling or Mini-Golf', 
    'Spa or Gym', 
    'Simpsons or Family Guy', 
    'Drunk or Sober', 
    'Indoor or Outdoor', 
    'Sunrise or Sunset', 
    'Beard or Clean-Shaved', 
    'Sports or Video-Games', 
    'Image or Video', 
    'Dishes or Laundry', 
    'Spiders or Snakes', 
    'Rap Music or Country Music', 
    'Sneeze or Hiccup', 
    'Time Travel or Space Travel', 
    'Comfortable Silence or Incredible Conversation', 
    'Son or Daughter', 
    'Fame or Money', 
    'Albert Einstein or Isaac Newton', 
    'Ancient Greece or Ancient Rome', 
    'Apartment or House', 
    'Aquarium or Zoo', 
    'Cyborg or Human', 
    'Dragon or Unicorn', 
    'Hero or Villian', 
    'Ninja or Samurai', 
    'Ruler or Follower', 
    'Fly or Teleport', 
    'Broke or Dead', 
    'Loved or Feared', 
    'Wise or Intelligent', 
    'Bill Gates or Mark Zuckerberg', 
    'Eggs: Boiled or Fried', 
    'Brush or Comb', 
    'Burgers or Pizzas', 
    'Cardio or Weights', 
    'Cambridge or Harvard', 
    'Flats or Heels', 
    'Give or Receive', 
    'Harry Potter or Hunger Games', 
    'Instagram or Snapchat', 
    'The Avengers or The Justice League', 
    'Mafia or Street Gang', 
    'Kill or Be Killed', 
    'Linux or Windows', 
    'London or Paris', 
    'Nails: Long or Short', 
    'Overdressed or Underdressed', 
    'Piano or Guitar', 
    'Rent or Buy', 
    'Speed or Precision', 
    'Autumn or Spring', 
    'Star Wars or Star Trek', 
    'Sun or Moon', 
    'Talk or Listen', 
    'Taj Mahal or Eiffel Tower', 
    'Call: Video or Audio', 
    'Truth or Dare', 
    'Rome or Paris', 
    'Tesla or SpaceX', 
    'Zombie Outbreak or Alien Invasion')   
}


class ThisOrThat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name='thisorthat')
    async def thisorthat(self, interaction: Interaction):
        """Get a ThisOrThat"""

        response = random.choice(database['ThisOrThats'])

        embed = discord.Embed()

        message = []

        if ':' in response: 
            split = response.split(':')
            embed.title = split[0]
            tot = split[1].strip()
        else:
            tot = response
        
        embed.description = (
            f"🔴 {tot.replace(' or ', ' **OR** ')} 🔵"
        )

        await interaction.response.send_message (embed=embed)

async def setup(bot):
    await bot.add_cog(ThisOrThat(bot))