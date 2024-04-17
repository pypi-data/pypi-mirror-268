import subprocess

def Desc():
    return "To execute a terminal command and send the output"

async def Run(ctx, command: str):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        await ctx.channel.send(result)
    except subprocess.CalledProcessError as e:
        await ctx.channel.send(e.output)
    except Exception as e:
        await ctx.channel.send(f"Error executing command: {e}")