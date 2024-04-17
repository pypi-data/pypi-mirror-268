import psutil
import pygetwindow as gw
from tabulate import tabulate

def Desc():
    return "To get current usage status of machine"

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_active_window():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else 'N/A'

async def Run(ctx):
    response = [
        ['CPU', get_cpu_usage()],
        ['RAM', get_ram_usage()],
        ['Active Window', get_active_window()]
    ]

    message = tabulate(response, headers=['Resource', 'Usage'], tablefmt="pretty")
    await ctx.channel.send(message)