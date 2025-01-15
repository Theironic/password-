
import flet as ft
import typing

qntd_input = ft.TextField("numeros")
btn_gera = ft.ElevatedButton("gerar senha")
main_texto= ft.Text("hello world",size=50,color="#003F91",font_family="Courier")



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
