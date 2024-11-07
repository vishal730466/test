# import pandas as pd
# import matplotlib as plt

# data = pd.read_csv("tip.csv")
# plt.plot(data["tip"])
# plt.plot(data["size"])
# plt.title("Line Graph")
# plt.xlabel("day")
# plt.ylabel("tip")
# plt.show()
from gtts import gTTS
import pyglet 
from time import sleep

# Create a gTTS instance
text_to_convert = "Hello, this is a test."
tts = gTTS(text_to_convert, lang='en')

# Save the audio to a temporary file
filename = 'output.mp3'
tts.save(filename)

# Load the audio using pyglet
music = pyglet.media.load(filename, streaming=False)
music.play()

# Wait for the audio to finish playing
sleep(music.duration)

# Clean up: remove the temporary file