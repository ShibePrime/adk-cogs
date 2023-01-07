from redbot.core import commands

class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        with open(r"/home/pi/notes.txt", "w") as f:
            f.write(words + "\n")
        await ctx.send("Note written.")

    @commands.command()
    async def readnote(self, ctx):
        try:
            with open(r"/home/pi/notes.txt", "r") as f:
                notes = f.read()
                if not notes:
                    await ctx.send("No notes have been written.")
                else:
                    await ctx.send(notes)
        except FileNotFoundError:
            await ctx.send("No notes have been written.")