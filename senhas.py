import random
import string
import json

error_msg:str = "valor inserido incorreto \n"

def gerar(strings:str ,ints:str,caracter:str)->str:
        
        numeros:list =list(string.digits)
        letras:list = list(string.ascii_letters)
        caracteres:list = list(string.punctuation)
        #embaralhando
        random.shuffle(numeros)
        random.shuffle(caracteres)
        random.shuffle(letras)

        #convertendo para string
        numeros_string:str = "".join(map(str,numeros))
        caracteres_string:str = "".join(caracteres)
        letras_string:str = "".join(letras)

        senha_lista:list = list(numeros_string[:ints]+ letras_string[:strings] + caracteres_string[:caracter] )
        random.shuffle(senha_lista)
        senha_gerada:str = "".join(senha_lista)

        logs:dict= {"senha": senha_gerada}
        with open("senhas.json","a") as f:
            f.write(json.dumps(logs) + "\n")

        return senha_gerada

while True:
    print("coloque a quantidade de letras,numeros e caract. especiais que voce quer \n")
    try:
        letras_qntd= int(input("qntd de letras: "))
        numeros_qntd= int(input("qntd de numeros: "))
        caracteres_qntd= int(input("qntd de caract. especiais: "))
    except ValueError:
        print(error_msg)
        continue
    print(gerar(letras_qntd,numeros_qntd,caracteres_qntd))
    
    break;