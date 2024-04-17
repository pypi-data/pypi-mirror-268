def Desc():
    return "This will terminate (exit) the discord PC bot"

async def Run(ctx):
    await ctx.channel.send("Closing the Agent now, no more commands will be processed")
    await ctx.bot.close()