import subprocess
import platform

def Desc():
    return "To Reboot the machine"

async def Run(ctx, delay: int = 0):
    system_platform = platform.system()

    if system_platform == "Windows":
        command = f"shutdown /r /t {delay}"
        await ctx.channel.send(f"Rebooting your Windows OS in {delay} seconds")
    elif system_platform == "Linux" or system_platform == "Darwin":
        command = f"shutdown -r {'now' if delay == 0 else f'+{delay}'}"
        await ctx.channel.send(f"Rebooting your Linux/MAC OS in {delay} seconds")
    else:
        await ctx.channel.send(f"Unsupported operating system: {system_platform}")
        return

    subprocess.run(command, shell=True)