from tkinter import *
from tkinter import ttk
from Usuarios import *
from tkinter import messagebox
from relatorio_usuario import gerar_relatorio

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="Id usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2, text="Buscar", command=self.buscarUsuario)
        self.busca.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefone_label = Label(self.janela4, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela4, width=30)
        self.telefone.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.email_label = Label(self.janela5, text="Email:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela5, width=30)
        self.email.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuario_label = Label(self.janela6, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela6, width=30)
        self.usuario.pack(side="left")

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senha_label = Label(self.janela7, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela7, width=30)
        self.senha.pack(side="left")

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.autentic = Label(self.janela8, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        self.janela9 = Frame(master)
        self.janela9["padx"] = 20
        self.janela9.pack(pady=5)

        self.botao = Button(self.janela9, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela9, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela9, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        self.voltar_botao = Button(self.janela9, width=10, text="Voltar", command=self.voltar)
        self.voltar_botao.pack(side="left")

        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack(pady=10)

        self.tree = ttk.Treeview(self.janela10, columns=("ID", "Nome", "Telefone", "Email", "Usuário"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.pack()

        self.relatorio_botao = Button(self.janela9, width=15, text="Gerar Relatório", command=self.gerarRelatorio)
        self.relatorio_botao.pack(side="left")

        self.atualizarTabela()
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def atualizarTabela(self):
        usu = Usuarios()
        usuarios = usu.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4]))

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        result = user.selectUser(idusuario)
        if "não encontrado" in result:
            messagebox.showwarning("Aviso", result)
        else:
            self.idusuario.delete(0, END)
            self.idusuario.insert(INSERT, user.idusuario)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.telefone.delete(0, END)
            self.telefone.insert(INSERT, user.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, user.email)
            self.usuario.delete(0, END)
            self.usuario.insert(INSERT, user.usuario)
            self.senha.delete(0, END)
            self.senha.insert(INSERT, user.senha)
            messagebox.showinfo("Busca", result)

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        result = user.insertUser()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        result = user.updateUser()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        result = user.deleteUser()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]
            dados = self.tree.item(item, 'values')
            self.idusuario.delete(0, END)
            self.idusuario.insert(0, dados[0])
            self.nome.delete(0, END)
            self.nome.insert(0, dados[1])
            self.telefone.delete(0, END)
            self.telefone.insert(0, dados[2])
            self.email.delete(0, END)
            self.email.insert(0, dados[3])
            self.usuario.delete(0, END)
            self.usuario.insert(0, dados[4])
        except IndexError:
            pass

    def voltar(self):
        self.master.destroy()  # Fecha a janela atual

    def gerarRelatorio(self):
        caminho_arquivo = "relatorio_usuarios.pdf"  # Caminho do arquivo do relatório
        gerar_relatorio(caminho_arquivo)
        messagebox.showinfo("Relatório", f"Relatório gerado com sucesso: {caminho_arquivo}")

