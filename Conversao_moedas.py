import requests

def listar_moedas():
    """Busca lista de moedas disponíveis na API"""
    url = "https://api.exchangerate.host/symbols"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["symbols"]
    else:
        print("Erro ao buscar lista de moedas.")
        return {}

def converter_moeda(valor, de, para):
    """Converte valores em tempo real"""
    url = f"https://api.exchangerate.host/convert?from={de}&to={para}&amount={valor}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        print("Erro ao acessar a API.")
        return None

def menu():
    moedas = listar_moedas()
    if not moedas:
        return
    
    print("--- Conversor de Moedas em Tempo Real --- \n")

    while True:
        print("\nMenu:")
        print("1 - Converter moeda")
        print("2 - Listar moedas disponíveis")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                valor = float(input("Digite o valor: "))
                moeda_origem = input("De (ex: USD, BRL, EUR): ").upper()
                moeda_destino = input("Para (ex: USD, BRL, EUR): ").upper()

                if moeda_origem not in moedas or moeda_destino not in moedas:
                    print("Moeda inválida! Digite novamente.")
                    continue

                resultado = converter_moeda(valor, moeda_origem, moeda_destino)
                if resultado is not None:
                    print(f"\n {valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")
            except ValueError:
                print("Digite um valor numérico válido!")

        elif escolha == "2":
            print("\nMoedas disponíveis:")
            for codigo, info in list(moedas.items())[:30]:  # mostra só as 30 primeiras
                print(f"{codigo} - {info['description']}")
            print("... (existem mais moedas, consulte a API)")

        elif escolha == "0":
            print("Saindo do conversor...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
