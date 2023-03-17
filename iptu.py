while True:
    try:
        print('-----------Calculadora de IPTU----------------')
        valordoimovel = float (input('digite o valor do imovel: '))
        valordoiptu = float (input('digite a taxa anual do iptu (Ex: 1.5): '))
        valordoiptu = valordoiptu / 100
        valordoiptu = valordoiptu * valordoimovel
        print(f"O valor anual do iptu é de R$:{valordoiptu}")
    except:
        print("digite um valor valido")
