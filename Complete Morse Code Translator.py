import numpy as np
import speech_recognition as sr
import pyaudio


letter_to_morse = {
	"a" : ".-",	    "b" : "-...",	"c" : "-.-.",
	"d" : "-..",	"e" : ".",	    "f" : "..-.",
	"g" : "--.",	"h" : "....",	"i" : "..",
	"j" : ".---",	"k" : "-.-",	"l" : ".-..",
	"m" : "--",	    "n" : "-.",	    "o" : "---",
	"p" : ".--.",	"q" : "--.-",	"r" : ".-.",
	"s" : "...",	"t" : "-",	    "u" : "..-",
	"v" : "...-",	"w" : ".--",	"x" : "-..-",
	"y" : "-.--",	"z" : "--..",	"1" : ".----",
	"2" : "..---",	"3" : "...--",	"4" : "....-",
	"5" : ".....", 	"6" : "-....",	"7" : "--...",
	"8" : "---..",	"9" : "----.",	"0" : "-----",	
	" " : " ",      ".":".-.-.-",   ",":"--..--",
    "?":"..--..",   "!":"..--.",    ":":"---...",
    "'":".----."}

mor = {v: k for k, v in letter_to_morse.items()}


def convert_text_to_morse(message):
    s=""
    for i in message.lower():
        m=letter_to_morse[i]
        s+=m
    print(s)
    return s


def audible_dot_and_dash(text):
    x=convert_text_to_morse(text)
    for i in x:
        if i==".":
            p = pyaudio.PyAudio()
            volume = 0.5     
            fs = 44100       
            duration = 1.0   
            f = 440.0        
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)
            stream.write(volume*samples)
            stream.stop_stream()
            stream.close()
            p.terminate()
        elif i=="-":
            p = pyaudio.PyAudio()
            volume = 0.5
            fs = 44100       
            duration = 3.0   
            f = 440.0        
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)
            stream.write(volume*samples)
            stream.stop_stream()
            stream.close()
            p.terminate()
        elif i==" ":
            p = pyaudio.PyAudio()
            volume = 0.5     
            fs = 44100     
            duration = 7.0   
            f = 10.0       
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=fs,
                            output=True)
            stream.write(volume*samples)    
            stream.stop_stream()
            stream.close()
            p.terminate()
        else:
            continue


#x=afplay "/Users/shreyashrivastava/Downloads/audio sample to morse.wav"
def speech_to_audio(audio_file):    
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print(text)
        except:
             print('Sorry.. run again...')
    audible_dot_and_dash(text)


def mor_to_eng():
    print('''Enter your msg in Morse.
    Notice that: 
        1- Use / to separate the words and ' ' to separate letters.
        2- Your message must contain only letters and numbers.
        3- '?' in output means that your input was unknown.
        >>> ''', end = '')
    msg = input(' ')              
    out = []
    letter = []
    j = -1
    for i in msg.split('/'):
        j += 1
        letter += [i.split(' ')]
        for k in range(len(letter[j])):
            out += mor.get(letter[j][k], '?')
        out += ' '
    print('\n      >>> Your msg is: ', end = '')
    print('' .join(out))
    return ('' .join(out))


def live_audio_to_morse():
    recog1 = sr.Recognizer()
    mc = sr.Microphone()
    with mc as source:
        print("Speak to initiate the Translation: ")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        MyText = recog1.recognize_google(audio) 
        MyText = MyText.lower()
        print(MyText)
        audible_dot_and_dash(MyText)

        
def final_func():
    choice=input("Type E for encoding and D for decoding:")
    if choice.lower()=="e":
        opt=input("Press A for audio file and M for a message:")
        if opt.lower()=="a":
            ch=input("Press L for live audio and R for recorded audio:")
            if ch.lower()=="l":
                live_audio_to_morse()
            elif ch.lower()=="r":
                aud= input("Please provide a path for the audio file:")
                speech_to_audio(aud)
            else:
                print("Invalid Input!")
        elif opt.lower()=="m":
            mes=input("Please type the message:")
            audible_dot_and_dash(mes)
        else:
            print("Incorrect Input!")
    elif choice.lower()=="d":
        mes2=input("Please type the message:")
        mor_to_eng(mes2)
    else:
        print("Incorrect Input! Please Try Again.")
final_func()

        