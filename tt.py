import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Função para verificar login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    # Exemplo de usuário e senha padrão
    if usuario == "" and senha == "":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        login_janela.destroy()  # Fecha a tela de login
        abrir_tela_cadastro()   # Abre a tela de cadastro
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# Função para salvar os dados do usuário
def salvar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    
    if nome and idade and email and telefone:
        # Salvar os dados em um DataFrame pandas
        dados = {
            'Nome': [nome],
            'Idade': [idade],
            'Email': [email],
            'Telefone': [telefone]
        }
        df = pd.DataFrame(dados)
        
        # Verificar se o arquivo já existe
        if not os.path.exists('cadastros_ejc.xlsx'):
            # Se o arquivo não existe, criar um novo
            df.to_excel('cadastros_ejc.xlsx', index=False, engine='openpyxl')
        else:
            # Se o arquivo já existe, adicionar os novos dados ao final
            with pd.ExcelWriter('cadastros_ejc.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                # Encontrar a última linha e adicionar dados
                start_row = writer.sheets['Sheet1'].max_row
                df.to_excel(writer, index=False, header=False, startrow=start_row)
        
        messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
        
        # Limpar os campos
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Função para abrir a tela de cadastro
def abrir_tela_cadastro():
    global entry_nome, entry_idade, entry_email, entry_telefone
    
    # Configurações da janela de cadastro
    cadastro_janela = tk.Tk()
    cadastro_janela.title("Cadastro de Usuários - EJC")
    cadastro_janela.geometry("400x300")

    # Labels e Entry para nome
    label_nome = tk.Label(cadastro_janela, text="Nome:")
    label_nome.pack(pady=5)
    entry_nome = tk.Entry(cadastro_janela)
    entry_nome.pack(pady=5)

    # Labels e Entry para idade
    label_idade = tk.Label(cadastro_janela, text="Idade:")
    label_idade.pack(pady=5)
    entry_idade = tk.Entry(cadastro_janela)
    entry_idade.pack(pady=5)

    # Labels e Entry para email
    label_email = tk.Label(cadastro_janela, text="Email:")
    label_email.pack(pady=5)
    entry_email = tk.Entry(cadastro_janela)
    entry_email.pack(pady=5)

    # Labels e Entry para telefone
    label_telefone = tk.Label(cadastro_janela, text="Telefone:")
    label_telefone.pack(pady=5)
    entry_telefone = tk.Entry(cadastro_janela)
    entry_telefone.pack(pady=5)

    # Botão para salvar os dados
    botao_salvar = tk.Button(cadastro_janela, text="Salvar", command=salvar_dados)
    botao_salvar.pack(pady=20)

    # Iniciar o loop da janela de cadastro
    cadastro_janela.mainloop()

# Configurações da janela de login
login_janela = tk.Tk()
login_janela.title("Login - EJC")
login_janela.geometry("300x200")

# Labels e Entry para login
label_usuario = tk.Label(login_janela, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(login_janela)
entry_usuario.pack(pady=5)

label_senha = tk.Label(login_janela, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(login_janela, show="*")
entry_senha.pack(pady=5)

# Botão para login
botao_login = tk.Button(login_janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)

# Iniciar o loop principal da janela de login
login_janela.mainloop()
