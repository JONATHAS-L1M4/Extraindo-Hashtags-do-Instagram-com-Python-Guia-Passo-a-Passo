import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

os.system('cls')

def hashtag(url):
    
    texto = []
    for u in tqdm(url):
        if "https" in u:
            response = requests.get(u)

            if response.status_code == 200:
                html_content = response.text
                soup = BeautifulSoup(html_content, "html.parser")
                full_text = list(set(soup.get_text().split()))

                for f in full_text:
                    if "#" in f:
                        texto.append(f)
                        texto = list(set(texto))
                    #if len(texto) < 29:
                        #break
            else:
                print(f"Falha na requisição: {response.status_code}")
    
    print(f"{len(texto)} encontradas.")
    return list(set(texto))

def txt():
    
    tags = ""
    arquivos_txt = [arquivo for arquivo in os.listdir('./') if arquivo.endswith('.txt')]

    for a in arquivos_txt:
        if a != "hashtag.txt":
            with open(a) as txt:
                links = list(set(txt.read().split()))
                hashtags = hashtag(links)

    for h in hashtags:
        tags += f"{h} "

    with open("hashtag.txt", 'w', encoding="utf-8") as txt:
        txt.write(tags)

if __name__ == "__main__":
    txt()