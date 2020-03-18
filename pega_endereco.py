import requests

def main():

    print('Consulta CEP')
    print()

    cep_input = input('Digite um CEP: ')

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print(address_data)
    else:
        print('CEP Inválido')

if __name__ == "__main__":
    main()