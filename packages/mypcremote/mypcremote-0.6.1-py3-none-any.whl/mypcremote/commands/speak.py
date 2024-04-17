import os
import platform

def Desc():
    return "To speak the text using TTS"

async def Run(ctx, phrase: str):
    system_platform = platform.system()

    if system_platform == "Windows":
        await ctx.channel.send("Saying: " + phrase)
        os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('{}')".format(phrase))
    elif system_platform == "Linux":
        await ctx.channel.send("Saying: " + phrase)
        os.system('spd-say "{}"'.format(phrase))
    else:
        await ctx.channel.send("Can't use TTS unknown platform {}".format(system_platform))