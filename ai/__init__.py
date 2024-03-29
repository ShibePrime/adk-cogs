from .ai import AICommand  # Corrected to import the AICommand class

def setup(bot):
    bot.add_cog(AICommand(bot))  # Instantiate and add the cog to the bot
