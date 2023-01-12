from redbot.core import commands
import json
import pyrebase

class WriteNote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Initialize Firebase
        config = {
          "apiKey": "AIzaSyBjtpGxF9ihX5DY7FCFxTJOc6QTVNvc1b8",
          "authDomain": "shibeprime-f4fd0.firebaseapp.com",
          "databaseURL": "https://shibeprime-f4fd0-default-rtdb.firebaseio.com",
          "projectId": "shibeprime-f4fd0",
          "storageBucket": "shibeprime-f4fd0.appspot.com",
          "messagingSenderId": "31986328863",
          "appId": "1:31986328863:web:cb25dde398d29df667fc2a",
          "measurementId": "G-746032TVEC"
        }
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    @commands.command()
    async def writenote(self, ctx, *, words: str):
        # Get the user's name and avatar image link
        user_name = ctx.message.author.name
        user_avatar_url = ctx.message.author.avatar_url

        # Create a dictionary with the user's name, avatar image link, and words
        data = {
            "user_name": user_name,
            "user_avatar_url": str(user_avatar_url),
            "words": words
        }
        
        # Push the data to the database
        self.db.child("users").push(data)
        await ctx.send("Note written.")
