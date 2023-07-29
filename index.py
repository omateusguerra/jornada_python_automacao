# Passo a passo do projeto:

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

#pyautogui.write -> Escrever textos
#pyautogui.click -> Click em botões e links
#pyautogui.press -> Apertar uma tecla
#pyautogui.PAUSE = 0.5 -> Tempo de espera entre os comandos
#pyautogui.hotkey("crtl", "z") -> Combinação de teclas

pyautogui.PAUSE = 0.7
# Passo 1.1: Abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 1.2: Entrar no link
time.sleep(3)
pyautogui.click(x=923, y=56)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login

# Passo 2.1: Clicar no campo de email
pyautogui.click(x=847, y=363)

# Passo 2.2: Digitar email
pyautogui.write("mateus@gmail.com")

# Passo 2.3: Clicar no campo de senha
pyautogui.press("tab")

# Passo 2.4: Digitar senha
pyautogui.write("fgyudtuyfg")

# Passo 2.5: Clicar no botão de login
pyautogui.click(x=666, y=532)
time.sleep(3)


# Passo 3: Importar a base de produtos
# Passo 3.1: Importar pandas
tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar produto
for linha in tabela.index:
    # Passo 4.1: clicar no campo codigo
    pyautogui.click(x=842, y=248)
    # Passo 4.2: Pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # Passo 4.3: Preencher o campo
    pyautogui.write(str(codigo))
    # Passo 4.4: Ir para proxima linha e repetir passos anteriores
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # Passo 4.5: Tratar o erro quando um campo da tabela puder receber valores nulos
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    # Passo 4.6: Cadastrar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")


    # Passo 5: Repetir processo até cadastrar todos os produtos desejados
    # Passo 5.1: Dar um scroll(rolar) até em cima
    pyautogui.scroll(5000)
    # Passo 5.2: Criar um laço de repetição no passo 4

    # tabela.index = Índice da tabela