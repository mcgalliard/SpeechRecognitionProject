import speech_recognition as sr
import pyaudio

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(0) as source:
    print("Enter Password to be granted access")
    audio = r.listen(source)
    password = r.recognize_google(audio)
    if 'element' in str(password):
        print("access granted")
        print("Welcome to bank")
        print("- View Balance -")
        print("- Withdraw -")
        print("- Deposit")
    else:
        print("access denied")

