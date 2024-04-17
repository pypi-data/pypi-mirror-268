import platform

def Desc():
    return "To control the volume of the PC range(0 - 100)"

async def Run(ctx, volume_level: int):
    try:
        system_platform = platform.system()

        if system_platform == "Windows":
            await ctx.channel.send("Setting volume to: {}%".format(volume_level))
            set_volume_windows(volume_level)
        elif system_platform == "Linux":
            await ctx.channel.send("Setting volume to: {}%".format(volume_level))
            set_volume_linux(volume_level)
        else:
            await ctx.channel.send("Can't control volume, unknown platform {}".format(system_platform))
    except Exception as e:
        await ctx.channel.send(str(e))

def set_volume_windows(volume_level):
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level / 100, None)

def set_volume_linux(volume_level):
    from pulsectl import Pulse

    with Pulse('set_volume_linux') as pulse:
        for sink in pulse.sink_list():
            pulse.volume_set_all_chans(sink, volume_level / 100)