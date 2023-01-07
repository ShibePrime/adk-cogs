from redbot.core import commands
import json

class AssetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Asset):
            # Convert the Asset object to a dictionary
            return {
                "type": "Asset",
                "value": obj.toString()
            }
        # Let the base class handle other objects
        return json.JSONEncoder.default(self, obj)
class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        # Get the user's name and avatar image link
        user_name = ctx.message.author.name
        user_avatar_url = ctx.message.author.avatar_url

        # Create a dictionary with the user's name, avatar image link, and words
        data = {
            "user_name": user_name,
            "user_avatar_url": user_avatar_url,
            "words": words
        }

        # Write the data to the file as JSON using the AssetEncoder
        with open(r"/mnt/notes.json", "w") as f:
            json.dump(data, f, cls=AssetEncoder)
        await ctx.send("Note written.")

