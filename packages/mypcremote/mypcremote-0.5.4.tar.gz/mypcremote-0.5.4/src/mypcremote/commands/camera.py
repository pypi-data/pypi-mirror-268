import discord
import cv2
from io import BytesIO
from PIL import Image

def Desc():
    return "This will capture a frame from the camera"

async def Run(ctx, camera: int = 0):
    cap = cv2.VideoCapture(camera)

    ret, frame = cap.read()

    if not ret:
        await ctx.channel.send("Failed to capture frame from the camera.")
        return

    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    image_bytes = BytesIO()
    pil_image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    await ctx.channel.send("Camera Frame:", file=discord.File(image_bytes, filename='camera_frame.png'))

    cap.release()
