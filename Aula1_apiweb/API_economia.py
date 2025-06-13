import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()

cotacao_dolar = cotacao['USDBRL']['bid']
cotacao_euro = cotacao['EURBRL']['bid']
cotacao_bitcoin = cotacao['BTCBRL']['bid']

print(f"A cotação do Dolar {cotacao_dolar}")
print(f"A cotação do Euro {cotacao_euro}")
print(f"A cotação do Bitcoin {cotacao_bitcoin}")
