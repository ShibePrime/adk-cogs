from redbot.core import commands

from .note import WriteNote

def setup(bot):
    bot.add_cog(WriteNote(bot))