from redbot.core import commands
import json
import requests
import re


class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Firebase Realtime Database API endpoint
        self.firebase_url = "https://shibeprime-f4fd0-default-rtdb.firebaseio.com"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "AIzaSyBjtpGxF9ihX5DY7FCFxTJOc6QTVNvc1b8",
        }

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        # Get the user's name and avatar image link
        user_name = ctx.message.author.display_name
        user_avatar_url = ctx.message.author.avatar_url
        # get all mentions in the message
        mentions = ctx.message.mentions

        # replace mentions with the mentioned user's nicknames
        for member in mentions:
            words = words.replace(f"<@{member.id}>", member.nick)
        words = re.sub(
            r"<(a)?:[a-zA-Z0-9_]+:([0-9]+)>",
            lambda x: "<img src='https://cdn.discordapp.com/emojis/{}.{}'>".format(
                x.group(2), "gif" if x.group(1) else "png"
            ),
            words,
        )

        # Create a dictionary with the user's name, avatar image link, and words
        data = {
            "user_name": user_name,
            "user_avatar_url": str(user_avatar_url),
            "words": words,
        }

        # Convert the dictionary to JSON
        json_data = json.dumps(data)

        # Send a POST request to the Firebase Realtime Database API
        response = requests.post(
            f"{self.firebase_url}/users.json", headers=self.headers, data=json_data
        )

        if response.status_code == 200:
            await ctx.send("Note written.")
        else:
            await ctx.send("An error occurred while writing the note.")
