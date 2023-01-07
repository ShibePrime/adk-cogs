from redbot.core import commands
import subprocess

# Mount the NFS share
subprocess.run(['mount', '-o', 'bind', 'pi-deskscreen:/data/compose/mounts/modules/MMM-HTMLSnippet', '/mnt'])
class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        # Get the user's name and avatar image link
        user_name = ctx.message.author.name
        user_avatar_url = ctx.message.author.avatar_url

        # Write the user's name, avatar image link wrapped in <img> HTML tags, and words to the file
        with open(r"/mnt/notes.txt", "w") as f:
            f.write(f"{user_name} <img src='{user_avatar_url}'>: {words}\n")
        await ctx.send("Note written.")