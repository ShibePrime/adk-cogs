from redbot.core import commands

class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        with open(r"~\home\pi\notes.txt", "w") as f:
            f.write(words + "\n")
        await ctx.send("Note written.")

def setup(bot):
    bot.add_cog(WriteNote(bot))