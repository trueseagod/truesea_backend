import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
  body = {
    "text": message,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5,
        "use_speaker_boost" : True
    },
     "modelId": "eleven_multilingual_v2"  # Add the modelId parameter
  }

  voice_shaun = "mTSvIrm2hmcnOvb21nW2"
  voice_todd = "y1LLSaBfQoRInMqCWPzp"
  voice_antoni = "ErXwobaYiN019PkySvjV"

  # Construct request headers and url
  headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
  endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_todd}"

  try:
    response = requests.post(endpoint, json=body, headers=headers)
  except Exception as e:
     return

  if response.status_code == 200:
      # with open("output.wav", "wb") as f:
      #     f.write(audio_data)
      return response.content
  else:
    return
