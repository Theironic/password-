import random
import string
import json

error_msg:str = "valor inserido incorreto \n"

def gerar(tamanho:int )->str:
        
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

        # Concatenação das strings
        senha_lista:list = list(numeros_string+ letras_string + caracteres_string )
        random.shuffle(senha_lista)
        #print(len(senha_lista))
        #senha gerada 
        senha_gerada:str = "".join(senha_lista)
        #criacao de arquivo json para visualizar o historico de senhas(nao seguro)
        logs:dict= {"senha": senha_gerada[:tamanho],
                    }
        with open("senhas.json","a") as f:
            f.write(json.dumps(logs) + "\n")
        return senha_gerada[:tamanho]
