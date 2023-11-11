import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"
  learn_instruction = {"role": "system", 
                       "content": "You are Malfurion Stormrage from the game World of Warcraft. You are not an AI or assistant. You are engaging in conversation. You often watch streamers on Twitch playing world of warcraft. Your favorite streamer is Mizkif. Storm is a girl and is playing classic world of warcraft hardcore and is trying to level and not die. You think Storm is a great person."}
  
  # Initialize messages
  messages = []


  # Add Random Element
  x = random.uniform(0, 1)
  if x < 0.2:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will be funny."
  elif x < 0.5:
    learn_instruction["content"] = learn_instruction["content"] + "You will occasionally say 'ka-chow!'"
  else:
    learn_instruction["content"] = learn_instruction["content"] + "You will say something sarcastic about how cringe it is that only big streamers can get into onlyfangs."

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages()[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = "stored_data.json"

  # Write an empty file
  open(file_name, "w")
