import requests 

def get_clima(cidade, api_key):
    url =  f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        cidade = data["name"]
        temperatura = data["main"]["temp"]
        sensacao = data["main"]["fells_like"]
        clima = data["main"][0]["description"]
        umidade = data["main"]["humidity"]

        print(f"Cidade: {cidade}")
        print(f"Temperatura: {temperatura} °C (sensacao): {sensacao} °C ")
        print(f"Clima: {clima}")
        print(f"Umidade: {umidade}%")
    
    else: 
        print("Erro ao buscar dados, verifique a cidade ou sua chave de API")

API_KEY = "SUA_CHAVE_AQUI"
cidade = input("digite o nome da sua cidade")
get_clima(cidade, API_KEY)