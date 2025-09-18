from gtts import gTTS #google text to speech(gtts)
import os
mytext='karthika is a fabulous'
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("Welcome.mp3")
os.system("Start Welcome.mp3")