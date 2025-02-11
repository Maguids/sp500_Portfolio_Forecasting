import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import os

# Passo 1: Obter a lista de empresas do S&P500 a partir da página da Wikipédia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar a tabela com as empresas
table = soup.find('table', {'class': 'wikitable'})

# Extrair os símbolos e nomes das empresas
tickers = []
company_names = []
for row in table.find_all('tr')[1:]:
    ticker = row.find_all('td')[0].text.strip()
    name = row.find_all('td')[1].text.strip()
    tickers.append(ticker)
    company_names.append(name)

# Definir o período de tempo (de 01-01-2010 até 31-01-2024)
start_date = "2010-01-01"
end_date = "2024-01-31"

# Caminho do arquivo CSV final
csv_file = 'sp500_all_data.csv'

# Criar o CSV com o cabeçalho antes de baixar os dados
header = ['Date', 'Close', 'Adj Close', 'High', 'Low', 'Open', 'Volume', 'Symbol', 'Name']
if not os.path.exists(csv_file):
    # Criar o arquivo CSV vazio com o cabeçalho
    pd.DataFrame(columns=header).to_csv(csv_file, mode='w', header=True, index=False)

# Função para baixar dados de cada empresa e salvar no arquivo CSV
def download_and_store_company_data(ticker, name):
    try:
        # Baixar dados históricos diários para o período definido
        data = yf.download(ticker, start=start_date, end=end_date)
        
        # Garantir que os dados estão corretos (não vazios)
        if data.empty:
            print(f"Sem dados para {ticker}.")
            return
        
        # Adicionar as colunas 'Symbol' e 'Name' aos dados
        data['Symbol'] = ticker
        data['Name'] = name
        
        # Resetar o índice, para garantir que `Date` se torne uma coluna normal
        data.reset_index(inplace=True)

        # Filtrar as linhas onde o valor de `Date` é inválido (por exemplo, linhas com "MMM")
        data = data[~data['Date'].isin(['Ticker', 'MMM'])]

        # Formatar a coluna `Date` para exibir apenas a data no formato YYYY-MM-DD
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

        # Garantir que as colunas estejam na ordem correta
        data = data[['Date', 'Close', 'Adj Close', 'High', 'Low', 'Open', 'Volume', 'Symbol', 'Name']]

        # Adicionar os dados ao arquivo CSV
        data.to_csv(csv_file, mode='a', header=False, index=False)
        
        #print(f"Dados de {ticker} ({name}) baixados e armazenados.")
    except Exception as e:
        print(f"Erro ao baixar dados para {ticker}: {e}")

# Baixar os dados para cada empresa e adicionar ao arquivo CSV
for ticker, name in zip(tickers, company_names):
    download_and_store_company_data(ticker, name)
    print(f"Dados da empresa {ticker} processados.")

print("Processo concluído!")
