from redbot.core import commands

from .shibeai import shibeai


def setup(bot):
    bot.add_cog(shibeai(bot))
