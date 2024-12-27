import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import pyttsx3  
import requests
import json
import pyautogui
import psutil
import platform
import wikipedia
import subprocess
import sys
import wolframalpha
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

openai.api_key = "YOUR-OPENAI-API-KEY"  # Replace with your OpenAI API key

# Wolframalpha API key
WOLFRAM_API_KEY = "YOUR-WOLFRAM-API-KEY"

# Email configuration
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"    


# Global chat history for conversation with AI
chatStr = ""

# Function to chat with the AI and get responses
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Harry: {query}\n Jarvis: "
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        print(f"Error interacting with OpenAI API: {e}")
        return "Sorry, I couldn't process your request right now."

# Function to process AI prompts and save responses to a file
def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"]

        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Openai/{timestamp}_{''.join(prompt.split('intelligence')[1:]).strip()}.txt"
        
        with open(filename, "w") as f:
            f.write(text)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Error processing AI prompt: {e}")

# Function to get weather information
def get_weather(city):
    API_KEY = "YOUR-OPENWEATHER-API-KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={Enter your city city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}"
    except:
        return "Sorry, I couldn't fetch the weather information."

# Function to send email to new user with an id
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        print(f"Sending email to {to_email} with subject: {subject}")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Function to get system information
def get_system_info():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return f"""
    CPU Usage: {cpu_usage}%
    Memory Usage: {memory.percent}%
    Disk Usage: {disk.percent}%
    OS: {platform.system()} {platform.release()}
    """

# Function to use text-to-speech to say something
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 135.0)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()

# Function to listen to user command via speech recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return "Sorry, I did not catch that."
        except sr.RequestError:
            print("Service is unavailable.")
            return "Sorry, I am unable to reach the service right now."
        except Exception as e:
            print(f"Error with speech recognition: {e}")
            return "Sorry, something went wrong."

# Function to handle website opening based on user input voice command
def openWebsite(query):
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"],
        ["facebook", "https://www.facebook.com"],
        ["instagram", "https://www.instagram.com"],
        ["twitter", "https://www.twitter.com"],
        ["reddit", "https://www.reddit.com"],
        ["discord", "https://www.discord.com"],
        ["github", "https://www.github.com"],
        ["stackoverflow", "https://www.stackoverflow.com"],
    ]
    
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])

# Main loop to run the assistant
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I is online.")
    
    while True:
        query = takeCommand().lower()
        
        # Handle website opening
        openWebsite(query)
        
        # Handle video playing
        if "open video" in query:
            videoPath = "/home/rudddyy/.wallpapers/orange-train-at-sunset.3840x2160.mp4"
            if os.path.exists(videoPath):
                try:
                    subprocess.run(['xdg-open', videoPath], check=True)
                    say("Opening video.")
                except subprocess.CalledProcessError as e:
                    print(f"Error opening video: {e}")
                    say("Sorry, I couldn't open the video.")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    say("Sorry, something went wrong while opening the video.")
            else:
                print("Video file not found")
                say("Sorry, I couldn't find the video file.")
        
        # Tell the current time
        elif "the time" in query:
            now = datetime.datetime.now()
            hour = now.strftime("%H")
            minute = now.strftime("%M")
            second = now.strftime("%S")
            meridiem = now.strftime("%p")
            weekday = now.strftime("%A")
            date = now.strftime("%B %d, %Y")
            
            if "date" in query:
                say(f"Sir, today is {weekday}, {date}")
            elif "full" in query:
                say(f"Sir, it is {hour}:{minute}:{second} {meridiem} on {weekday}, {date}")
            else:
                say(f"Sir, the time is {hour}:{minute} {meridiem}")

        # Weather information
        elif "weather" in query:
            say("Which city would you like to know the weather for?")
            city = takeCommand()
            weather_info = get_weather(city)
            say(weather_info)

        # System information
        elif "system info" in query:
            info = get_system_info()
            say("Here's your system information:")
            print(info)
            say(info)

        # Send email
        elif "send email" in query:
            try:
                say("Who should I send the email to?")
                to_email = takeCommand()
                say("What should be the subject?")
                subject = takeCommand()
                say("What should I write in the email?")
                body = takeCommand()
                
                if send_email(to_email, subject, body):
                    say("Email has been sent successfully!")
                else:
                    say("Sorry, I couldn't send the email.")
            except Exception as e:
                say("Sorry, I encountered an error while sending the email.")

        # Wikipedia search
        elif "wikipedia" in query:
            say("What would you like to search on Wikipedia?")
            search_query = takeCommand()
            try:
                result = wikipedia.summary(search_query, sentences=2)
                say("According to Wikipedia:")
                say(result)
            except:
                say("Sorry, I couldn't find that on Wikipedia.")

        # Calculator
        elif "calculate" in query:
            try:
                client = wolframalpha.Client(WOLFRAM_API_KEY)
                res = client.query(query)
                answer = next(res.results).text
                say(f"The answer is {answer}")
            except:
                say("Sorry, I couldn't perform that calculation.")
            
        # AI interaction
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        # Quit Jarvis
        elif "jarvis quit" in query:
            say("Goodbye, sir.")
            break

        # Reset chat history
        elif "reset chat" in query:
            try:
                chatStr = ""
                say("Chat history has been successfully reset.")
            except Exception as e:
                print(f"Error resetting chat: {e}")
                say("Sorry, I encountered an error while trying to reset chat history.")
        
        # General AI chat
        else:
            chat(query)
