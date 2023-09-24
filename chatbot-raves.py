#!/usr/bin/env python
# coding: utf-8

# # code

# In[ ]:


import speech_recognition as sr
import pyttsx3
import openai

key = "XXX"

openai.api_key = key

speaker = pyttsx3.init()
   
voices = speaker.getProperty("voices")
   
for voice in voices:
    print(voice, voice.id) #traz os idiomas de voz instalados em sua maquina

speaker.setProperty("voice",  1)
speaker.setProperty("rate", 200)



def ouvir_microfone():
   
    #usando o microfone
    microfone = sr.Recognizer()

   
    with sr.Microphone() as source:
       
        #chama um algoritmo de redução de ruídos
        microfone.adjust_for_ambient_noise(source)
       
        print("Fale alguma coisa: ")
        speaker.say("Como posso lhe ajudar?")
        speaker.runAndWait()
       
        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)

       
        try:
           
            #Passa a variável paa o algoritmo reconhecedor de padrões
            frase = microfone.recognize_google(audio,language="pt-BR")
           
            #Retorna a frase pronunciada
            print("Você disse: "  + frase)
           
       
        #Senão funcionou
        except sr.UnkownValueError:
            print("Não Entendi")
           
           
        return frase



def zerarMensagens():
    return [{"role": "system", "content": "Você é uma Inteligência Artifical generativa e foi criado pelo Guilherme. Você é inspirada no Jarvis. Você é gentil e educado na resposta. Você se chama Raves"}]

def generate_answer(messages):
    try:
        response = openai.ChatCompletion.create(
            #model="gpt-4",
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=250,
            temperature=1,
            top_p=0.5,
            frequency_penalty=0.25,
            presence_penalty=0.25
        )
        return [response.choices[0].message.content, response.usage]
    except Exception as e:
        print("Deu ruim", e)
        return ["", ""]

speaker.say("Olá eu sou o Raves - um robô feito por meio de Inteligência Artificial.")
speaker.runAndWait()

while True:
   

    print(50*"x")
    prompt = ouvir_microfone()
   
    print("-")
    print("----")
    print("Raves está processando a mensagem")
   
    mensagens = zerarMensagens()
    mensagens.append({"role": "user", "content": str(prompt)})
    answer = generate_answer(mensagens)

    print(50*"x")
    response = answer[0]
    print(response)
    print("")
    print(50*"x")
   
    speaker.say(response)
    speaker.runAndWait()


# In[ ]:


pip install pyaudio


# In[ ]:




