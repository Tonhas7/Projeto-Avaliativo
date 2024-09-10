from tkinter import *
from tkinter import ttk
from apliClientes import Clientes
from tkinter import messagebox
from Banco import Banco
from relatorio_cliente import gerar_relatorio  # Importa a função para gerar relatórios

class Cliente:
    def __init__(self, master=None):
        self.master = master
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados do Cliente:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcliente_label = Label(self.janela22, text="ID Cliente:")
        self.idcliente_label.pack(side="left")
        self.idcliente = Entry(self.janela22, width=20)
        self.idcliente.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCliente)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.nome_label = Label(self.janela23, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela23, width=30)
        self.nome.pack(side="left")

        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack()

        self.cidade_label = Label(self.janela24, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade_combobox = ttk.Combobox(self.janela24, width=27)
        self.cidade_combobox.pack(side="left")
        self.carregarCidades()  # Carregar cidades na Combobox

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack(pady=5)

        self.nascimento_label = Label(self.janela25, text="Nascimento:")
        self.nascimento_label.pack(side="left")
        self.nascimento = Entry(self.janela25, width=28)
        self.nascimento.pack(side="left")

        self.janela26 = Frame(master)
        self.janela26["padx"] = 20
        self.janela26.pack()

        self.cpf_label = Label(self.janela26, text="CPF:")
        self.cpf_label.pack(side="left")
        self.cpf = Entry(self.janela26, width=30)
        self.cpf.pack(side="left")

        self.janela27 = Frame(master)
        self.janela27["padx"] = 20
        self.janela27.pack()

        self.genero_label = Label(self.janela27, text="Gênero:")
        self.genero_label.pack(side="left")
        self.genero = Entry(self.janela27, width=30)
        self.genero.pack(side="left")

        self.janela28 = Frame(master)
        self.janela28["padx"] = 20
        self.janela28.pack()

        self.autentic = Label(self.janela28, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCliente)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCliente)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCliente)
        self.botao3.pack(side="left")

        # Adicionando o botão Voltar
        self.voltar_botao = Button(self.janela11, width=10, text="Voltar", command=self.voltar)
        self.voltar_botao.pack(side="left")

        # Adicionando o botão para gerar o relatório
        self.relatorio_botao = Button(self.janela11, width=15, text="Gerar Relatório", command=self.gerarRelatorio)
        self.relatorio_botao.pack(side="left")

        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Nascimento", "CPF", "Gênero", "Cidade"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Nascimento", text="Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Gênero", text="Gênero")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.pack()

        self.atualizarTabela()
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def carregarCidades(self):
        cli = Clientes()
        cidades = cli.selectCidades()
        self.cidade_combobox['values'] = cidades

    def atualizarTabela(self):
        cli = Clientes()
        clientes = cli.selectAllClientes()
        self.tree.delete(*self.tree.get_children())
        for c in clientes:
            self.tree.insert("", "end", values=(c[0], c[1], c[2], c[3], c[4], c[5]))

    def buscarCliente(self):
        cli = Clientes()
        idcliente = self.idcliente.get()
        result = cli.selectCliente(idcliente)
        if "não encontrado" in result:
            messagebox.showwarning("Aviso", result)
        else:
            self.idcliente.delete(0, END)
            self.idcliente.insert(INSERT, cli.idcliente)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, cli.nome)
            self.nascimento.delete(0, END)
            self.nascimento.insert(INSERT, cli.nascimento)
            self.cpf.delete(0, END)
            self.cpf.insert(INSERT, cli.cpf)
            self.genero.delete(0, END)
            self.genero.insert(INSERT, cli.genero)
            self.cidade_combobox.set(cli.cidade)
            messagebox.showinfo("Busca", result)

    def inserirCliente(self):
        cli = Clientes(nome=self.nome.get(), nascimento=self.nascimento.get(), cpf=self.cpf.get(),
                       genero=self.genero.get(), cidade=self.cidade_combobox.get())
        result = cli.insertCliente()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def alterarCliente(self):
        cli = Clientes(idcliente=self.idcliente.get(), nome=self.nome.get(), nascimento=self.nascimento.get(),
                       cpf=self.cpf.get(), genero=self.genero.get(), cidade=self.cidade_combobox.get())
        result = cli.updateCliente()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def excluirCliente(self):
        cli = Clientes(idcliente=self.idcliente.get())
        result = cli.deleteCliente()
        messagebox.showinfo("Resultado", result)
        self.atualizarTabela()

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]
            dados = self.tree.item(item, 'values')
            self.idcliente.delete(0, END)
            self.idcliente.insert(0, dados[0])
            self.nome.delete(0, END)
            self.nome.insert(0, dados[1])
            self.nascimento.delete(0, END)
            self.nascimento.insert(0, dados[2])
            self.cpf.delete(0, END)
            self.cpf.insert(0, dados[3])
            self.genero.delete(0, END)
            self.genero.insert(0, dados[4])
            self.cidade_combobox.set(dados[5])
        except IndexError:
            pass

    def voltar(self):
        self.master.destroy()  # Fecha a janela atual

    def gerarRelatorio(self):
        caminho_arquivo = "relatorio_clientes.pdf"  # Caminho do arquivo do relatório
        gerar_relatorio(caminho_arquivo)
        messagebox.showinfo("Relatório", f"Relatório gerado com sucesso: {caminho_arquivo}")

