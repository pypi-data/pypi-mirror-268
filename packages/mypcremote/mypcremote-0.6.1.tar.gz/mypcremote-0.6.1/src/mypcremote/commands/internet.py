import json
import discord
from tabulate import tabulate
from subprocess import check_output

def Desc():
    return "This will calculate & return the Current internet Bandwidth, Ping and other statistics"

def generate_map_url(lat, long):
    lat, long = float(lat), float(long)
    base_url = 'https://www.openstreetmap.org/export/embed.html?bbox='
    bbox = f'{long-0.005},{lat-0.005},{long+0.005},{lat+0.005}'
    return f'{base_url}{bbox}&layer=mapnik'

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

async def Run(ctx):
    try:
        await ctx.channel.send("Measuring internet statistics please wait")
        result = json.loads(check_output('speedtest-cli --json', shell=True, text=True))
        table = [
            ['Ping', "{} ms".format(result['ping'])],
            ['Download', convert_bytes(result['download'])],
            ['Upload', convert_bytes(result['upload'])],
            ['Server', result['server']['name']],
            ['IP', result['client']['ip']],
            ['ISP', result['client']['isp']],
            ['ISP Rating', result['client']['isprating']]
        ]
        table = tabulate(table, headers=['Attribute', 'Status'], tablefmt="pretty")
        if 'lat' in result['client'] and 'lon' in result['client']:
            url = generate_map_url(result['client']['lat'], result['client']['lon'])
            embed = discord.Embed(title="Location", description="Current Agent location wrt IP")
            embed.set_thumbnail(url=url)
            await ctx.channel.send(url, embed=embed)
        await ctx.channel.send(table)
    except Exception as e:
        await ctx.channel.send("Error: {}".format(e))