import googletrans #library
import speech_recognition #speech recognition library
import gtts #gts(text to voice) library
import playsound
input_language = "hi"# input language hindi
output_language = "en"
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak something")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language = input_language)
    print(text)


translator = googletrans.Translator()
translation = translator.translate(text,dest = output_language)
print(translation.text)
converted_audio = gtts.gTTS(translation.text,lang = output_language)
converted_audio.save("audio.mp3");
playsound.playsound("audio.mp3")

