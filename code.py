import requests
from gtts import gTTS
import pygame
import tempfile
import time


def speak_text(text):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=text, lang='en')
        tts.save(fp.name + ".mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(fp.name + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


api_url = "http://hackhour.hackclub.com/api/clock/U0217R0029Z"


while True:
    try:
        response = requests.get(api_url)
        data = response.json()
        clock_status = data
        
        if clock_status != -1:
            print("API is fine -1")
            time.sleep(5)
            continue
        print(f"API returned {clock_status}, speaking text...")
        speak_text(f"API returned {clock_status}")
        
        time.sleep(5)  

    except requests.exceptions.RequestException as e:
        print(f"Error fetching API: {e}")
        time.sleep(5) 
    except KeyError:
        print("Error: Unexpected API response format.")
        time.sleep(5)  
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break

pygame.mixer.quit() 

print("Program ended.")
