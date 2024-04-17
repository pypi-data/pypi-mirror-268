import platform
import ctypes
import os

def Desc():
    return "This will lock the machine"

async def Run(ctx):
    operating_system = platform.system()

    if operating_system == "Windows":
        ctypes.windll.user32.LockWorkStation()
        ctx.channel.send("Don't worry i am locked now")
    elif operating_system == "Linux":
        os.system("xdg-screensaver lock")
        ctx.channel.send("I tried to lock myself, let's see if i am successfull")
    elif operating_system == "Darwin":
        ctx.channel.send("I don't know how to lock myself on this OS")
    else:
        ctx.channel.send("I don't know very much about this OS {}".format(operating_system))