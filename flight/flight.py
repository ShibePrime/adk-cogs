from redbot.core import commands
import json
import requests
import re


class flight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def flight(self, ctx, *, words: str):
        # flightradar api free endpoint
        url = https://data-live.flightradar24.com/zones/fcgi/feed.js

        # Get the flight number from the message
        flight_number = re.search(r'\d+', words).group()
        # Get the flight data from the API
        response = requests.get(url)
        # Convert the response to a json object
        data = json.loads(response.text)
        # Get the flight data from the json object
        flight_data = data[flight_number]
        # Get the flight status
        flight_status = flight_data['status']
        # Get the flight origin
        flight_origin = flight_data['origin']['airport']
        # Get the flight destination
        flight_destination = flight_data['destination']['airport']
        # Get the flight aircraft
        flight_aircraft = flight_data['aircraft']['type']
        # Get the flight airline
        flight_airline = flight_data['airline']['name']
        #put it all in a discord embed and send it
        embed = discord.Embed(title="Flight Info", description="Flight Information", color=0xeee657)
        embed.add_field(name="Flight Number", value=flight_number, inline=False)
        embed.add_field(name="Flight Status", value=flight_status, inline=False)
        embed.add_field(name="Flight Origin", value=flight_origin, inline=False)
        embed.add_field(name="Flight Destination", value=flight_destination, inline=False)
        embed.add_field(name="Flight Aircraft", value=flight_aircraft, inline=False)
        embed.add_field(name="Flight Airline", value=flight_airline, inline=False)
        await ctx.send(embed=embed)

