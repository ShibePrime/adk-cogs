import asyncio
import json
import re
import random
import string
import sys
from redbot.core import commands
import websockets

IP_ADDRESS = "10.101.69.2"
PORT = "8080"


def generate_session_id():
    charset = string.ascii_lowercase + string.digits
    return ''.join((random.choice(charset) for _ in range(9)))


class ShibeAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session_id = generate_session_id()

    async def send_request(self, prompt, llm_params):
        async with websockets.connect(f"ws://{IP_ADDRESS}:{PORT}/queue/join") as websocket:
            data_list = [
                prompt,
                *llm_params.values()
            ]
            json_data = {"data": data_list}

            await websocket.send(json.dumps(json_data))
            response_text = await websocket.recv()
            print("Response text:", response_text)
            result = json.loads(response_text)["data"][0]

        return result[len(prompt):]

    @commands.command(aliases=["shibeai", "heyshibeai", "hey_shibeai"])
    async def ask_shibeai(self, ctx, *, question: str):
        input_text = re.sub(r"@.*\s?", "", question).strip()
        prompt = f"User: {input_text}\nShibeAI: "

        async with ctx.channel.typing():
            response_text = await self.send_request(prompt, {
                "max_new_tokens": 150,
                "do_sample": True,
                "temperature": 0.8,
                "top_p": 0.9,
                "typical_p": 1,
                "repetition_penalty": 1.15,
                "encoder_repetition_penalty": 1.0,
                "top_k": 100,
                "min_length": 0,
                "no_repeat_ngram_size": 0,
                "num_beams": 1,
                "penalty_alpha": 0,
                "length_penalty": 1,
                "early_stopping": False,
                "seed": -1
            })

            response_text = response_text.replace("\\", "\\\\").replace("<", "\\<").replace(">", "\\>").replace("@", "\\@ ").strip()
            if not response_text.strip():
                response_text = "[ShibeAI Error]"

            await ctx.send(response_text)
