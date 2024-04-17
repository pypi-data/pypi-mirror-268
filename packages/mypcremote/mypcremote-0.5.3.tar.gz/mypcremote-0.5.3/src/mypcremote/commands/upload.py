import discord
import shutil
import os

def Desc():
    return "Let the bot upload the file as a attachment for you"

async def Run(ctx, file_path: str):
    try:
        if os.path.isdir(file_path):
            shutil.make_archive(file_path, 'zip', file_path)
            zip_file_path = f'{file_path}.zip'
            fname = os.path.basename(zip_file_path)
            zip_file = discord.File(zip_file_path, filename=fname)

            await ctx.channel.send(file=zip_file)
            os.remove(zip_file_path)
        else:
            with open(file_path, 'rb') as file:
                fname = os.path.basename(file_path)
                file_to_send = discord.File(file, filename=fname)
                
                await ctx.channel.send(file=file_to_send)
    except FileNotFoundError:
        await ctx.channel.send(f'The file or directory "{file_path}" does not exist.')
    except Exception as e:
        await ctx.channel.send("Error occured {}".format(str(e)))