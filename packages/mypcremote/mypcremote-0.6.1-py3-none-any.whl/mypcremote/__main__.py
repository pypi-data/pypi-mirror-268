import os
import sys
import socket
import discord
from pydoc import importfile
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

class BotControls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="This will enable the bot specified by unique Hostname of the bot machine or all bots if not specified")
    async def enable(ctx, hostname="all"):
        if hostname == socket.gethostname() or hostname == "all":
            count = HandleCommands()
            await ctx.channel.send(f"Activated {count} commands")

    @commands.command(description="This will disable the bot specified by unique Hostname of the bot machine or all bots if not specified")
    async def disable(ctx, hostname="all"):
        if hostname == socket.gethostname() or hostname == "all":
            count = HandleCommands(register=False)
            await ctx.channel.send(f"Disabled {count} commands")

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
intents = discord.Intents.all()

bot = Bot(description="A remote administration discord BOT to control your PC", command_prefix='#', intents=intents)

def HandleCommands(register=True):
    commands = os.path.join(os.path.dirname(__file__), "commands")
    scripts = [file for file in os.listdir(commands) if file.endswith('.py') and file != '__init__.py']
    count = 0
    for name in scripts:
        command = name.split('.')[0]
        if register and command not in [c.name for c in bot.commands]:
            script_module = importfile(os.path.join(commands, name))
            Instance = getattr(script_module, 'Run', None)

            if Instance and callable(Instance):
                desc = getattr(script_module, 'Desc', 'Not Available')
                bot.command(name=command, help=desc())(Instance)
                count += 1
        elif not register and command != "ping" and command in [c.name for c in bot.commands]:
            bot.remove_command(command)
            count += 1
    return count

def Init(token=os.environ.get('TOKEN')):
    HandleCommands()
    bot.run(token)

@bot.event
async def on_ready():
    greeting = f'Hello master I "{socket.gethostname()}" am ready to serve you'
    channels = list(bot.get_all_channels())
    if len(channels) > 0:
        await channels.pop().send(greeting)
    if not bot.get_cog("BotControls"):
        await bot.add_cog(BotControls(bot))

@bot.event
async def on_disconnect():
    print("Connection broken from server")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in event {event}: {sys.exc_info()} with ARGS {args} and {kwargs}")

@bot.event
async def on_command_error(event, *args, **kwargs):
    print(f"Error in command event {event}: {sys.exc_info()} with ARGS {args} and {kwargs}")

@bot.event
async def on_message(message):
    proceed = message.author != bot.user
    if proceed:
        await bot.process_commands(message)

def main():
    sys.path.append(os.path.dirname(__file__))
    if os.environ.get('TOKEN', None) is None:
        token = input("Enter Auth Token: ") if len(sys.argv) == 1 else sys.argv[1]
        with open(os.path.join(os.path.dirname(__file__), ".env"), 'w') as f:
            f.write(f'TOKEN={token}')
        Init(token)
    else:
        Init()

if __name__ == "__main__":
    main()