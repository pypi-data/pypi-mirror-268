def Desc():
    return "To clear all or x last messages from channel"

async def Run(ctx, count: int = 0):
    try:
        await ctx.message.delete()
        if count == 0:
            deleted = await ctx.channel.purge()
            await ctx.channel.send(f'Cleared all messages in the channel. ({len(deleted)} messages)')
        else:
            deleted = await ctx.channel.purge(limit=count)
            await ctx.channel.send(f'Cleared {len(deleted)} messages.')
    except Exception as e:
        await ctx.channel.send(str(e))