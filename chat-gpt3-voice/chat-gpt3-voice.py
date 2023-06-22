import speech_recognition as sr
import openai
import playsound
import io
from pydub import AudioSegment
import pyttsx3

# set up OpenAI API credentials
openai.api_key = "Enter Your api key "

# function to generate response using GPT-3
def generate_response(text):
    prompt = f"Conversation with user:\nUser: {text}\nAI:"
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message

# function to convert text to speech
def speak_text(text):
    response_audio = openai.api.SynthesizeSpeech.create(
        engine="davinci",
        text=text,
        voice="f1"
    )
    audio_bytes = io.BytesIO(response_audio.audio_content)
    audio = AudioSegment.from_file(audio_bytes, format="mp3")
    audio.export("tts.mp3", format="mp3")
    playsound.playsound("tts.mp3")

# function to transcribe audio to text
def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# main program loop
while True:
    print("Say your question...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        with open('audio.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    # transcribe audio to text
    text = transcribe_audio_to_text('audio.wav')
    if text:
        print(f"You said: {text}")
        # generate response using GPT-3
        response = generate_response(text)
        print(f"GPT-3 says: {response}")
        # read response using text-to-speech
        speak_text(response)
