from redbot.core.bot import Red

from .note import note

def setup(bot: Red):
    bot.add_cog(note())
