import subprocess
import platform

def Desc():
    return "To put the machine to sleep"

async def Run(ctx, delay: int = 0):
    system_platform = platform.system()

    if system_platform == "Windows":
        command = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        await ctx.channel.send(f"Putting your Windows OS to sleep in {delay} seconds")
    elif system_platform == "Linux" or system_platform == "Darwin":
        command = "pmset sleepnow"
        await ctx.channel.send(f"Putting your Linux/MAC OS to sleep in {delay} seconds")
    else:
        await ctx.channel.send(f"Unsupported operating system: {system_platform}")
        return

    subprocess.run(command, shell=True)