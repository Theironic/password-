import random
import string
import json
while True:
    print("coloque a quantidade de letras,numeros e caract. especiais que voce quer \n")
    val= int(input("qntd de letras"))
    def gerar(strings:str ,ints:str,caracter:str)->str:
        numeros:list =list(string.digits)
        letras:list = list(string.ascii_letters)
        caracteres:list = list(string.punctuation)
        #embaralhando
        random.shuffle(numeros)
        random.shuffle(caracteres)
        random.shuffle(letras)
        
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



print(gerar(4,7,4))
