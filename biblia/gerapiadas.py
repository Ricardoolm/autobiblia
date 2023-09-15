import re
import random
import keyboard

# Função para ler as piadas de um arquivo
def ler_piadas_de_arquivo(nome_arquivo):
    piadas = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            piadas = conteudo.split('\n')
            piadas = [piada.strip('"\n') for piada in piadas if piada.strip()]
    except FileNotFoundError:
        pass
    return piadas
# Lista de piadas lidas do arquivo
piadas = ler_piadas_de_arquivo('biblia/piadas.txt')
def escrever_piada():
    piada_selecionada = random.choice(piadas).strip()
    print(f"Piada selecionada aleatoriamente: {piada_selecionada}")
    keyboard.write(piada_selecionada)

# Defina as teclas de ativação
tecla_piada = 'ctrl+q'

# Registre manipuladores de eventos para as teclas de ativação
keyboard.add_hotkey(tecla_piada, escrever_piada)
print(f"Pressione a tecla {tecla_piada} para soltar uma piada.")

keyboard.wait()