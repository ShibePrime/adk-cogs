from redbot.core import commands

from .flight import flight

def setup(bot):
    bot.add_cog(flight(bot))