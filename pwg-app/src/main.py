import flet as ft
from typing import NewType
from senhas import gerar



# tipagem
TextField = NewType('TextField', str)
ElevatedButton = NewType("ElevatedButton", str)
Text = NewType("Text",str)

#variaveis de interface
qntd_input: TextField= ft.TextField("", label="Tamanho da sua Senha",width=450,height=50)

main_texto: Text = ft.Text("Password Generator",size=50,color="#003F91",font_family="Courier")





# main interface
def main(page: ft.Page):
    def btn_gerar(e)->None:
        valor: int = int(qntd_input.value)
        qntd_input.value = gerar(valor)
        page.update()
    
    def copiar_texto(e)-> None:
        page.set_clipboard(qntd_input.value)
        qntd_input.value = ''
        page.update()

        
    texto: Text= ft.Text("")
    btn_gera: ElevatedButton = ft.ElevatedButton("Gerar Senha",on_click=btn_gerar, width=150,height=50)
    btn_copia: ElevatedButton = ft.ElevatedButton("copiar",width=95,height=50,on_click=copiar_texto)
    page.add(

        ft.Container (
            ft.Column(
            [   #linha comeca aqui
                main_texto,
                
                ft.Row(
                    [qntd_input, btn_copia,],
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
                
                btn_gera,
                texto
                
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            
            

        )

    ))


ft.app(main)
