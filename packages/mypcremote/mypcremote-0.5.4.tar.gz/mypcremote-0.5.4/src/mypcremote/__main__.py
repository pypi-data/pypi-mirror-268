import os
import sys
import discord
from pydoc import importfile
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
intents = discord.Intents.all()

bot = Bot(description="A remote administration discord BOT to control your PC", command_prefix='#', intents=intents)

def RegisterCommands():
    commands = os.path.join(os.path.dirname(__file__), "commands")
    scripts = [file for file in os.listdir(commands) if file.endswith('.py') and file != '__init__.py']
    for name in scripts:
        script_module = importfile(os.path.join(commands, name))
        Instance = getattr(script_module, 'Run', None)

        if Instance and callable(Instance):
            desc = getattr(script_module, 'Desc', 'Not Available')
            bot.command(name=name.split(".")[0], help=desc())(Instance)

def Init(token=os.environ.get('TOKEN')):
    RegisterCommands()
    bot.run(token)

@bot.event
async def on_ready():
    greeting = f'Hello master I "{bot.user}" am ready to serve you'
    channels = list(bot.get_all_channels())
    if len(channels) > 0:
        await channels.pop().send(greeting)

@bot.event
async def on_disconnect():
    print("I am going to die")

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