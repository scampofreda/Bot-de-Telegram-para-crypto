# Importo la libreria requests para poder hacer uso de la api de https://min-api.cryptocompare.com/
import requests

# Creo la funcion "obtener_precios"
def obtener_precios():
    # Guardo en la variable "coins" los tickers de los cuales me interesa extraer datos
    coins = ["BTC", "ETH", "XRP", "LTC", "SLP", "ADA", "DOT", "LINK", "BNB", "XLM"]
    # Guardo en "crypto data" la url con el endpoint que voy a consumir
    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

# Creo un diccionario vacio, que voy a usar para ordenar los datos en sus respectivas variables a traves de un loop
    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "precio": crypto_data[i]["USD"]["PRICE"],
            "variacion_dia": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "variacion_hora": crypto_data[i]["USD"]["CHANGEPCTHOUR"],
            "minimo":crypto_data[i]["USD"]["LOWDAY"],
            "maximo":crypto_data[i]["USD"]["HIGHDAY"]
        }

    return data

# Archivo raiz
if __name__ == "__main__":
    print(obtener_precios())