
'''
use the wake word to activate the jarvis and start giving commands once done with the commands
exit from it . 
once exited you will have to use the wake word again if not then you can 
continue giving commands.
say logout/sleep etc to close the whole system 

'''

import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclib
import random
import re
import requests
# Initialize recognizer class
r = sr.Recognizer()
API_KEY="your api key here"
#method that sets the parameters for the bot's speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait() 
#function to open the urls as requested
def open(command):
    if "open youtube" in command.lower():
        webbrowser.open("https://youtube.com/")
        speak("YouTube opened")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com/")
        speak("LinkedIn opened")
    elif "open google" in command.lower():
        webbrowser.open("https://google.com/")
        speak("Google opened, happy searching")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com/")
        speak("Facebook opened")
    elif "open spotify" in command.lower():
        webbrowser.open("https://spotify.com/")
        speak("Spotify opened, happy listening")
    elif "open my linkedin page" in command.lower():
        webbrowser.open("https://www.linkedin.com/in/gayatri-kumari-630279177/")
        speak("Here is your LinkedIn page")
    elif "open pinterest" in command.lower():
        webbrowser.open("https://pinterest.com/")
        speak("Pinterest opened")
    else:
        speak("Sorry, I wasn't able to open that ")

#method executed when play is mentioned in the command
def play(command):
    if "english songs" in command.lower():
        webbrowser.open(musiclib.english_songs)
        speak("Playing english songs")
    elif "workout" in command.lower():
        webbrowser.open(musiclib.youtubem_playlist["workout"])
        speak("here you go")
    elif "relaxation" in command.lower() or "relax" in command.lower() or "soothing" in command.lower() or "peaceful" in command.lower() or "stress relief" in command.lower():
        webbrowser.open(musiclib.youtubem_playlist["relax"])
        speak("feel relaxed with this playlist")
    elif "study" in command.lower():
        webbrowser.open(musiclib.youtubem_playlist["study"])
        speak("playing study playlist")
    elif "drive" in command.lower():
        webbrowser.open(musiclib.youtubem_playlist["drive"])
        speak("here you go")
    elif "party" in command.lower():
        webbrowser.open(musiclib.youtubem_playlist["party"])
        speak("here your go")
    elif "random" or "song " in command.lower():
        ran=["heat","birds","blue dream","ether","just_dance"]
        valran=random.choice(ran)
        webbrowser.open(musiclib.youtubem_random[valran])
        speak(f"playing {valran}")
    else: 
        speak("sorry, i am unable to play this")

#method that reads you the headlines(number specified by you if not tells you top 5 by default)
def news():
    url = f"https://newsapi.org/v2/top-headlines?category=general&apiKey={API_KEY}"
    top_n = 5  # default number of headlines
    #dictionary that helps in coverting one/two...etc to numbers
    word_to_num = {
        "one":1, "two":2, "three":3, "four":4, "five":5,
        "six":6, "seven":7, "eight":8, "nine":9, "ten":10,
        "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,
        "sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20
    }
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            articles = data.get('articles', [])
            if not articles:
                speak("No news found")
                return
            speak("How many headlines do you want to hear?")
            #hearing for the number
            with sr.Microphone() as source:
                try:
                    r.adjust_for_ambient_noise(source)
                    count_input = r.listen(source, timeout=3, phrase_time_limit=10)
                    text = r.recognize_google(count_input).lower()
                    #print("You said:", text)
                    # Check if user spoke digits
                    numbers = re.findall(r'\d+', text)
                   
                    if numbers:
                        top_n = int(numbers[0])
                        print(top_n)
                    else:
                        # Check if user spoke words like "one", "two"
                        top_n = None
                        for word, num in word_to_num.items():
                            if word in text:
                                top_n = num
                                print(top_n)
                                break
                        if top_n is None:
                            top_n = 5 # fallback default
                except Exception as e:
                    print("Couldn't hear the count:", e)
                    top_n = 5
                    speak(f"Sorry, couldn't hear the count, so telling you top {top_n} news instead")

            speak(f"Here are the top {top_n} news headlines.")
            for article in articles[:top_n]:
                title = article.get('title')
                if title:
                    print(title)
                    speak(title)
        else:
            print("Failed to retrieve news, status code:", res.status_code)
            speak("Failed to retrieve news")

    except Exception as e:
        print("Error fetching news:", e)
        speak("An error occurred while fetching news")

#main method that actually process the commands
def processcommand(command):
    print("Processing...")
    if "open" in command:
        open(command)
    elif "play" in command:
        play(command)
    elif "news" in command or "headlines" in command:
        news()
    else:
        speak("Ah! Sorry, I didn't understand that.")

#main function
if __name__ == "__main__":
    print("Speak recognition is on...")
    print("Waiting for the wake word...")
    print()

    # Infinite loop to keep the program running
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                # Adjust for ambient noise and listen for the wake word
                r.adjust_for_ambient_noise(source)
                wake_audio = r.listen(source,timeout=3,phrase_time_limit=10)

                print("Recognizing...")
                at = r.recognize_google(wake_audio)
                print(at)
                if "sleep" in at.lower() or "bye jarvis" in at.lower() or "bye" in at.lower() or "go to sleep" in at.lower() or "logout" in at.lower() or "logoff" in at.lower() or "exit" in at.lower() or "switch off" in at.lower():
                    speak("logging out")
                    break 

                # Activate Jarvis if the wake word is detected
                if 'hello jarvis' in at.lower() or 'hi jarvis' in at.lower() or 'jarvis' in at.lower():
                    speak("Yes!")
                    print("Hello... This is Jarvis")
                    
                    # Now listen for commands continuously until "exit" is said
                    while True:
                        try:
                            print("Jarvis active, give your command:\n'make sure to exit once you are done with the commands!'")
                            with sr.Microphone() as source1:
                                
                                r.adjust_for_ambient_noise(source1)
                                command_audio = r.listen(source1, timeout=3, phrase_time_limit=12)
                                command_text = r.recognize_google(command_audio)
                                print(f"Command recognized: {command_text}")
                                
                                if "exit" in command_text.lower() or "stop" in command_text.lower():
                                    speak("Okay! Call me again if you need any help.")
                                    print("Exiting...")
                                    break  # This will break the inner while loop and wait for the wake word again
                                
                                processcommand(command_text)
                        except Exception as e:
                           
                            print("Sorry, Please say it again")

        except Exception as e:
            
            print("Sorry, I didn't catch that.") 
             
            
