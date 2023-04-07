from redbot.core import commands

from .shibeai import ShibeAI


def setup(bot):
    bot.add_cog(ShibeAI(bot))
