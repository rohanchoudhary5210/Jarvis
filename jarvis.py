import tkinter as tk
# import customtkinter as ctk
from tkinter import ttk
import os
import subprocess
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser
import cv2
import sys
active = True
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# win= ctk.CTk()
win = tk.Tk()
win.geometry("700x500")
win.title("Function Input/Output GUI")

def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    talk("hope your day is going good I am your virtual assistance  sir. Please tell me how may I help you")


wishMe()


def take_command():
    command= ""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.adjust_for_ambient_noise(source)    
            r.pause_threshold = 1
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower() # type: ignore
            if 'google' in command:
                command = command.replace('google', '')
                return(command)
    except:
        pass
    return command
# if _name_ == '_main_':
    # take_command()


def run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')  # type: ignore
        talk('playing ' + song)
        pywhatkit.playonyt(song) # type: ignore 
    elif 'yourself' in command:
        talk('I am a virtual assistance created by master gear 5 in the month of August. i can perform some simple task ike playing a song for you searching something for you etectra')
    elif 'created you' in command:
        talk('i was created by gear 5')
    elif "what can you do" in command:
        print("I can fulfill most of your requiments")
        talk("I can fulfill most of your requiments")
    elif "search" in command:
        talk("Searching")
        command = command.replace('wikipedia', '') # type: ignore
        result = wikipedia.summary(command, sentences=2)
        talk("According to wikipedia")
        print(result)
        talk(result)
    elif 'sayonara' in command:
        talk('aryasamaego bye bye take care')
        sys.exit()
    elif 'code'in command:
       codepath = "C:\Program Files\Python310\Scripts\f2py.exe" 
       os.startfile(codepath)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif "sing for me" in command:
        talk("sorry i cant sing because i am very bad in singing songs")
    elif 'open' in command :
        talk('yes sire')   
        command=command.replace('open','') # type: ignore
        subprocess.Popen(command)
        subprocess.check_output=True 
    elif 'who is' in command:
        person = command.replace('who is', '') # type: ignore
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'want to go for a date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'youtube' in command:
        webbrowser.open("youtube.com")
    elif 'google' in command:
        webbrowser.open("google.com")
    elif 'stackoverflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'selfie' in command:
        talk('yes sire!!')
        cap= cv2.VideoCapture(0)
        rate, photo= cap.read()
        cv2.imshow('webcam', photo)
        cv2.waitKey(5000)
        cv2.imwrite('riz.jpg', photo)
        cap.release()
        cv2.destroyAllWindows()
    elif 'email' in command:
        talk('sending email')
        password = "pass****rd"
        from_addr = "ri*************123@gmail.com"
        to_addr = "Riz******123**8@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = "Subject"

        # add in the message body
        message = "hii, this is Rizwan"
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

    else:
        talk('Please say the command again.')
        
    while active:
        run()        

    user_input = take_command # Get user input from the entry widget
    result = run(user_input)   # type: ignore # Process the input using your function
    # output_label.config(command=result)  # Display the result using a label

# Replace 'your_function' with the actual function you want to use
input_label = tk.Label(win, text="Jarvis:",font="times 28 bold")

input_label.pack()

entry = tk.Entry(win, width=100)
entry.pack()

process_button = ttk.Button(win, text="start", command=wishMe)
process_button.pack()
process_button = ttk.Button(win, text="process", command=run)
process_button.pack()
input_label = tk.Label(win, text="Features", font="times 28 bold")
input_label.place(x=100,y=100)
input_label = tk.Label(win, text="1. 'PLAY'  command used to play music")
input_label.place(x=110,y=150)
input_label = tk.Label(win, text="2. 'SEARCH'  command used to search something")
input_label.place(x=110,y=180)
input_label = tk.Label(win, text="3. 'CODE'  command used to open code platform ")
input_label.place(x=110,y=210)
input_label = tk.Label(win, text="4. 'TIME'  command used to check the Time")
input_label.place(x=110,y=240)
input_label = tk.Label(win, text="5. 'EMAIL'  command used to send email")
input_label.place(x=110,y=270)
input_label = tk.Label(win, text="6. 'YOUTUBE'  command used to open youtube website")
input_label.place(x=110,y=300)
input_label = tk.Label(win, text="7. 'GOOGLE'  command used to open google website")
input_label.place(x=110,y=330)
input_label = tk.Label(win, text="8. 'STACKOVERFLOW'  command used to open  stackoverflow website")
input_label.place(x=110,y=360)
input_label = tk.Label(win, text="9. 'SELFIE'  command used to Take selfie")
input_label.place(x=110,y=390)
input_label = tk.Label(win, text="10. 'JOKE'  command used to crack jokes")
input_label.place(x=110,y=420)
input_label = tk.Label(win, text="11. 'OPEN'  command used to open  system software")
input_label.place(x=110,y=450)
input_label = tk.Label(win, text="12. 'SAYONARA'  command used to exit ")
input_label.place(x=110,y=480)



output_label = tk.Label(win, text="", font=("Courier 12 bold"))
output_label.pack()
win.mainloop()