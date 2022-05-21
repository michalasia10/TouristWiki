import requests

api_key = "5ae2e3f221c38a28845f05b65eae23667ad956ca2bd118e97d015aa2"

""" przykładowe połączenie do obiektu """
response = requests.get("http://api.opentripmap.com/0.1/en/places/xid/Q372040?apikey="+api_key)
print(response.json())


