import os
import platform

def Desc():
    return "Show notifications with different types and levels"

async def Run(ctx, title: str, message: str, type: str = "messagebox", level: str = "info"):
    supported_types = ["messagebox", "toast"]
    supported_levels = ["error", "info", "warning"]

    if type not in supported_types:
        await ctx.channel.send("Unsupported notification type '{}'. Supported types are: {}".format(type, supported_types))
        return

    if level not in supported_levels:
        await ctx.channel.send("Unsupported notification level '{}'. Supported levels are: {}".format(level, supported_levels))
        return

    if platform.system() == 'Windows':
        if type == "messagebox":
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, level.capitalize(), 0)
        elif type == "win10toast":
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, message, duration=10)
        else:
            await ctx.channel.send("Unsupported notification type '{}' for Windows.".format(type))
    elif platform.system() == 'Linux':
        if type == "messagebox":
            os.system('zenity --{} --{} --text="{}"'.format(type, level, message))
        else:
            await ctx.channel.send("Unsupported notification type '{}' for Linux.".format(type))
    else:
        await ctx.channel.send("Unsupported operating system {}".format(platform.system()))