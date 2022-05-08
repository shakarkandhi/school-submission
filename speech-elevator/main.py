import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
while(1):
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        inp=r.recognize_google(audio)
        print(inp)
        if('1st floor' in inp.lower() or 'first floor'  in inp.lower() or 'pahli manjil'  in inp.lower() or 'pahli manzil'  in inp.lower() or '1'  in inp.lower()):
            print('Going To 1st Floor')
        if('2nd floor'  in inp.lower() or 'second floor' in inp.lower() or 'dusri manjil'  in inp.lower() or 'dusri manzil'  in inp.lower() or '2' in inp.lower()):
            print('Going To 2nd Floor')
        if('3rd floor'  in inp.lower() or 'third floor' in inp.lower() or 'teesri manjil'  in inp.lower() or 'teesri manzil'  in inp.lower() or '3'  in inp.lower()):
            print('Going To 3rd Floor')
        if('4th floor' in inp.lower() or 'fourth floor' in inp.lower() or 'chauthi manjil' in inp.lower() or  'chauthi mazjil' in inp.lower() or '4' in inp.lower()):
            print('Going To 4th Floor')
    except KeyboardInterrupt:
        break
    except:
        pass