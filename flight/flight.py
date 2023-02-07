from redbot.core import commands
from FlightRadar24.api import FlightRadar24API

class Flight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fr_api = FlightRadar24API()

    @commands.command()
    async def flight(self, ctx, *, flight_id: str):
        flight = self.fr_api.get_flight(flight_id)
        if not flight:
            await ctx.send("Flight not found.")
            return

        details = self.fr_api.get_flight_details(flight.id)
        flight.set_flight_details(details)

        embed = discord.Embed(title=f"Flight Info for Flight {flight.id}", color=0xeee657)
        embed.add_field(name="Aircraft", value=flight.aircraft_name, inline=False)
        embed.add_field(name="Airline", value=flight.airline_name, inline=False)
        embed.add_field(name="From", value=flight.origin_airport_name, inline=False)
        embed.add_field(name="To", value=flight.destination_airport_name, inline=False)
        embed.add_field(name="Status", value=flight.status, inline=False)
        await ctx.send(embed=embed)