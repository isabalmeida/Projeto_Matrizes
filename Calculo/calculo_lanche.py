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

    return tipos_lanche.get(opcao, "Default")


def obter_precos_custo():
    print("Por favor, escolha o mercado para inserir os preços de custo:")
    print("1. Mercado Extra")
    print("2. Mercado Pão de açúcar")
    opcao_mercado = int(
        input("Digite o número correspondente ao mercado desejado: "))

    if opcao_mercado == 1:
        mercado = "Extra"
    elif opcao_mercado == 2:
        mercado = "Pão de açúcar"
    else:
        print("Opção inválida. Selecionando mercado Extra por padrão.")
        mercado = "Extra"

    print(f"Valores de custo para o mercado {mercado}:")
    custo_alface = float(input(f"Preço de custo do alface ({mercado}): "))
    custo_tomate = float(input(f"Preço de custo do tomate ({mercado}): "))
    custo_mussarela = float(
        input(f"Preço de custo da mussarela ({mercado}): "))
    custo_hamburguer = float(
        input(f"Preço de custo do hambúrguer ({mercado}): "))
    custo_bacon = float(input(f"Preço de custo do bacon ({mercado}): "))
    custo_maionese = float(input(f"Preço de custo da maionese ({mercado}): "))
    custo_barbecue = float(
        input(f"Preço de custo do molho barbecue ({mercado}): "))
    custo_cebola = float(input(f"Preço de custo da cebola ({mercado}): "))
    custo_pao = float(input(f"Preço de custo do pão"))

    return {
        'alface': custo_alface,
        'tomate': custo_tomate,
        'mussarela': custo_mussarela,
        'hamburguer': custo_hamburguer,
        'bacon': custo_bacon,
        'maionese': custo_maionese,
        'barbecue': custo_barbecue,
        'cebola': custo_cebola,
        'pao': custo_pao
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

    for ingrediente, quantidade in quantidades.items():
        total_custo += quantidade * precos_custo[ingrediente]

    preco_final = 1.5 * total_custo
    return preco_final


def main():
    tipo_lanche = selecionar_tipo_lanche()
    precos_custo = obter_precos_custo()

    # Obtém os ingredientes específicos para o tipo de lanche escolhido
    ingredientes_lanche = obter_ingredientes_lanche(tipo_lanche)

    quantidades = {}
    for ingrediente in ingredientes_lanche:
        quantidades[ingrediente] = int(input(f"Quantidade de {ingrediente}: "))

    preco_final = calcular_preco_lanche(quantidades, precos_custo)

    print(f"O valor do lanche '{tipo_lanche}' é: R$ {preco_final:.2f}")


if __name__ == "__main__":
    main()
