import pyttsx3                                       # pip install pyttsx3                        (text to speech )
import datetime                                      # importing date adn time dictonaries
import speech_recognition as sr                      # pip install speechrecognition              (to take commands through speech)(also added a variable as sr to run this command)
import wikipedia                                     # pip install wikipedia 
import smtplib                                       # importing a library to send emails 
import webbrowser as wb                              # importing the inbuilt lib for browser
import os                                            # importing the built in lib for os related querys.
import pyautogui                                     # pip3 install pyautogui    (for taking screenshots)
import psutil                                        # pip3 install psutil       (to get the battery and cpu details of the system)
import pyjokes                                       # pip install pyjokes     (to get jokes)
import requests
import pyowm 
from bs4 import BeautifulSoup
import speedtest
import keyboard
import random
import webbrowser



engine = pyttsx3.init()


def speak(audio):                                   # creating a function speak whatever you want the ai to speak just type speak("enter you text") 
    engine.say(audio)
    engine.runAndWait()


def time():                                         # creating a function which speaks time whenever "time()" is called
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(time)


def date():                                         # creating the date function
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("and the current date is ")
    speak(day)
    speak(month)
    speak(year)


def wishme():                                       # Creating the wishme function "wishme()"
    speak("welcome back Arul!")
    time()
    date()
    hour = datetime.datetime.now().hour             # creating a variable to greet morning afternoon eveing 
    if hour >=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night SIr")
    
    speak("devil at your service. Please tell me how can I help you?")


def takecommand():                                  # creating the function to take command 
    r = sr.Recognizer()
    with sr.Microphone() as source:                 # adding the microphone 
        print("Listening...")                       # once it starts listing it will show listning 
        r.pause_threshold = 1                       # after running the program it will wait for 1 sec 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')        # giving language 
        print(f"User said: {query}\n")              # printing whatever is said by the user

    except Exception as e:                          # if it is unable to recoganise than it will say this. 
        print(e)
        print("Say that again please...")
        return "None"
    
    return query


def sendemail(to, content):                        # creating a function "send email" to send emails\\ you also need to enable less secure apps access in you gmail from which you want to send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)   # providing the gmail and port which we are using "587 is the default port gmail gennerally uses"
    server.ehlo()
    server.starttls()
    server.login('YOUR MAIL ID', 'PASSWORD OR YOUR MAIL')
    server.sendmail('YOUR MAIL ID', to, content)
    server.close()


def screenshot():                                  # creating a function to take screenshots 
    img = pyautogui.screenshot()
    img.save("enter the path where you want to save the screenshot")    # enter the folder path where you want to save the screenshot taken


def cpu():                                         #defining cpu funcion for battery percent, cpu usage, cpu temperature
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("battery percentage at the moment is ")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_jokes())                      # defining jokes function for getting jokes


if __name__ == "__main__":                          # giving commands first defining thm here then using them in speech to execute
    wishme()
    while True:
        query = takecommand().lower()               # taking all commands in lowercase
        if 'time' in query:                         # we say time it will tell time 
            time()
      

        elif 'date' in query:                       # we say date it will tell date 
            date()
      

        elif 'sleep' in query:                      # we say sleep it will tell exit
           speak("Thank you sir! You should also take some rest. Have a good day ahead")
           quit()
       

        elif 'wikipedia' in query:                  # to search anything on wikipedia
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentence=5)
            print(result)
            speak(result)
        

        elif 'email to arul' in query:
            try:
                speak("what message I should write in the email ?")
                content = takecommand()
                to ='arulgupta15@gmail.com'
                sendemail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("I am sorry! I am unable to send the email.")
       

        elif 'chrome search' in query:           # defining the function to search on chrome google
            speak("what should I search ?")
            chromepath = 'Enter you chrome application.exe file path here %s'     # enter the chrome.exe file path in the brackets 
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
           


        elif 'logout' in query:                  # defining the function for logout the system
            os.system("shutdown -l")   


        elif 'shutdown' in query:                # defining the function for shutdown the system
            os.system("shutdown /s /t 1") 


        elif 'restart' in query:                 # defining the function for restarting the system
            os.system("shutdown /r /t 1") 


        elif 'play song' in query:               # defining the function for playing the songs in your system in the music directory whaere your songs are present in the system
            songs_dir = 'enter your music directory path'   # enter the music directory folder path in the braket 
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))


        elif 'remember that' in query:          # defing the function for the ai to remember all the data 
            speak("what should I remember ?")
            data = takecommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()


        elif 'do you know anything' in query:   # defining the function to tell us what it has remembered
            remember =open('data.txt', 'r')
            speak("you said me to remember" +remember.read())


        elif 'screenshot' in query:            # the function to screenshot when we say screenshot n speech 
            screenshot()
            speak("screenshot taken !")


        elif 'cpu' in query:                   # the function specifies the cpu function which was defined above 
            cpu()


        elif 'joke' in query:                  # the function specifies the jokes function which was defined above
            jokes()

        elif "temperature" in query:           # defining the temperature command for delhi 
            location = "delhi"
            search = f"temperature in {location}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")

            
        elif "weather" in query:              # defining the weather command for delhi 
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


        elif "internet speed" in query:                # defining a function to get internet speed.
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            speak(f"Wifi download speed is {download_net}")
            speak(f"Wifi Upload speed is {upload_net}")
                    
        elif "click my photo" in query:                   #defining the function to click a photo 
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")




############################################################

        elif "hello" in query:
            speak("Hello sir, how are you ?")
        elif "I am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
                
 ###################       
        elif "tired" in query:                         # defining the function tired to play youtube 
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=Op4EMZXWjyE&list=RDOp4EMZXWjyE&start_radio=1")
                    
######################
        elif "pause" in query:                           # to pause the video 
                    pyautogui.press("k")
                    speak("video paused")
        elif "play" in query:                            # to play the video 
                    pyautogui.press("k")
                    speak("video played")
        elif "mute" in query:                            # to mute the video 
                    pyautogui.press("m")
                    speak("video muted")
                
####################

        elif "volume up" in query:                       # to volume up 
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
        elif "volume down" in query:                    # to volume down
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
        
       
 ###################################################################################################



        elif 'exit' in query:                  
            break
        else:
            speak("I didn't get that. Please try again")













