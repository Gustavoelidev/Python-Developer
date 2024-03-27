import tkinter as tk

# criando a janela

window = tk.Tk()
window.geometry('500x500')
window.title("Gerenciador de Frases")



# adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# adicionando o label

label = tk.Label(frame, text="Hello World")
label.pack(fill='x', expand=True)

# adicionando o input

frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)


frase_in = tk.Entry(frame)
frase_in.pack(fill='x', expand=True)

# funcao label

def click():
    label.config(text=frase_in.get())

#adicionando botao

button = tk.Button(frame, text="Enviar", command=click)
button.pack()






window.mainloop()