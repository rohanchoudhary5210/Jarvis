# Jarvis: Virtual Assistant with GUI
Jarvis is a virtual assistant program built using Python and the Tkinter library for the GUI. It is equipped with voice recognition, speech synthesis, and various commands for interacting with system services, browsing the web, sending emails, and more.

## Features
* **Play Music:** Command **'play [song]'** will play the desired song on YouTube.
* **Search Information:** Command **'search [query]'** retrieves information from Wikipedia.
* **Open Code Editor:** Command **'code'** opens the code editor.
* **Tell Time:** **Command time** will report the current time.
* **Send Email:** Command **email** sends an email to a predefined address.
* **Open Websites:** Commands like **youtube, google, stackoverflow** will open the respective websites in a browser.
* **Take a Selfie:** Command **selfie** will capture a photo using the webcam.
* **Tell a Joke:** Command **joke** makes Jarvis tell a joke.
* **Open System Software:** Command **open [software]** opens the specified software.
* **Exit:** Command **sayonara** will close the assistant.
## Requirements
To run this project, you need to have the following Python libraries installed:

* tkinter
* speech_recognition
* pyttsx3
* pywhatkit
* wikipedia
* pyjokes
* smtplib
* opencv-python
* webbrowser

You can install the dependencies using pip:
```pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes opencv-python```
## How to Run
1. Clone the repository to your local machine:
```git clone https://github.com/yourusername/jarvis-virtual-assistant.git```
2. Install the required libraries as listed in the **Requirements** section.
3. Run the program:
```python jarvis.py```
## Usage
1. Launch the application.
2. Jarvis will greet you with a voice prompt and ask how it can assist you.
3. You can issue voice commands for tasks such as playing music, checking the time, or searching the web.
4. Use the GUI buttons to start Jarvis and process voice commands.
## Voice Commands
* **'PLAY [song_name]':** Plays the specified song on YouTube.
* **'SEARCH [query]':** Searches Wikipedia for the query and reads the summary.
* **'CODE':** Opens the default code editor.
* **'TIME':** Tells the current time.
* **'EMAIL':** Sends a predefined email.
* **'YOUTUBE'/'GOOGLE'/'STACKOVERFLOW':** Opens the respective websites in your browser.
* **'SELFIE':** Takes a photo using the webcam.
* **'JOKE':** Tells a random joke.
* **'OPEN [software]':** Opens specified system software.
* **'SAYONARA':** Closes the program.
## Notes
* Make sure to adjust the email and credentials in the **'email'** command before using it.
* Voice recognition accuracy may vary depending on ambient noise and microphone quality.
* The program uses Google's voice recognition API, which requires an active internet connection.
## Future Enhancements
Some ideas for potential future improvements:
* Addition of more advanced commands and integrate additional APIs (weather, calendar, etc.).
* Customize the GUI for a more user-friendly experience.
* Add support for other languages in voice recognition and synthesis.
## Contibutions
If you have any issue or suggestions feel free to open an issue or contact me.
