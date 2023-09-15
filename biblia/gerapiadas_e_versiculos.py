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

# Função para soltar uma piada do arquivo quando Ctrl + P é pressionado
def escrever_piada():
    piada_selecionada = random.choice(piadas).strip()
    print(f"Piada selecionada aleatoriamente: {piada_selecionada}")
    keyboard.write(piada_selecionada)

# Defina as teclas de ativação
tecla_macro = 'ctrl+x'
tecla_piada = 'ctrl+q'

# Registre manipuladores de eventos para as teclas de ativação
keyboard.add_hotkey(tecla_macro, execute_macro)
keyboard.add_hotkey(tecla_piada, escrever_piada)

print(f"Pressione a tecla {tecla_macro} para ativar o macro.")
print(f"Pressione a tecla {tecla_piada} para soltar uma piada.")

keyboard.wait()