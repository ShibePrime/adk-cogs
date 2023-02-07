import re
import requests
import json
import discord
from redbot.core import commands

class Flight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.flight_data_cache = {}

    @commands.command()
    async def flight(self, ctx, *, words: str):
        # Get the flight number from the message
        flight_number = re.search(r'\d+', words).group()

        # Check if flight data is in cache
        if flight_number in self.flight_data_cache:
            flight_data = self.flight_data_cache[flight_number]
        else:
            # Flightradar24 API endpoint
            url = "https://data-live.flightradar24.com/zones/fcgi/feed.js"

            try:
                # Make a GET request to the API endpoint
                response = requests.get(url)
                # Raise an exception if the request was not successful
                response.raise_for_status()
                # Parse the JSON data from the response
                data = json.loads(response.text)
                # Get the flight data from the json object
                flight_data = data[flight_number]
                # Store flight data in cache
                self.flight_data_cache[flight_number] = flight_data
            except requests.exceptions.HTTPError as e:
                return await ctx.send(f"Error retrieving flight information: {e}")
            except json.decoder.JSONDecodeError as e:
                return await ctx.send(f"Error parsing flight information: {e}")

        # Get the flight status
        flight_status = flight_data.get('status', 'Unknown')
        # Get the flight origin
        flight_origin = flight_data.get('origin', {}).get('airport', 'Unknown')
        # Get the flight destination
        flight_destination = flight_data.get('destination', {}).get('airport', 'Unknown')
        # Get the flight aircraft
        flight_aircraft = flight_data.get('aircraft', {}).get('type', 'Unknown')
        # Get the flight airline
        flight_airline = flight_data.get('airline', {}).get('name', 'Unknown')

        # Put it all in a Discord embed and send it
        embed = discord.Embed(title="Flight Info", description="Flight Information", color=0xeee657)
        embed.add_field(name="Flight Number", value=flight_number, inline=False)
        embed.add_field(name="Flight Status", value=flight_status, inline=False)
        embed.add_field(name="Flight Origin", value=flight_origin, inline=False)
        embed.add_field(name="Flight Destination", value=flight_destination, inline=False)
        embed.add_field(name="Flight Aircraft", value=flight_aircraft, inline=False)
        embed.add_field(name="Flight Airline", value=flight_airline, inline=False)
        await ctx.send(embed=embed)
