import speech_recognition as sr
def speech_writer():
    '''
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as audio_file:
        r.adjust_for_ambient_noise(audio_file)
        print("говорите")
        audio = r.listen(audio_file)
        try:
            input_text = r.recognize_google(audio,  language="ru")

        except:
            input_text = ''
    '''
    input_text = input('Человек: ')
    #print('Человек: ', input_text)
    return input_text.lower()

def keyword(x):
    sub = x.find("кеша")
    if sub == 0:
        x = x[(sub + 4) :]
        print('Обрабатываю ', x)
    else:
        x = x[:(sub-1)] + x[(sub + 4):]
        print('Обрабатываю ' + x)
    return(x)

while True:
    k = speech_writer()
    keyword(k)