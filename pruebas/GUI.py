import FreeSimpleGUI as sg

def crear_ventana():
    layout = [
        [sg.Text("Hola, esta es la interfaz gráfica")],
        [sg.Button("Salir")]
    ]
    
    window = sg.Window("Mi Aplicación", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Salir":
            break
    
    window.close()

# Esto evita que se ejecute si se importa en otro archivo
if __name__ == "__main__":
    crear_ventana()