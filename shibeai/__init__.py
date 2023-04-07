from .shibe_ai import ShibeAI


def setup(bot):
    bot.add_cog(ShibeAI(bot))
