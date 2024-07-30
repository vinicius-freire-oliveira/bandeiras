import requests
import csv

def obter_bandeiras():
    url = 'https://restcountries.com/v3.1/all'
    resposta = requests.get(url)
    dados = resposta.json()

    with open('bandeiras_paises.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['País', 'Código ISO', 'Bandeira'])

        for pais in dados:
            nome_pais = pais.get('name', {}).get('common', '')
            codigo_iso = pais.get('cca2', '')
            bandeira = pais.get('flags', {}).get('png', '')

            escritor.writerow([nome_pais, codigo_iso, bandeira])

if __name__ == "__main__":
    obter_bandeiras()
