#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Trabalho final de CPD - FIFA 21 - Players.
#Abre e le o arquivo de nomes.
#Funcao que cria a tabela hash.    

import time  #Usado para cronometrar o tempo para gerar as estruturas utilizadas no trabalho.

#Classe que ira armazenar a funções do nodo da árvore trie.
#from types import NoneType

class TrieNode: 
    def __init__(self, char): 
        self.char = char 
        self.is_end = False 
        self.children = {}

#Classe que ira armazenar a funções da árvore trie. 
class Trie(object): 
    def __init__(self): 
        self.root = TrieNode("")
    
    #Função para inserir elementos na árvore.
    def insert(self, word): 
        node = self.root 
        for char in word:
            if char in node.children:
                node = node.children[char]
            else: 
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node         
        node.is_end = True
         
    def dfs(self, node, pre): 
        if node.is_end:
            self.output.append((pre + node.char))         
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    #Função para procurar elementos na árvore.     
    def search(self, x):        
        node = self.root         
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:               
                return []
        self.output = []
        self.dfs(node, x[:-1]) 
        return self.output

#Função que inserte todos os nomes na árvore trie.
def insert_trie(contents):
    for x in range (0, len(contents)):          #Percorre o vetor inteiro.
        for i in range (0, len(contents[x])):                               
            tr.insert(contents[x][i][1])        #Insere ela na trie.

def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][0], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_rating(hash_value, vet,contents[x])        #Chama a funcao que ira inserir os nomes na tabela hash.

def hash_table_players(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                             #Percorre todas os nomes da lista.                
        hash_value = horner_method_players_smp(contents[x][1], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash_value, vet,contents[x])                   #Chama a funcao que ira inserir os nomes na tabela hash.

def hash_table_players_in_rating(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][0], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_names_in_media(hash_value, vet,contents[x][0]) 

def insert_ratings(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][1], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_ratings_in_media(hash_value, vet,contents[x]) 

def get_media(vet):                     #pega os ratings atribuidos a cada jogador e faz a média,
    for i in range(0,len(vet)):         #alocando esse valor na segunda posição do array
        for j in range(0,len(vet[i])):  #de modo que a média é vet[1] e a quantidade de 
            if(len(vet[i][j])>2):       #ratings atribuidos é igual a len(vet) - 1
                media = 0
                cont = 0
                for k in range(1,len(vet[i][j])):
                    media += float(vet[i][j][k][0:3])
                    cont +=1
                media = media/cont
                media = ("{:.2}".format(media))
                vet[i][j][1] = media


#Calcula o polinomio de horner para a tabela hash dos JOGADORES.
def horner_method_players(word, M):
    p = 31
    hash_value = (p * int(word)) % M
    return(hash_value)       #Retorna a posição do vetor a ser colocado o jogador.

#Mesma função que a de cima, mas simplificada.
#Apenas calcula o hash e retorna ele.
def horner_method_players_smp(word, M):
    p = 31
    hash_value = 0   
    for i in word:        
            num = ord(i)
            hash_value = (p * hash_value + num) % M
    return(hash_value)
    
#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word, M):
    test = 0
    p = 11                                              #Primeiro numero primo maior que 10.
    hash_value = 0                                      #Hash comeca valendo 0.
    sigN = 7
    for i in word:                                      #Percorre a palavra.
        if (i == ','):
            test += 1                                           #Marca que passou pela primeira virgula.
        if (test == 1) and ((i != '\n') and (i != ',')):        #Testa se o char eh diferente de "\n" e ",".            
            num = ord(i)                                        #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash_value = ((sigN * hash_value) + num) % M        #Cria um polinomio correspondente a palavra.
            sigN -= 1            
    return(hash_value)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet, name):     
    vet[pos].append(name)
    return

def hash_insert_ratings_in_media(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i][0]==name[1]):
            vet[pos][i].append(name[2])
            return
    print('error')
    return

def hash_insert_names_in_media(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i]== [] ):
            vet[pos][i].append(name)
            return
    vet[pos].append([])
    i+=1
    vet[pos][i].append(name)
    return
        

def hash_insert_rating(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i][0]==name[0]):      #se o usuário já deu rating para outro jogador
            vet[pos][i].append(name[1])   #apenas dá um append com o ID do jogador e o rating
            vet[pos][i].append(name[2])
            return
    vet[pos].append(name)
    return



