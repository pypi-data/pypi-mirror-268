def Desc():
    return "This will echo back PONG response to check if bot responding"

async def Run(ctx):
    await ctx.channel.send("PONG")