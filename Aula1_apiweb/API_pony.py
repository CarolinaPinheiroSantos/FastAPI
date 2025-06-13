import requests
import json
from io import BytesIO
import matplotlib.pyplot as plt
from PIL import Image

pony = requests.get("https://ponyapi.net/v1/character/all")
pony = pony.json()

def personagem():
    saudacao = input("\n \nOiiiii, vamos descobrir qual personagenm de my little poney você é!!!!!!!!\n Esta preparado?(DIZ QUE sim): ")
    if saudacao != "sim" and saudacao != "s":
        input("FALEI PRA FALAR QUE SIM \n Esta preparado?(DIZ QUE sim): ")
    else:
        opcao = int(input("Digite um numero e irá descobrir: "))
        opcao -= 1
        print(f"Você é {pony['data'][opcao]['name']}")
        
        url = pony['data'][opcao]['image'][0]
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        plt.imshow(img)
        plt.axis('off')  
        plt.show()
        
personagem()