#Realiza a consulta na tabela hash dos jogadores.
def realizar_consulta_players(vet,name):    
    aux = horner_method_players_smp(name,len(vet))  #Calcula a posição em que está o nome solicitado na tabela hash.
    for i in range(0,len(vet[aux])):                #Declara uma string vazia, para guardar o nome do jogador.                     
        if(name == vet[aux][i][1]):                 #Caso o nome procurado exista na tabela:  
            player_id = vet[aux][i][0]  
            player_name = vet[aux][i][1]
            string = (player_id + '   ' + player_name + '   ')
            for x in range (2, len(vet[aux][i])):
                player_pos = vet[aux][i][x]                
                string = string + player_pos   
            string = string.replace("\n", "")         
            return (string)                         #Retorna todas as informações sobre o jogador solicitado.    
    return('Not found.')                            #Caso o jogador não exista.

#Função que consulta a hash pelo ID do jogador
def hash_consult_id(vet, id_player):
    aux = horner_method_players(id_player, len(vet))
    for i in range(0, len(vet[aux])):
        if (id_player == vet[aux][i][0]):
            return (vet[aux][i])



def chamou_tags(vet_insert, vet_tags):
    if(len(vet_insert)<2):
        print('Faltaram as tags')
        return
    lista_aux = junta_as_tags(vet_insert)
    
    lista_IDS = []
    lista_IDS_sem_repet = []
    for j in range(0,len(vet_tags)):
        for k in range(2,len(vet_tags[j])):
            if(lista_aux[0] == vet_tags[j][k]):
                lista_IDS.append(vet_tags[j][1])
    
    for i in range(0, len(lista_IDS)):
        for j in range(i+1,len(lista_IDS)):
            if(lista_IDS[i] == lista_IDS[j]):
                lista_IDS[j] = []

    for i in range(0, len(lista_IDS)):
        if(lista_IDS[i]):
            lista_IDS_sem_repet.append(lista_IDS[i])
    

    for i in range(1,len(lista_aux)):
        lista_IDS_sem_repet = busca_interseccao(lista_IDS_sem_repet,lista_aux[i],vet_tags)
        print(len(lista_IDS_sem_repet))
        


    #aqui printar os jogadores e tals
    # 
    # 
    # 
    #     
    print(lista_IDS_sem_repet) 
    
    return 




#pega a lista com os jogadores já verificados com a tag anterior
#e verifica com as outras tags

def busca_interseccao(listaaqui,tag,vetoriginal):   
    lista2 = []
    for i in range(0,len(vetoriginal)):
        for j in range(2,len(vetoriginal[i])):
            if(vetoriginal[i][j] == tag):
                for k in range(0,len(listaaqui)):
                    if(vetoriginal[i][1] == listaaqui[k]):
                        lista2.append(listaaqui[k])
                        
                        break
    lista3 = []
    for i in range(0, len(lista2)):
        for j in range(i+1,len(lista2)):
            if(lista2[i] == lista2[j]):
                lista2[j] = []
    
    for i in range(0, len(lista2)):
        if(lista2[i]):
            lista3.append(lista2[i])


    return(lista3)


#pega as tags separadas por espaço e junta elas pra serem consideradas
#uma só
def junta_as_tags(vet):
    aux = []
    stringaux = vet[1]
    for i in range(2,len(vet)):
        if((vet[i][0] == '\'') or (vet[i][0] == '\"')):
            aux.append(stringaux[1:len(stringaux)-1])
            stringaux = vet[i]
        else:
            stringaux = stringaux + ' ' + vet[i]
    aux.append(stringaux[1:len(stringaux)-1])
    return aux





#------------------------------------------------------------------
#Leitura dos arquivos do trabalho.
with open('players_clean2.csv') as f:   #Usei o arquivo clean2. O arquivo original não tava lendo por conta da acentuação em alguns nomes.
    players = f.readlines()             #Armazena cada campo em uma posição do vetor players.

for i in range(0,len(players)):
    b = players[i].lower()
    a = b.split(',')
    players[i] = a

#with open('rating.csv') as f:          #Lê o arquivo rating.
#    rating = f.readlines()             #Armazena cada campo em uma posição do vetor rating.

with open('minirating.csv') as f:       #Arquivo minirating. To usando ele só pra não travar o programa inteiro.
    rating = f.readlines()              #Armazena cada campo em uma posição do vetor rating.   

for i in range(0,len(rating)):
    a=rating[i].split(',')
    rating[i]=a        


with open('tags.csv') as f:             #Lê o arquivo tags.csv. 
    tags = f.readlines()                #Armazena cada campo em um posição do vetor tags.
  
for i in range(0,len(tags)):
    b = tags[i].lower()
    b= b[0:len(b)-1]
    a = b.split(',')
    tags[i] = a

