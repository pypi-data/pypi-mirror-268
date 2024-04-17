import discord
import pyaudio
import sounddevice as sd

class PyAudioPCM(discord.AudioSource):
    def __init__(self, channels=2, rate=48000, chunk=960, input_device=1) -> None:
        p = pyaudio.PyAudio()
        self.chunks = chunk
        self.input_stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, input_device_index=input_device, frames_per_buffer=chunk)

    def read(self) -> bytes:
        return self.input_stream.read(self.chunks)

def Desc():
    return "To initiate a Voice call from Machine"

async def Run(ctx):
    if not ctx.author.voice:
        await ctx.channel.send("You need to first join the voice channel")
        return

    channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        tunnel = await channel.connect()

        info = sd.query_devices(sd.default.device, 'input')
        source = PyAudioPCM(input_device=info['index'])
        tunnel.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
    else:
        await ctx.voice_client.disconnect()