import re
import random
import keyboard

#CODIGO PARA USAR SOMENTE A BIBLIA
def execute_macro():
    # Abra o arquivo TXT
    with open('biblia/data.txt', 'r', encoding='utf-8') as arquivo:
        # Leia o conteúdo do arquivo
        texto = arquivo.read()

    # Use regex para encontrar todos os textos entre as aspas
    textos_entre_aspas = re.findall(r'"(.*?)"', texto)

    # Verifique se há textos entre as aspas encontrados
    if textos_entre_aspas:
        # Selecione um texto aleatoriamente
        texto_selecionado = random.choice(textos_entre_aspas)
        print(f"Texto selecionado aleatoriamente: {texto_selecionado}")

        # Simule a digitação do texto
        keyboard.write(texto_selecionado)
        print("Texto digitado usando o macro.")
    else:
        print("Nenhum texto entre as aspas encontrado no arquivo.")

# Defina a tecla que acionará o macro
tecla_ativacao = 'ctrl+x'

# Registre um manipulador de eventos para a tecla de ativação
keyboard.add_hotkey(tecla_ativacao, execute_macro)

print(f"Pressione a tecla {tecla_ativacao} para ativar o macro.")

keyboard.wait()  