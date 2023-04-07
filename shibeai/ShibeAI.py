from redbot.core import commands
import aiohttp
import json
import re


class shibeai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url_base = "http://10.101.69.2:7860"
        self.headers = {"user-agent": "ShibeAI/1.0"}

    async def send_request(self, prompt, llm_params):
        async with aiohttp.ClientSession() as session:
            data_list = [
                prompt,
                *llm_params.values()
            ]
            j_root = {"data": data_list}

            async with session.post(f"{self.url_base}/run/textgen", json=j_root, headers=self.headers) as response:
                response_text = await response.text()
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
