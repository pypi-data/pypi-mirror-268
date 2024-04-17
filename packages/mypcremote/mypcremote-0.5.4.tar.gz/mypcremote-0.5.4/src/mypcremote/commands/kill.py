import platform
import ctypes
import psutil
import os

def Desc():
    return "This will kill the active/specific running process"

async def Run(ctx, app_title=None):
    operating_system = platform.system()

    if operating_system == "Windows":
        if app_title:
            for process in psutil.process_iter(['pid', 'name']):
                if app_title.lower() in process.info['name'].lower():
                    try:
                        os.kill(process.info['pid'], 9)
                    except Exception as e:
                        print(f"Error killing process {process.info['pid']}: {e}")
            ctx.channel.send(f"All instances of {app_title} killed.")
        else:
            ctypes.windll.user32.PostMessageW(ctypes.windll.user32.GetForegroundWindow(), 0x0112, 0xF060, 0)
            ctx.channel.send("Default active window killed.")
    elif operating_system == "Linux":
        if app_title:
            for process in psutil.process_iter(['pid', 'name', 'cmdline']):
                if app_title.lower() in ' '.join(process.info['cmdline']).lower():
                    try:
                        process.terminate()
                    except Exception as e:
                        print(f"Error killing process {process.info['pid']}: {e}")
            ctx.channel.send(f"All instances of {app_title} killed on Linux.")
        else:
            ctx.channel.send("Killing the default active window not implemented on Linux yet.")
    else:
        ctx.channel.send(f"Killing not supported on {operating_system}.")