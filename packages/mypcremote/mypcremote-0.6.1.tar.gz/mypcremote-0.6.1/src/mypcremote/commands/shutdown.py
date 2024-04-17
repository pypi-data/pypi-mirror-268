import subprocess
import platform

def Desc():
    return "To Shutdown the machine"

async def Run(ctx, delay: int = 0):
    system_platform = platform.system()

    if system_platform == "Windows":
        shutdown_command = f"shutdown /s /t {delay}"
        await ctx.channel.send("Shutting down your Windows OS in {} seconds".format(delay))
    elif system_platform == "Linux" or system_platform == "Darwin":
        shutdown_command = f"shutdown -h {'now' if delay == 0 else f'+{delay}'}"
        await ctx.channel.send("Shutting down your Linux/MAC OS in {} seconds".format(delay))
    else:
        await ctx.channel.send(f"Unsupported operating system: {system_platform}")
        return

    subprocess.run(shutdown_command, shell=True)