from gtts import gTTS


#███████╗░█████╗░██████╗░░██████╗███████╗███████╗████████╗████████╗░██████╗               ForseeTTS
#██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝               Developed by: ForseeGab
#█████╗░░██║░░██║██████╔╝╚█████╗░█████╗░░█████╗░░░░░██║░░░░░░██║░░░╚█████╗░               What is?:Free & open source TTS service 
#██╔══╝░░██║░░██║██╔══██╗░╚═══██╗██╔══╝░░██╔══╝░░░░░██║░░░░░░██║░░░░╚═══██╗
#██║░░░░░╚█████╔╝██║░░██║██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░██████╔╝
#╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═════╝░


from playsound import playsound

audio ='speech.mp3'
#SELECT THE LEANGUAGE#
language = 'en'
sp = gTTS(text = "Insert Text HERE", lang= language,slow=False)

sp.save(audio)
playsound(audio)
