import flet as ft
from typing import NewType
# tipagem
TextField = NewType('TextField', str)
ElevatedButton = NewType("ElevatedButton", str)
Text = NewType("Text",str)

#variaveis de interface
qntd_input: TextField= ft.TextField("numeros")
btn_gera: ElevatedButton = ft.ElevatedButton("gerar senha")
main_texto: Text = ft.Text("hello world",size=50,color="#003F91",font_family="Courier")


# main interface
def main(page: ft.Page):
    def btn_gerar(e)->None:
        
        pass
    page.add(
        ft.Column(
            [   #linha comeca aqui
                main_texto,
                qntd_input,
                btn_gera
                
                
            ]
            
        )

    )


ft.app(main)
