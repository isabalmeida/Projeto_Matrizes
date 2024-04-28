def selecionar_tipo_lanche():
    print("Selecione o tipo de lanche:")
    print("1. For Mata-fome")
    print("2. Barba-byte")
    print("3. Default")
    print("4. Ba-code")
    opcao = int(input("Digite o número correspondente ao lanche desejado: "))

    tipos_lanche = {
        1: "For Mata-fome",
        2: "Barba-byte",
        3: "Default",
        4: "Ba-code"
    }

    # Se a opção não existir, retorna "Default"
    return tipos_lanche.get(opcao, "Default")


def obter_precos_custo():
    # Solicita os preços de custo ao usuário
    custo_pao = float(input("Preço de custo do pão: "))
    custo_alface = float(input("Preço de custo do alface: "))
    custo_tomate = float(input("Preço de custo do tomate: "))
    custo_mussarela = float(input("Preço de custo da mussarela: "))
    custo_hamburguer = float(input("Preço de custo do hambúrguer: "))
    custo_bacon = float(input("Preço de custo do bacon: "))
    custo_maionese = float(input("Preço de custo da maionese: "))
    custo_barbecue = float(input("Preço de custo do molho barbecue: "))
    custo_cebola = float(input("Preço de custo da cebola: "))

    return {
        'pao': custo_pao,
        'alface': custo_alface,
        'tomate': custo_tomate,
        'mussarela': custo_mussarela,
        'hamburguer': custo_hamburguer,
        'bacon': custo_bacon,
        'maionese': custo_maionese,
        'barbecue': custo_barbecue,
        'cebola': custo_cebola
    }


def obter_ingredientes_lanche(tipo_lanche):
    ingredientes = {
        "For Mata-fome": ['pao', 'hamburguer', 'mussarela', 'maionese', 'alface', 'tomate'],
        "Barba-byte": ['pao', 'hamburguer', 'mussarela', 'maionese', 'cebola', 'barbecue'],
        "Default": ['pao', 'hamburguer', 'mussarela', 'maionese', 'alface', 'tomate', 'cebola', 'bacon'],
        "Ba-code": ['pao', 'hamburguer', 'mussarela', 'maionese', 'bacon']
    }
    return ingredientes.get(tipo_lanche, [])


def calcular_preco_lanche(quantidades, precos_custo):
    total_custo = 0

    # Calcula o custo total dos ingredientes
    for ingrediente, quantidade in quantidades.items():
        total_custo += quantidade * precos_custo[ingrediente]

    # Calcula o preço final do lanche com 50% a mais do custo
    preco_final = 1.5 * total_custo

    return preco_final


def main():
    # Seleciona o tipo de lanche
    tipo_lanche = selecionar_tipo_lanche()

    # Obtém os preços de custo dos ingredientes do usuário
    precos_custo = obter_precos_custo()

    # Obtém os ingredientes específicos para o tipo de lanche escolhido
    ingredientes_lanche = obter_ingredientes_lanche(tipo_lanche)

    # Solicita as quantidades de ingredientes ao usuário apenas para o lanche escolhido
    quantidades = {}
    for ingrediente in ingredientes_lanche:
        quantidades[ingrediente] = int(input(f"Quantidade de {ingrediente}: "))

    # Calcula o preço final do lanche
    preco_final = calcular_preco_lanche(quantidades, precos_custo)

    # Exibe o preço final para o usuário
    print(f"O valor do lanche '{tipo_lanche}' é: R$ {preco_final:.2f}")


# Executa o programa
if __name__ == "__main__":
    main()