del rating[0]                          #Elimina a primeira posição do vetor.
del tags[0]                            #Elimina a primeira posição do vetor.
del players[0]                         #Elimina a primeira posição do vetor.
#------------------------------------------------------------------

#------------------------------------------------------------------
#N/M = 1/3
M = int(len(rating)/4) #M será o tamanho da tabela Hash a ser criada para armazenar as médias das avaliações e o total de avaliações para cada jogador.
#Rating_vet é uma tabela Hash que vai armazenar em cada nodo, todas as notas de um mesmo jogador.
#Atualmente anda dando alguns problemas nela, ta armazendo as vezes 2 ou 3 jogadores diferentes no mesmo nodo.
rating_vet = [[] for _ in range(0,M)]   #Vetor que ira armazenar a tabela hash com as notas de cada jogador.   
hash_table(rating, M, rating_vet)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------

#caad valor dos ratings na tabela hash é um array com o primeiro elemento representando
#o ID do usuário e os elementos seguintes são o ID do jogador que ele deu review e a nota 
#atribuída, podendo repetir esses elementos mais de uma vez caso o usuário tenha dado review 
#a mais de um jogador EX:

#['20434', '220440', '5.0\n', '200529', '3.0\n']
#ID do usuário: 20434
#review para o jogador de ID 220440: 5.0
#review para o jogador de ID 200529: 3.0



'''
for i in range(0,len(rating_vet)):
    if(len(rating_vet[i])>0):
        for j in range(0,len(rating_vet[i])):
            if(len(rating_vet[i][j])>3):
                print(rating_vet[i][j])
                '''
#------------------------------------------------------------------
#Criação da tabela Hash com as informações complementares dos jogadores.
M = int(len(players)/5)                           
players_vet = [[] for _ in range(0,M)]            #Vetor que ira armazenar a tabela hash com as informações adicionais de cada jogador.
hash_table(players, M, players_vet)              #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------

#------------------------------------------------------------------
#Criação da tabela Hash com as informações complementares dos jogadores.
M = int(len(players)/5)                           
players_vet_name = [[] for _ in range(0,M)]            #Vetor que ira armazenar a tabela hash com as informações adicionais de cada jogador.
hash_table_players(players, M, players_vet_name)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------

players_media =[[[]] for _ in range(0,M)]
hash_table_players_in_rating(players,M,players_media)

insert_ratings(rating,M,players_media)

get_media(players_media)





print(tags[1])
print(rating_vet[3])
print(players_vet[1])
print(players_media[422])



#------------------------------------------------------------------
#Árvore trie com os nomes dos jogadores.
tr = Trie()
#Chama a função que vai inserir na árvore trie todos os nomes dos jogadores.
insert_trie(players_vet_name)


rating = 0
running = 1                         #Variável que vai controlar quando o programa irá terminar.
while (running == 1):               #Loop para deixar o programa rodando.
    text = input("Please insert a name to search. ")
    text = text.lower()
    text = text.split(' ')          #Separa o texto em diferentes partes.
    if (text[0].lower == 'exit'):         #Exit para terminar o programa.
        print("Ending program.")
        running = 0             
    elif (text[0] == 'player'):     #Caso digite player, procura o jogador solicitado.                                           
        if (len(text) >= 2):
            text2 = text[1]
            for w in range(2,len(text)):
                text2 = text2 + ' ' + text[w] 
            consult = (tr.search(text2))          #Pega todos os nomes, dado o prefixo dado   
            print("\nsofifa_id   name              player_positions   rating   count")
            for x in consult:                                             #Para cada nome encontrado.
                info = realizar_consulta_players(players_vet_name,x)      #Recebe o resto das informações pela tabela hash dos jogadores.
                str_aux = info
                str_aux = str_aux.split(" ")
                player_note = hash_consult_id(players_media, str_aux[0])
                count = (len(player_note) - 1)
                if(len(player_note)>1):
                    rating = player_note[1]
                else:
                    rating = "NA"
                info = info + "       " + str(rating) + "    " + str(count) 
                print(info)                                               #Printa as informações adicionais.
        else:
            print("Please, insert a name after player")    #Caso o usuário insira somente "player".            
    
    elif(text[0] == 'tags'):
        chamou_tags(text, tags)
    
    
    else:
        print("Wrong command. Please, try again. ")        #Caso o usuário insira algum comando inválido. 
#--------------------------------------------------------
# 
#   O que a gente tem de lista e array
# 
# 
#   rating_vet = usuário,jogador,rating,jogador,rating...
#
#   players_vet = ID, nome, posição
# 
#   players_media = ID, rating, rating, rating...
# 
# #
#----------