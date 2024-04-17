import webbrowser

def Desc():
    return "This will open the URL in default browser"

async def Run(ctx, url: str, browser: str = 'default'):
    if browser == 'default':
        status = "Successfull" if webbrowser.open(url) else "Failed"
        await ctx.channel.send("The URL opening process was {}".format(status))
    else:
        c = webbrowser.get(browser)
        status = "Successfull" if c.open(url) else "Failed"
        await ctx.channel.send("The URL opening process was {}".format(status))