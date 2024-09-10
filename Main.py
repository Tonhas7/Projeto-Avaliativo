import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from Formulario import Application as UserForm
from Cidade import Cidade as Cidform
from Clientes import Cliente as Cliform


class MainMenu:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gestão")

        # Configura o menu principal
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Adiciona o menu de navegação
        self.navigation_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu Principal", menu=self.navigation_menu)

        # Adiciona as opções ao menu
        self.navigation_menu.add_command(label="Usuários", command=self.open_user_screen)
        self.navigation_menu.add_command(label="Cidades", command=self.open_city_screen)
        self.navigation_menu.add_command(label="Clientes", command=self.open_client_screen)
        self.navigation_menu.add_command(label="Sair", command=self.master.quit)

    def open_user_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = UserForm(self.new_window)

    def open_city_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Cidform(self.new_window)

    def open_client_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Cliform(self.new_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(master=root)
    root.mainloop()
