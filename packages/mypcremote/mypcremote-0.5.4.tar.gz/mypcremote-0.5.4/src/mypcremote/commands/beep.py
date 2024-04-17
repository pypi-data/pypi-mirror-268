import os
import platform

def Desc():
    return "This will produce beep sound in the system"

async def Run(ctx, frequency: int = 1000, duration: int = 1000):
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(frequency, duration)
    elif platform.system() == 'Linux':
        os.system('printf "\a"')
    else:
        await ctx.channel.send("Unsupported operating system {}".format(platform.system()))