import os
import platform
import subprocess

def Desc():
    return "This will hybernate your PC"

async def Run(ctx):
    system_platform = platform.system()
    response = await hibernate_machine(system_platform)
    await ctx.channel.send(response)

async def hibernate_machine(platform):
    if platform == 'Windows':
        os.system('shutdown /h /t 1')
        return "Hybernating windows machine"
    elif platform == 'Linux':
        subprocess.run(['sudo', 'systemctl', 'hibernate'])
        return "Hybernating Linux machine"
    else:
        return f"Hibernation is not supported on {platform}."