O que o script faz:
1. Faz requisições para uma lista de URLs.
2. Extrai todo o texto das páginas e busca por hashtags.
3. Coleta até 30 hashtags únicas por página.
4. Lê arquivos `.txt` no diretório atual que contêm listas de URLs.
5. Salva todas as hashtags coletadas em um arquivo chamado `hashtag.txt`.

Bibliotecas Utilizadas:
- `requests`: Para realizar requisições HTTP.
- `BeautifulSoup`: Para parsear o HTML.
- `tqdm`: Para exibir barras de progresso.
- `os`: Para manipulação de arquivos do sistema.

Instalação das Bibliotecas:

Antes de começar, instale as bibliotecas necessárias usando os seguintes comandos:

pip install requests
pip install beautifulsoup4
pip install tqdm
