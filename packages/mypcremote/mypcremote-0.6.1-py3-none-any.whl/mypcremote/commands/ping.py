import socket

def Desc():
    return "This will echo back hostname of the machine to check available instances of running bot, helpful if running multiple bots in different machines under same token"

async def Run(ctx):
    await ctx.channel.send("Hello From ".format(socket.gethostname()))