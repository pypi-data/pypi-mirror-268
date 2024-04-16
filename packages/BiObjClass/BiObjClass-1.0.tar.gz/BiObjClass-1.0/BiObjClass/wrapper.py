import csv

def bilex(R_file, T_file, has_header=False):
    """
    Calcula a matriz A usando a abordagem biobjetiva lexicográfica.
    
    Args:
        R_file (str): Nome do arquivo R contendo os valores para R. Valores da execução do algoritmo.
        T_file (str): Nome do arquivo T contendo os valores para T. Valores com o tempo de execução dos algoritmos.
        has_header (bool): Indica se o arquivo têm cabeçalho
    
    Returns:
        list: Matriz A resultante

    Abordagem biobjetiva lexicográfica:
        Mais detalhes sobre a abordagem biobjetiva lexicográfica podem ser encontrados em (https://...)
    """


    # Inicializa a lsita R como uma lista vazia
    R = []

    # Inicializa a lista T como uma lista vazia
    T = []

    # Inicializa a lista names como uma lista vazia
    names = []
    
    

    # Lê os valores do arquivo R_file e atribui a matriz vazia R, e adiciona os nomes à lista names
    with open(R_file, 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        if has_header:
            next(arquivo_csv)  # Pula a linha do cabeçalho
        for line in arquivo_csv:
            names.append(line[0])  # Adiciona o primeiro elemento de cada linha à lista names
            valores = [float(valor) if (valor != '' and valor != '0.0') else 0.0 for valor in line[1:]]
            R.append(valores)

    # Lê os valores do arquivo T_file e atribui a matriz vazia T, e adiciona os nomes à lista names
    with open(T_file, 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        if has_header:
            next(arquivo_csv)  # Pula a linha do cabeçalho
        for line in arquivo_csv:
            valores = [float(valor) if (valor != '' and valor != '0.0') else 0.0 for valor in line[1:]]
            T.append(valores)

    
    # Inicializa as variáveis m e n com o número total de listas em R e com o comprimento da última lista, respectivamente.
    m, n = len(R), (len(R[0-1]))
    
    # Inicializa a matriz A com o mesmo comprimento de R preenchida com 1's
    A = [[1] * n for _ in range(m)]



    # Bloco para calcular os valores da matriz A
    for i in range(0,m):
        maior = 1   # Variável para calcular a classificação do maior valor na matriz. (0.0 é considerado o maior valor) Os demais valores seguem a ordenação decimal.

        # Bloco que percorre cada linha da matriz A e atualiza os valores
        for j in range(n):

            # Caso haja apenas um valor na linha ele recebe 1.0
            if n == 0:
                A[i][j] = 1.0
            else:

                if R[i][j-1] == 0.0:
                    if R[i][j] != 0.0:  # Se o valor anterior de R (R[i][j-1]) for igual a zero e o atual R[i][j] for diferente de zero
                        maior += 1      # Soma 1 a variável maior
                        A[i][j] = A[i][j-1]     # O valor atual de A na linha recebe a classificação do anterior 
                        A[i][j-1] = maior       # e o atual recebe a maior classificação
                        # Fazer com que todos os zeros também recebam maior:
                        for k in range (j):
                            if R[i][k] == 0.0:  # Atribui a classificação maior em A para todos os valores 0.0 correspondentes em R 
                                A[i][k] = maior
  
                    # Caso o valor em R seja 0.0, A[i][j] recebe a maior classificação
                    else:
                        A[i][j] = maior
                        #Colocar todos os 0's de R faltantes como classificação maior em A
                        for k in range (j):
                            if R[i][k] == 0.0:
                                A[i][k] = maior
                        

                # Caso o anterior de R seja menor que o atual
                elif R[i][j-1] < R[i][j]:
                    maior += 1      # Incrementa maior já que um novo valor foi adicionado
                    # Bloco para atualizar os valores anteriores a R[i][j]
                    for k in range (j):
                            if R[i][k] == 0:    # Se o valor em R for 0.0, a posição em A correspondente recebe a maior classificação
                                A[i][k] = maior
                            elif R[i][k] == R[i][j]:    # Se o valor for igual a R[i][j], o equivalente de R[i][j] em A recebe a mesma classificação
                                A[i][j] = A[i][k]   
                                maior += 1
                            elif R[i][k] > R[i][j]:     # Se o valor for maior que R[i][j], sua classificação é aumentada
                                A[i][k] += 1
                            elif R[i][k] < R[i][j] and R[i][k] != 0.0:  # Se o valor for menor que R[i][j] então a classificação de A[i][j] é aumentada 
                                A[i][j] += 1

                # Caso a posição anterior de R tenha o mesmo valor que a atual
                elif R[i][j-1] == R[i][j]:
                    if T[i][j-1] < T[i][j]:  # Se o tempo do anterior for menor do que o atual então a posição atual em A recebe a classificação do anterior incrementada em 1
                        A[i][j] = A[i][j-1] + 1
                    elif T[i][j-1] > T[i][j]:  # Se o tempo do anterior for maior que o atual então a posição atual em A recebe a classificação da anterior, e a anterior recebe a atual + 1
                        A[i][j] = A[i][j-1]
                        A[i][j-1] = A[i][j] + 1 
                    else:
                        A[i][j] = A[i][j-1] # Caso os valores de tempo sejam iguais a atual recebe a classificação da anterior

                elif R[i][j] == 0.0:
                     A[i][j] = maior    # Se a posição atual em A tiver o correspondente em R igual a 0.0, A recebe a maior classificação

                # Caso a posição anterior de R tenha valor maior que a atual
                elif R[i][j-1] > R[i][j]:
                    # Bloco para atualizar os valores anteriores a R[i][j]
                    for k in range (j):
                        if R[i][k] > R[i][j]:   # Se o valor for maior que R[i][j], sua classificação em A é aumentada
                            A[i][k] += 1
                        elif R[i][k] < R[i][j]: # Se o valor for menor que R[i][j] então a classificação de A[i][j] é aumentada 
                            A[i][j] = A[i][j] + 1
                        elif R[i][k] == R[i][j]: # Se o valor for igual a R[i][j], então A[i][j] recebe a mesma classificação de A[i][k]
                            A[i][j] = A[i][k]


                #Ajustar os valores de classificação caso seja a última repetição do bloco
                if j == n-1:
                    n1 = -1     # Variável para verificar quantas posições dividem a classificação 1
                    n2 = -1     # Variável para verificar quantas posições dividem a classificação 2
                    n3 = -1     # Variável para verificar quantas posições dividem a classificação 3
                    n4 = -1     # Variável para verificar quantas posições dividem a classificação 4
                    n5 = -1     # Variável para verificar quantas posições dividem a classificação 5

                    # Bloco para atualizar os valores
                    for k in range (n):
                        if A[i][k] == 1:    # Se a posição A[i][k] tiver classificação igual a 1, o valor de n1 é incrementado
                            n1 += 1
                        elif A[i][k] == 2:
                            n2 += 1
                        elif A[i][k] == 3:
                            n3 += 1
                        elif A[i][k] == 4:
                            n4 += 1
                        elif A[i][k] == 5:
                            n5 +=1
                    
                    # Bloco que verifica a real classificação, atribui a classificação referente a quantas classificações menores foram encontradas
                    for k in range (n):
                        if A[i][k] == 4:      # Se a classificação for igual a 4, recebe como incremento quantos classificações repetidas houveram para classficações menores qe 4
                            A[i][k] += n1+n2+n3
                        if A[i][k] == 3:
                            A[i][k] += n1+n2
                        if A[i][k] == 2:
                            A[i][k] += n1


                    n1 = -1     # Variável para verificar quantas posições dividem a classificação 1
                    n2 = -1     # Variável para verificar quantas posições dividem a classificação 2
                    n3 = -1     # Variável para verificar quantas posições dividem a classificação 3
                    n4 = -1     # Variável para verificar quantas posições dividem a classificação 4
                    n5 = -1     # Variável para verificar quantas posições dividem a classificação 5


                    # Bloco para atualizar os valores
                    for k in range (n):
                        if A[i][k] == 1:    # Se houver apenas uma posição com classificação 1 n1 será igual a 0, caso contrário n1 receberá (a quantidade de posições com classificação 1) -1
                            n1 += 1
                        elif A[i][k] == 2:
                            n2 += 1
                        elif A[i][k] == 3:
                            n3 += 1
                        elif A[i][k] == 4:
                            n4 += 1
                        elif A[i][k] == 5:
                            n5 +=1

                    for k in range (n):
                        if A[i][k] == 4 and n4 >= 1:    # Para cada posição com a clasificação repetida a classificação e incrementada em 0.5
                            A[i][k] += 0.5
                    for k in range (n):
                        if A[i][k] == 3 and n3 >= 1:
                            A[i][k] += n3*0.5
                    for k in range (n):
                        if A[i][k] == 2 and n2 >= 1:
                            A[i][k] += n2*0.5
                    for k in range (n):
                        if A[i][k] == 1 and n1 >= 1:
                            A[i][k] += n1*0.5
                   
            
                
    return A



def run_biobjective_lexicographic():
    """
    Calcula a matriz A usando a abordagem biobjetiva lexicográfica. 
    Opção para o usuário não precisar passar os nomes dos arquivos como parâmetros
    
    Args:
    
    Returns:
        list: Matriz A resultante

    Abordagem biobjetiva lexicográfica:
        Mais detalhes sobre a abordagem biobjetiva lexicográfica podem ser encontrados em (https://...)
    """


    # Solicita o nome do arquivo R
    R_file = input("Informe o nome do arquivo R: ")

    # Solicita o nome do arquivo T
    T_file = input("Informe o nome do arquivo T: ")

    # Verifica se os arquivos têm cabeçalho
    has_header_input = input("Os arquivos têm cabeçalho? (S para Sim, N para Não): ").upper()
    has_header = has_header_input == 'S'

    # Chama a função biobjective_lexicographic automaticamente
    A = bilex(R_file, T_file, has_header)

    # Retorna a matriz
    return A






def par10(G_file, has_header = False):

    G = []

    names = []

    # Lê os valores do arquivo G_file e atribui a matriz vazia G, e adiciona os nomes à lista names
    with open(G_file, 'r') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        if has_header:
            next(arquivo_csv)  # Pula a linha do cabeçalho
        for line in arquivo_csv:
            names.append(line[0])  # Adiciona o primeiro elemento de cada linha à lista names
            valores = [float(valor) if (valor != '' and valor != '0.0') else 0.0 for valor in line[1:]]
            G.append(valores)


    # Inicializa as variáveis m e n com o número total de listas em G e com o comprimento da última lista, respectivamente.
    m, n = len(G), (len(G[0-1]))
    
    # Inicializa a matriz A com o mesmo comprimento de G preenchida com 1's
    A = [[1] * n for _ in range(m)]

    for i in range(0,m):
        

        # Bloco que percorre cada linha da matriz A e atualiza os valores
        for j in range(n):
            # Caso haja apenas um valor na linha ele recebe 1.0
            if n == 0:
                A[i][j] = G[i][j]
            else:
                A[i][j] = G[i][j]


        # Variável para calcular o maior valor na linha
        max = max(A[0])

        for j in range(n):
            # Caso A[i][j] == 0 então A[i][j] recebe o maior valor da linha multiplicado por 10
            if A[i][j] == 0:
                A[i][j] = max*10
        #A.sort()



#R_file = input("Informe o nome do arquivo R: ")
#T_file = input("Informe o nome do arquivo T: ")
#
#R = []
#T = []
#
#
#has_header_input = input("Os arquivos têm cabeçalho? (S para Sim, N para Não): ").upper()
#has_header = has_header_input == 'S'
#
#names = []
#
#
#
#
#A = bilex(R_file, T_file, has_header)
#tam = len(A)
#
#
## Exibir a matriz A
#with open('out.txt', 'w') as output_file:
#    for i in range(0, tam):
#        name = names[i]
#        formatted_row = [float(value) for value in A[i]]
#        print(f'{name: <30}{formatted_row}', file=output_file)