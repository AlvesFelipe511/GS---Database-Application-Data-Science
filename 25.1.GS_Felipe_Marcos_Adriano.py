categoria = ["Crianças", "adulto", "idoso", "pessoas com mobilidade reduzida", "feridos"]
qtd = int(input('Informe a quantidade de desastres registrados: '))

for _ in range(qtd):
    validador = False
    while not validador:
        tipo_desastre = str(input('Informe o tipo de desastre: '))
        pais_desastre = str(input('Informe o país do desastre: '))
        cidade_desastre = str(input('Informe a cidade do desastre: '))
        bairro_desastre = str(input('Informe o bairro do desastre: '))
        rua_desastre = str(input('Informe a rua do desastre: '))
        
        qtd_vitimas = int(input('Informe a quantidade total de vítimas: '))
        soma_vitimas = 0
        
        for tipo in categoria:
            quantidade_vitimas = int(input(f'Informe a quantidade de vítimas do tipo {tipo}: '))
            soma_vitimas += quantidade_vitimas 
        
        if soma_vitimas != qtd_vitimas:
            print('A soma das vítimas por categoria não bate com a quantidade total.')
            print(f"Soma das categorias: {soma_vitimas}, Total informado: {qtd_vitimas}")
            print("Preencha novamente os dados deste desastre.\n")
        else:
            print("Dados registrados com sucesso, inserido o seguinte desastre:.\n")
            print(f'Tipo: {tipo_desastre}, País: {pais_desastre}, Cidade: {cidade_desastre}, Bairro: {bairro_desastre}, Rua: {rua_desastre}')
            validador = True 
