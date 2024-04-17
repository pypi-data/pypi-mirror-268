import discord
import pyautogui
from io import BytesIO

def Desc():
    return "This will capture the Screenshot"

async def Run(ctx):
    screenshot = pyautogui.screenshot()

    screenshot_bytes = BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes.seek(0)

    await ctx.channel.send("Screenshot:", file=discord.File(screenshot_bytes, filename='screenshot.png'))