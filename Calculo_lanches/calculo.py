def calcular_preco_lanche(quantidades, precos_custo, tipo_lanche):
    total_custo = 0

    # Calcula o custo total dos ingredientes
    total_custo += quantidades['pao'] * precos_custo['pao']
    total_custo += quantidades['alface'] * precos_custo['alface']
    total_custo += quantidades['tomate'] * precos_custo['tomate']
    total_custo += quantidades['queijo'] * precos_custo['queijo']
    total_custo += quantidades['presunto'] * precos_custo['presunto']
    total_custo += quantidades['hamburguer'] * precos_custo['hamburguer']
    total_custo += quantidades['bacon'] * precos_custo['bacon']
    total_custo += quantidades['maionese'] * precos_custo['maionese']
    total_custo += quantidades['barbecue'] * precos_custo['barbecue']

    # Calcula o preço final do lanche com 50% a mais do custo
    preco_final = 1.5 * total_custo

    return preco_final


def obter_precos_custo():
    # Solicita os preços de custo ao usuário
    custo_pao = float(input("Preço de custo do pão: "))
    custo_alface = float(input("Preço de custo do alface: "))
    custo_tomate = float(input("Preço de custo do tomate: "))
    custo_queijo = float(input("Preço de custo do queijo: "))
    custo_presunto = float(input("Preço de custo do presunto: "))
    custo_hamburguer = float(input("Preço de custo do hambúrguer: "))
    custo_bacon = float(input("Preço de custo do bacon: "))
    custo_maionese = float(input("Preço de custo da maionese: "))
    custo_barbecue = float(input("Preço de custo do molho barbecue: "))

    return {
        'pao': custo_pao,
        'alface': custo_alface,
        'tomate': custo_tomate,
        'queijo': custo_queijo,
        'presunto': custo_presunto,
        'hamburguer': custo_hamburguer,
        'bacon': custo_bacon,
        'maionese': custo_maionese,
        'barbecue': custo_barbecue
    }


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


def main():
    # Obtém os preços de custo dos ingredientes do usuário
    precos_custo = obter_precos_custo()

    # Seleciona o tipo de lanche
    tipo_lanche = selecionar_tipo_lanche()

    # Solicita as quantidades de ingredientes ao usuário
    quantidades = {
        'pao': int(input("Quantidade de pães: ")),
        'alface': int(input("Quantidade de alface: ")),
        'tomate': int(input("Quantidade de tomate: ")),
        'queijo': int(input("Quantidade de queijo: ")),
        'presunto': int(input("Quantidade de presunto: ")),
        'hamburguer': int(input("Quantidade de hambúrguer: ")),
        'bacon': int(input("Quantidade de bacon: ")),
        'maionese': int(input("Quantidade de maionese (porção): ")),
        'barbecue': int(input("Quantidade de barbecue (porção): "))
    }

    # Calcula o preço final do lanche
    preco_final = calcular_preco_lanche(quantidades, precos_custo, tipo_lanche)

    # Exibe o preço final para o usuário
    print(f"O valor do lanche '{tipo_lanche}' é: R$ {preco_final:.2f}")


# Executa o programa
if __name__ == "__main__":
    main()
