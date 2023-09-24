# Assistente pessoal criado com Chat GPT e Python 

Nesse texto vou comentar mais sobre o **Raves**, o assistente pessoal que eu criei utilizando o CHAT GPT e python. 

# 1. Como funciona? 

![image](https://github.com/GuiGrecov/ASSISTENTEPESSOAL-CHATGPT/assets/94385953/6cf7af7f-b274-492f-9d1c-4f2b87c53e2a)

Como podemos ver na imagem acima o código tem 3 estruturas básicas: 
- Leitura do áudio: Speech_Recognition
- Inteligência (Machine Learning): Chat GPT utilizando a biblioteca da Openai
- Saída do som: pyttsx3 - nessa parte tem como brincar mais, há a possibilidade da saída do som ser a voz de outra pessoa, por ser mais simpoles eu coloquei a voz presente no meu computador.

# 2. O que eu imagino como futuro? 

Acredito que isso é um exemplo que facilmente conseguimos programar uma IA para falar com alguém utilizando o que já existe no mercado com um custo baixíssimo. Então eu vejo que no futura terá uma automatização maior nas áreas de Telemarketing. A Open AI lancou uma página focada para empresas, programarem soluções utilizando IA (então podemos imaginar que a empresa já almeja alcançar esse mercado no futuro). 

# 3. Sobre a API? 

![image](https://github.com/GuiGrecov/ASSISTENTEPESSOAL-CHATGPT/assets/94385953/66b843e9-3669-4a51-b469-c57003e708ed)

Essas duas funções exercem protagonismo no código. 

A função zerarMensagens - tem como foco enviar um prompt para a API dizendo que ele deve se comportar como um assisten virtual e se inspirar no Jarvis. 
Enquanto isso, a função generate_answer é a responsável por enviar a mensagem ao código, porém nessa função temos algumas variáveis importante: 
- model: seta que iremos utilizar o chat gpt 3.5
- messagens: envia a mensagem
- max_tokens: limitei o tamanho da resposta porque isso economiza custos da API
- temperature: responsável pela criatividade na resposta
- frequency_penalty: penalização nas palavras, penalizei em 25%, ou seja, não repete tanta as palavras. 
