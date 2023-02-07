import json
import re
import requests

from redbot.core import commands


class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.firebase_url = "https://shibeprime-f4fd0-default-rtdb.firebaseio.com"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "AIzaSyBjtpGxF9ihX5DY7FCFxTJOc6QTVNvc1b8",
        }

    @commands.command()
    async def writenote(self, ctx, *, words):
        user_name = ctx.message.author.display_name
        user_avatar_url = str(ctx.message.author.avatar_url)
        mentions = ctx.message.mentions

        for member in mentions:
            words = words.replace(f"<@{member.id}>", member.nick or member.name)

        words = re.sub(
            "<(a)?:[a-zA-Z0-9_]+:([0-9]+)>",
            lambda x: "<img src='https://cdn.discordapp.com/emojis/{}.{}'>".format(
                x.group(2), "gif" if x.group(1) else "png"
            ),
            words,
        )

        data = {"user_name": user_name, "user_avatar_url": user_avatar_url, "words": words}
        json_data = json.dumps(data)
        response = requests.post(f"{self.firebase_url}/users.json", headers=self.headers, data=json_data)

        if response.status_code == 200:
            await ctx.send("Note written.")
        else:
            await ctx.send("An error occurred while writing the note. Response: " + response.text)
