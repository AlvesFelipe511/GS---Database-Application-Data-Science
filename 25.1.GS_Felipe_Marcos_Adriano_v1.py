categoria = ["Crianças", "adulto", "idoso", "pessoas com mobilidade reduzida", "feridos"]

qtd_total = 0 

qtd = int(input('Informe a quantidade de desastres registrados: '))
categorias_soma_vitimas = 0

local = []
qts_categorias_categorias = []
nr_categorias = []


qtd_categorias_vitimas = []
descricao_categorias_vitimas = []


print("\n=========================================")
print("Total de desastres registrados:", qtd)
print("=========================================\n")
descricao_tipo_desastre = []
total_vitima__por_desastre = []

for _ in range(qtd):
    validador = False
    while not validador:
        tipo_desastre = str(input('Informe o tipo de desastre: '))
        descricao_tipo_desastre.append(tipo_desastre)
        pais_desastre = str(input('Informe o país do desastre: '))
        cidade_desastre = str(input('Informe a cidade do desastre: '))
        bairro_desastre = str(input('Informe o bairro do desastre: '))
        rua_desastre = str(input('Informe a rua do desastre: '))
        local.append(f'pais: {pais_desastre}, cidade: {cidade_desastre}, bairro: {bairro_desastre}, rua: {rua_desastre}')
        
        qtd_vitimas = int(input('Informe a quantidade total de vítimas: '))
        total_vitima__por_desastre.append(qtd_vitimas)
        soma_vitimas = 0


        for tipo in categoria:
            quantidade_vitimas = int(input(f'Informe a quantidade de vítimas do tipo {tipo}: '))
            print(f'Quantidade de vítimas do tipo {tipo}: {quantidade_vitimas}')
            qtd_categorias_vitimas.append(quantidade_vitimas)
            descricao_categorias_vitimas.append(tipo)
            soma_vitimas += quantidade_vitimas 
            categorias_soma_vitimas += quantidade_vitimas
            qtd_total += quantidade_vitimas

                    
        if soma_vitimas != qtd_vitimas:
            print('A soma das vítimas por categoria não bate com a quantidade total.')
            print(f"Soma das categorias: {soma_vitimas}, Total informado: {qtd_vitimas}")
            print("Preencha novamente os dados deste desastre.\n")
        else:
            print("Dados registrados com sucesso\n")
            maior_desastre = max(qtd_categorias_vitimas)
            indice_maior = qtd_categorias_vitimas.index(maior_desastre)
            id_desastre_maior = descricao_categorias_vitimas[indice_maior]
            print(f"Categoria mais afetada:{id_desastre_maior}")
            validador = True 

            print("\n=========================================")


maior_desastre = max(total_vitima__por_desastre)
indice_maior = total_vitima__por_desastre.index(maior_desastre)
id_desastre_maior = descricao_tipo_desastre[indice_maior]
print(f'Maior quatidade de afetados: {qtd_total}')
print(id_desastre_maior)
print(f'{local[indice_maior]}')


                


