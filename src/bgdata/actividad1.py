import requests
import json



def get_data_api(url="",params={}):
    url = "{}/{}/{}/".format(url,params["coin"],params["method"])
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(error)
        return {}
    

parameters = {"coin":"BTC","method":"ticker"}
url = "https://www.mercadobitcoin.net/api"
datos = get_data_api(url=url, params=parameters)

if len(datos)>0:
    print(json.dumps(datos,indent=4))
else:
    print("No data found")