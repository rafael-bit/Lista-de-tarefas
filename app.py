import tkinter as tk
from tkinter import messagebox

class ListaDeTarefasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        self.tarefas = []
        self.tarefa_entry = tk.Entry(root, width=40)
        self.adicionar_button = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.remover_button = tk.Button(root, text="Remover Tarefa", command=self.remover_tarefa)
        self.tarefa_entry.pack(pady=10)
        self.adicionar_button.pack(pady=5)
        self.listbox.pack(pady=10)
        self.remover_button.pack(pady=5)
        self.atualizar_listbox()

    def adicionar_tarefa(self):
        tarefa = self.tarefa_entry.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.atualizar_listbox()
            self.tarefa_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo Vazio", "Por favor, insira uma tarefa.")

    def remover_tarefa(self):
        selecionado = self.listbox.curselection()
        if selecionado:
            indice = selecionado[0]
            del self.tarefas[indice]
            self.atualizar_listbox()
        else:
            messagebox.showwarning("Nenhuma Tarefa Selecionada", "Por favor, selecione uma tarefa para remover.")

    def atualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.listbox.insert(tk.END, tarefa)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTarefasApp(root)
    root.mainloop()
