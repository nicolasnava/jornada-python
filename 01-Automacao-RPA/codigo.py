# Logica de automacao para cadastro de produtos em sistema de empresa
# Bibliotecas = Pacotes de Codigo Prontos

#   Passo a passo:
#       Passo 1 : Entra Sistema Empresa
#       Passo 2 : Fazer Login
#       Passo 3 : Abrir base de dados
#       Passo 4 : Cadastrar Produto
#       Passo 5 : Repetir passo 4 ate terminar lista de produtos

import pyautogui
import time 
# pyautogui.click -> clicar
# pyautogui.write -> digitar
# pyautogui.press -> pressionar
# pyautogui.hotkey -> atalho_teclado

pyautogui.PAUSE = 1  # Tempo de espera entre as acoes   
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1 : Entra Sistema Empresa
pyautogui.press("win")  # Abre o menu iniciar
pyautogui.write("brave")  # Digita o nome do navegador
pyautogui.press("enter")  # Pressiona enter para abrir o navegador
time.sleep(2)  # Espera o navegador abrir

# entrar no link 
pyautogui.write(link)  # Digita o endereco do sistema
pyautogui.press("enter")  # Pressiona enter
time.sleep(2)  # Espera a pagina carregar

# Passo 2 : Fazer Login 
pyautogui.click(x=409, y=403) # Clica no campo de email
pyautogui.write("nicolasnava@gmail.com")  # Digita o email
pyautogui.press("tab")  # Passa para o campo de senha
pyautogui.write("1234")  # Digita a senha
pyautogui.click(x=667, y=562)  # Clica no botao de login


#install pandas openpyxl
import pandas as pd


# Passo 4 : Cadastrar Produto
tabela = pd.read_csv("produtos.csv")

print(tabela)
for linha in tabela.index:
    # Codigo
    pyautogui.click(x=411, y=286)  # Clica no campo codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))  # Preenche o campo codigo
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))  # Preenche o campo marca
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))  # Preenche o campo tipo
    pyautogui.press("tab")

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))  # Preenche o campo categoria
    pyautogui.press("tab")

    # Preco Unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))  # Preenche o campo preco unitario
    pyautogui.press("tab")

    # Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))  # Preenche o campo custo
    pyautogui.press("tab")

    # Observacao
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))  # Preenche o campo observacao
    pyautogui.press("tab")

    pyautogui.click(x=595, y=578)  # Clica no botao salvar

    pyautogui.scroll(5000)
