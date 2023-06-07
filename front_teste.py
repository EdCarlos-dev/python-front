
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

import pandas as pd
import os

root = customtkinter.CTk()
root.geometry("500x450")

def get_client_info():
    name = entry0.get()
    email = entry1.get()
    telefone = entry2.get()
    celular = entry3.get()
    caixa_postal = checkbox.get()

    if not entry0.get():
        name = ''
    if not  entry1.get():
        email = ''
    if not entry2.get():
        telefone = ''
    if not entry3.get():
        celular = ''
      
    client_list.append((name, email, telefone, celular, caixa_postal))
    return client_list

def clear_input():
    entry0.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    checkbox.deselect()

def save_client():
    cliente = get_client_info()
    df_cliente = pd.DataFrame(cliente, columns = ['Nome', 'E-mail', 'Telefone', 'Celular', 'Caixa-Postal'])
    df_cliente.to_csv('clienteInfo.tsv', sep='\t', index=False)
    clear_input()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Informações Cliente', font=("Roboto",24))
label.pack(pady=12, padx=10)

client_list = []

entry0 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome Cliente")
entry0.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="E-mail Cliente")
entry1.pack(pady=12, padx=10)


entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Telefone")
entry2.pack(pady=12, padx=10)


entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Celular")
entry3.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text = 'Caixa postal?')
checkbox.pack(pady=12, padx=10)


button = customtkinter.CTkButton(master=frame, text="Salvar informações", command=save_client)
button.pack(pady=12, padx=10)


root.mainloop()