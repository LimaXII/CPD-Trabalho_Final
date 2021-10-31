#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Trabalho final de CPD - FIFA 21 - Players.
#Abre e le o arquivo de nomes.
#Funcao que cria a tabela hash.
def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (1, len(rating_vet)):                #Percorre todas os nomes da lista.                
        hash_value = horner_method(contents[x], M)      #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash_value, vet,contents[x])        #Chama a funcao que ira inserir os nomes na tabela hash.

#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word, M):
    p = 11                                              #Primeiro numero primo maior que 10.
    hash_value = 0                                      #Hash comeca valendo 0.
    for i in word:                                      #Percorre a palavra.
        if ((i != '\n') and (i != ',')):                #Testa se o char eh diferente de "\n" e ",".            
            num = ord(i)                                #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash_value = (p * hash_value + num) % M     #Cria um polinomio correspondente a palavra.            
    return(hash_value)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet, name):     
    vet[pos].append(name)
    return

with open('players_clean2.csv') as f:   #Usei o arquivo clean2. O arquivo original não tava lendo por conta da acentuação em alguns nomes.
    players = f.readlines()             #Armazena cada campo em uma posição do vetor players.
                      
#with open('rating.csv') as f:          #Lê o arquivo rating. Arquivo ENORME que consome muito do programa. Precisamos rever isso.
#    rating = f.readlines()             #Armazena cada campo em uma posição do vetor rating.

with open('minirating.csv') as f:       #Arquivo minirating. To usando ele só pra não travar o programa inteiro.
    rating = f.readlines()              #Armazena cada campo em uma posição do vetor rating.

with open('tags.csv') as f:             #Lê o arquivo tags.csv. 
    tags = f.readlines()                #Armazena cada campo em um posição do vetor tags.

#N/M = 1/5
M = int(len(rating)/5)                 #M será o tamanho da tabela Hash a ser criada para armazenar as médias das avaliações e o total de avaliações para cada jogador.
rating_vet = [[] for _ in range(0,M)]  #Vetor que ira armazenar a tabela hash.   
hash_table(rating, M, rating_vet)             #Chama a funcao para criar a tabela hash.
