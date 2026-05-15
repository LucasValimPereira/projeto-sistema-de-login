import customtkinter as ctk

# configuração aparencia
ctk.set_appearance_mode('dark')

# Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #verificar o ususario e senha
    if usuario == 'lucas' and senha == 'admin123':
        resultado_login.configure(text='Login bem-sucedido!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

# Criação da janela principal
app=ctk.CTk()
app.title('login')
app.geometry('400x300')

# Criação dos campos
# Label
label_usuario=ctk.CTkLabel(app, text='Usuário: ')
label_usuario.pack(pady=10)

# Entry - Campo de texto
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

#label
label_usuario=ctk.CTkLabel(app, text='Senha: ')
label_usuario.pack(pady=10)

# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# Button
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

resultado_login=ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# Inicia aaplicação
app.mainloop()