# autobiblia
README - Explicação do Código

Este arquivo fornece uma explicação do código Python que envolve a leitura de piadas de um arquivo de texto e a simulação de digitação de piadas ou trechos de texto aleatórios usando a biblioteca `keyboard`. O código foi dividido em várias partes, e cada parte será explicada abaixo.

1. Leitura das Piadas do Arquivo:
   - A função `ler_piadas_de_arquivo(nome_arquivo)` é usada para ler as piadas de um arquivo de texto especificado (`'biblia/piadas.txt'`) e armazená-las em uma lista.
   - As piadas são lidas do arquivo e divididas em linhas usando `conteudo.split('\n')`, e, em seguida, as aspas duplas são removidas de cada linha para limpar os dados.
   - O resultado final é uma lista chamada `piadas` contendo todas as piadas lidas do arquivo.

2. Execução do Macro:
   - A função `execute_macro()` é usada para ler um arquivo de texto (`'biblia/data.txt'`) e encontrar trechos de texto entre as aspas duplas usando expressões regulares (`re.findall(r'"(.*?)"', texto)`).
   - Se houver trechos de texto entre as aspas, o código seleciona aleatoriamente um desses trechos e simula a digitação desse texto usando a biblioteca `keyboard.write()`.
   - Isso permite que o código simule a digitação de trechos aleatórios de texto entre as aspas sempre que o macro é ativado.

3. Escrita de Piadas:
   - A função `escrever_piada()` é usada para selecionar aleatoriamente uma piada da lista de piadas lidas do arquivo e, em seguida, simular a digitação dessa piada usando `keyboard.write()`.
   - Isso permite que o código solte piadas aleatórias sempre que a tecla de ativação for pressionada.

4. Ativação do Macro e da Piada:
   - Duas teclas de ativação são definidas: `ctrl+x` para ativar o macro e `ctrl+q` para soltar uma piada.
   - Manipuladores de eventos são registrados para essas teclas de ativação usando `keyboard.add_hotkey()`.

5. Mensagens para o Usuário:
   - Mensagens informativas são exibidas para o usuário para indicar como ativar o macro e soltar uma piada.
   - O programa aguarda até que uma das teclas de ativação seja pressionada, e então executa a ação correspondente.

Este código é projetado para fornecer uma maneira divertida de simular a digitação de piadas ou trechos de texto aleatórios e pode ser personalizado para adicionar mais piadas ao arquivo de texto ou ajustar as teclas de ativação conforme necessário.

Divirta-se! 😄
