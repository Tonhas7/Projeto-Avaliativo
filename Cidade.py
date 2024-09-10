from tkinter import *
from tkinter import ttk
from apliCidade import Cidades
from tkinter import messagebox
from Banco import Banco
from Clientes import Clientes
from relatorio_cidade import gerar_relatorio

class Cidade:
    def __init__(self, master=None):
        self.master = master
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcidade_label = Label(self.janela22, text="Id cidade:")
        self.idcidade_label.pack(side="left")
        self.idcidade = Entry(self.janela22, width=20)
        self.idcidade.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCidade)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.cidade_label = Label(self.janela23, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade = Entry(self.janela23, width=30)
        self.cidade.pack(side="left")

        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack(pady=5)

        self.uf_label = Label(self.janela24, text="UF:")
        self.uf_label.pack(side="left")
        self.uf = Entry(self.janela24, width=28)
        self.uf.pack(side="left")

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack()

        self.autentic = Label(self.janela25, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Adicionando os botões para Inserir, Alterar e Excluir
        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCidade)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCidade)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCidade)
        self.botao3.pack(side="left")

        self.voltar_botao = Button(self.janela11, width=10, text="Voltar", command=self.voltar)
        self.voltar_botao.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID","Cidade","UF"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.pack()

        self.relatorio_botao = Button(self.janela11, width=15, text="Gerar Relatório", command=self.gerarRelatorio)
        self.relatorio_botao.pack(side="left")

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        # Bind da função para preencher entradas com seleção do Treeview
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def atualizarTabela(self):
        cid = Cidades()
        cidades = cid.selectAllCidades()
        self.tree.delete(*self.tree.get_children())
        for c in cidades:
            self.tree.insert("", "end", values=(c[0], c[1], c[2]))

    def buscarCidade(self):
        cid = Cidades()
        idcidade = self.idcidade.get()
        result - cid.selectCidade(idcidade)
        if "não encontrado" in result:
            messagebox.showwarning("Aviso", result)
        else:
            self.autentic["text"] = cid.selectCidade(idcidade)
            self.idcidade.delete(0, END)
            self.idcidade.insert(INSERT, cid.idcidade)
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, cid.cidade)
            self.uf.delete(0, END)
            self.uf.insert(INSERT, cid.uf)
            messagebox.showinfo("Busca", result)

    def inserirCidade(self):
        cid = Cidades(cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.insertCidade()
        messagebox.showinfo("Resultado", result)
        self.autentic["text"] = result
        self.atualizarTabela()

    def alterarCidade(self):
        cid = Cidades(idcidade=self.idcidade.get(), cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.updateCidade()
        messagebox.showinfo("Resultado", result)
        self.autentic["text"] = result
        self.atualizarTabela()

    def excluirCidade(self):
        cidade = self.cidade.get()  # Corrigido para self.usuario.get()

        banco = Banco()
        cursor = banco.conexao.cursor()

        # Verificando se o usuário e a senha estão corretos
        cursor.execute("SELECT * FROM tbl_clientes WHERE cidade=?", (cidade,))
        engual = cursor.fetchone()

        if engual:
            messagebox.showinfo("Erro", "Nao pode ser excluida!")
        else:
            cid = Cidades(idcidade=self.idcidade.get())
            result = cid.deleteCidade()
            if result:
                messagebox.showerror("Excluir", "Excluido com sucesso!")

            else:
                messagebox.showerror("Erro", "erro ao excluir!")
            self.atualizarTabela()
        cursor.close()

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]  # Pega o item selecionado
            dados = self.tree.item(item, 'values')  # Obtém os valores do item

            # Preenche os campos de entrada com os dados
            self.idcidade.delete(0, END)
            self.idcidade.insert(0, dados[0])
            self.cidade.delete(0, END)
            self.cidade.insert(0, dados[1])
            self.uf.delete(0, END)
            self.uf.insert(0, dados[2])
        except IndexError:
            pass  # Nenhum item selecionado

    def voltar(self):
        self.master.destroy()  # Fecha a janela atual

    def gerarRelatorio(self):
        caminho_arquivo = "relatorio_cidade.pdf"  # Caminho do arquivo do relatório
        gerar_relatorio(caminho_arquivo)
        messagebox.showinfo("Relatório", f"Relatório gerado com sucesso: {caminho_arquivo}")
