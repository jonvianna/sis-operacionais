import tkinter as tk
from tkinter import messagebox

# Cria um dicionário com a lista de livros e suas quantidades em estoque e seus preços
estoque = {'Livro 1': {'quantidade': 10, 'preco': 20.0},
           'Livro 2': {'quantidade': 15, 'preco': 15.0},
           'Livro 3': {'quantidade': 5, 'preco': 25.0}}

# Define a função que será executada quando o botão "Realizar Venda" for clicado
def realizar_venda():
    livro = livro_entry.get()
    quantidade = int(quantidade_entry.get())
    preco_unitario = estoque[livro]['preco']
    preco_total = quantidade * preco_unitario
    dinheiro_recebido = float(dinheiro_entry.get())
    troco = dinheiro_recebido - preco_total
    if livro in estoque and estoque[livro]['quantidade'] >= quantidade and troco >= 0:
        estoque[livro]['quantidade'] -= quantidade
        messagebox.showinfo('Venda realizada com sucesso!', f'Foram vendidos {quantidade} unidades do livro {livro}.\n'
                                                             f'Preço total: R${preco_total:.2f}\n'
                                                             f'Dinheiro recebido: R${dinheiro_recebido:.2f}\n'
                                                             f'Troco: R${troco:.2f}')
        atualizar_estoque()
    else:
        mensagem_label.config(text=f'Não foi possível realizar a venda do livro {livro}.')

# Define uma função que atualiza o estoque exibido na interface
def atualizar_estoque():
    estoque_texto = ''
    for livro, dados in estoque.items():
        estoque_texto += f'{livro}: {dados["quantidade"]} unidades, R${dados["preco"]:.2f} cada\n'
    estoque_label.config(text=estoque_texto)

# Cria a janela da aplicação
janela = tk.Tk()
janela.title('Livraria')

# Cria os widgets da interface
livro_label = tk.Label(janela, text='Livro:')
livro_entry = tk.Entry(janela)
quantidade_label = tk.Label(janela, text='Quantidade:')
quantidade_entry = tk.Entry(janela)
dinheiro_label = tk.Label(janela, text='Dinheiro Recebido:')
dinheiro_entry = tk.Entry(janela)
vender_button = tk.Button(janela, text='Realizar Venda', command=realizar_venda)
estoque_label = tk.Label(janela, text='')
mensagem_label = tk.Label(janela, text='')

# Posiciona os widgets na interface
livro_label.grid(row=0, column=0)
livro_entry.grid(row=0, column=1)
quantidade_label.grid(row=1, column=0)
quantidade_entry.grid(row=1, column=1)
dinheiro_label.grid(row=2, column=0)
dinheiro_entry.grid(row=2, column=1)
vender_button.grid(row=3, column=1)
estoque_label.grid(row=4, column=0, columnspan=2)
mensagem_label.grid(row=5, column=0, columnspan=2)

# Atualiza o estoque exibido na interface
atualizar_estoque()

# Inicia o loop principal
janela.mainloop()